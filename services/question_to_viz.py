from services.schema_generation import return_result_after_query_in_df,return_schema_short,return_schema
from services.connection_to_database import return_engine,return_session
from services.prompt_template import return_prompt_template,return_question_prompt,return_summary_roles
from services.connection_to_gpt import get_completion
from services.preprocessresponse import process_response
import regex as re
import json


def question_to_viz(connection_string,question):
    session=return_session(connection_string)
    engine=return_engine(connection_string)
    schema=return_schema_short(engine)
    prompt=return_prompt_template(question,schema)
    print(prompt)


    model='gpt-4'
    system_message="You are an AI assistant specialized in database analysis that can help in generate analytical questions and SQL queries."
    response,all_resp = get_completion(prompt)
    print(response)

    usd=83.25
    if(model=='gpt-3'):
        print(f"total token:{all_resp['usage']['total_tokens']}")
        print(f"cost : {all_resp['usage']['total_tokens']*2*0.000001*usd} indian rupees")
    elif (model=='gpt-4'):
        print(f"total token:{all_resp['usage']['total_tokens']}",'blue')
        print(f"cost : {all_resp['usage']['total_tokens']*6*0.00001*usd} indian rupees")
        
    code,data=process_response(response,session)
    return code,data


def prompt_to_questions(connection_string,role="CEO company"):
    session=return_session(connection_string)
    engine=return_engine(connection_string)
    schema=return_schema_short(engine)
    prompt=return_question_prompt(schema,role=role)
    print(prompt)


    model='gpt-3'
    system_message="You are an AI assistant specialized in database analysis that can help in generate analytical questions and SQL queries."
    response,all_resp = get_completion(prompt,system_message=system_message,model='gpt-3')
    print(response)

    usd=83.25
    if(model=='gpt-3'):
        print(f"total token:{all_resp['usage']['total_tokens']}")
        print(f"cost : {all_resp['usage']['total_tokens']*2*0.000001*usd} indian rupees")
    elif (model=='gpt-4'):
        print(f"total token:{all_resp['usage']['total_tokens']}",'blue')
        print(f"cost : {all_resp['usage']['total_tokens']*6*0.00001*usd} indian rupees")
    
    questions=re.findall(r'\d+\.\s+(.+\?)',response)
    return questions



def prompt_to_summary_roles(connection_string):
    session=return_session(connection_string)
    engine=return_engine(connection_string)
    schema=return_schema_short(engine)
    prompt=return_summary_roles(schema)
    print(prompt)


    model='gpt-3'
    response,all_resp = get_completion(prompt,model='gpt-3')
    print(response)

    usd=83.25
    if(model=='gpt-3'):
        print(f"total token:{all_resp['usage']['total_tokens']}")
        print(f"cost : {all_resp['usage']['total_tokens']*2*0.000001*usd} indian rupees")
    elif (model=='gpt-4'):
        print(f"total token:{all_resp['usage']['total_tokens']}",'blue')
        print(f"cost : {all_resp['usage']['total_tokens']*6*0.00001*usd} indian rupees")
    
    summary,roles=json.loads(response)['summary'],json.loads(response)['Roles']
    return roles,summary




def return_schema_in_database(connection_string):
    session=return_session(connection_string)
    engine=return_engine(connection_string)
    schema=return_schema(engine)
    return schema