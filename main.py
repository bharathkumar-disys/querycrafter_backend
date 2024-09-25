from typing import Union
from fastapi import FastAPI, HTTPException
from services.question_to_viz import question_to_viz,prompt_to_questions,return_schema_in_database,prompt_to_summary_roles
from services.connection_to_database import connectdatabasename_to_database,return_all_databases
from fastapi.middleware.cors import CORSMiddleware 
from models.user import UserLogin,Userresponseforviz,Userquestions,ErrorFeedback
import json

origins = [
    "http://localhost:3000", 
     "https://commentclassifier.azurewebsites.net",
     "https://cardcommentclassifier.azurewebsites.net",
     "http://localhost:4200", 
]


app = FastAPI(
    title="TextTOSql"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "Text to Sql"}

@app.post("/login")
async def login(userlogin: UserLogin):
    if userlogin.password=='raj':
        return userlogin.username
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    

@app.post("/response")
def get_data_viz(responseviz:Userresponseforviz):
    print(responseviz.message)
    database_name=responseviz.connection_string
    connection_string=connectdatabasename_to_database(database_name)
    question=responseviz.message
    code,data=question_to_viz(connection_string,question)
    return {"code": code, "data": data}

@app.post("/questions")
def get_questions_prompt(database:Userquestions):
    print(database.connection_string,database.role)
    database_name=database.connection_string
    connection_string=connectdatabasename_to_database(database_name)
    questions=prompt_to_questions(connection_string,role=database.role)
    return questions


@app.post("/summary_roles")
def get_summary_roles(database:Userquestions):
    print(database.connection_string)
    database_name=database.connection_string
    connection_string=connectdatabasename_to_database(database_name)
    roles,summary=prompt_to_summary_roles(connection_string)
    return roles,summary

@app.post("/feedback")
async def save_feedback(error_feedback: ErrorFeedback):
    print(error_feedback)
    # Load existing data from the JSON file if it exists
    try:
        with open("data/errortrack.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    # Append the new feedback to the data list
    data.append(error_feedback.dict())
    
    # Write the updated data back to the JSON file
    with open("data/errortrack.json", "w") as file:
        json.dump(data, file, indent=4)
    
    return "Feedback saved successfully"






@app.get("/database_list")
def get_avaialable_database():
    databases=return_all_databases()
    dataArray = []
     
    for i,j in enumerate(databases):
        temp={}
        temp['label']=j
        temp['value']=i
        dataArray.append(temp)


    return dataArray