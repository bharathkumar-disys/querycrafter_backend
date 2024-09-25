
def return_prompt_template(question,schema):
    metadata="""
Important Notes
-- First read the schema of all tables before composing your query.
-- Make sure to understand the relationships between different tables to construct accurate joins.
-- Don't use "IN", "OR", "LEFT JOIN" as it might cause extra results, use "INTERSECT" or "EXCEPT" instead, and remember to use "DISTINCT" or "LIMIT" when necessary
-- Do not select extra columns that are not explicitly requested in the query.
"""
  
    ans_format="""
    [
    'query':'SELECT Gender as gender,Count(*) as total from students ;',
    'chart_type':'bar',
    'chart_code':' 
        {  
            "data": [{
                "x": ["gender"],
                "y": ["total"],
                "type": "bar"
            }],
            "layout": {
                "title": "Bar Chart",
                "width": 500, 
                "height": 500,
                "plot_bgcolor": "rgba(0,0,0,0)", 
                "paper_bgcolor": "rgba(0,0,0,0)" 
            }
        }
    '
    ]
    """
    

    prompt= f"""
Your task is to provide a SQL query based on the given question and database schema provided below in triple backticks.
Ensure the response only contains the SQL query and it is starting from the 'SELECT' clause.
{metadata}

Question:```{question}```

Database Schema:```{schema}```

And also suggest which chart is best to represent this data that i will get after query.
And give code for plotting chart in plotly js.


give output in json format ,one example given below:
Please strictly follow the json output for ans_format which I have speicified.
{ans_format}

    """
    

    return prompt



def return_question_prompt(schema,role="CEO of Company"):
    prompt= f"""
Your task is read and analyze the given schema and based on that create 10 different questions that should give excellent  
analytical insight to the user who is a {role}. It would be good, if you include questions that require SQL to use, Group by, aggregate 
function, min, max, probability etc. I want question to be more mathematical and analytical oriented.
Database Schema:```{schema}```

Give answer in Python list format: ["question1","question2","question3",...,"question10"]
 
"""
    return prompt


def return_summary_roles(schema):
    
    example="""
{
"summary":"This database has information about ....",
"Roles": ["HR Manager","Finance Manager","Sales Manager","Marketing Manager","IT Administrator","Customer Support Manager","Product Manager"]
}
    """
    prompt=f"""

Please provide a brief summary of the database schema and suggest roles that users might assume while asking question for query 
a database which schema below in triple backticks.


Give a brief summary.It should not exceed more than 30 words.
Database Schema:```{schema}```

please follow json format for giving output:
example:
{example}
"""

    return prompt