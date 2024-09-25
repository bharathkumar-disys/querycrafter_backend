import regex as re
from tabulate import tabulate
from IPython.display import display, Markdown, Latex, HTML, JSON
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from services.connection_to_database import return_engine,return_session
import pandas as pd

def return_result_after_query_in_df(session, query):
    results = session.execute(query)
    
    # Get column names from query results
    column_names = [description for description in results.keys()]
    
    # Convert query results to a list of dictionaries
    results_list = [dict(zip(column_names, row)) for row in results]
    
    # Convert the list of dictionaries to a Pandas DataFrame
    result_df = pd.DataFrame(results_list)
    
    return result_df



def return_result_after_query(session, query):
    """_summary_

    Args:
        db_path (_type_): path of sqlite database
        query (_type_): sql query
        database (str, optional): which database connecting. Defaults to 'sqlite'.

    Returns:
        _type_: result after query
    """
    
    results = session.execute(query)
    column_names = [description for description in results.keys()]
    formatted_results = tabulate(results, headers=column_names, tablefmt="pretty")
    return formatted_results



def return_result_after_query_schema(session,query):
    """_summary_

    Args:
        db_path (_type_): path of sqlite database
        query (_type_): sql query
        database (str, optional): which database connecting. Defaults to 'sqlite'.

    Returns:
        _type_: result after query
    """

    results = session.execute(query)
    ans=""
    column_names = " ".join(results.keys())
    ans+=column_names
    for i in results.all():
        temp='\n'
        for k in i:
            temp+=str(k)+" "
        ans+=temp
    return ans
    

def return_schema(engine):
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    schema=''
    for table_name in table_names:
        schema+="\n"
        schema=schema+f"Table Name: {table_name}"
        columns = inspector.get_columns(table_name)
        for column in columns:
            schema+="\n"
            schema+=f"  Column Name: {column['name']}, Type: {column['type']}"
            
        foreign_keys = inspector.get_foreign_keys(table_name)
        for foreign_key in foreign_keys:
            schema += "\n"
            schema += f"  Foreign Key: {foreign_key['constrained_columns']} references {foreign_key['referred_table']}.{foreign_key['referred_columns']}"
    return schema






def return_schema_short(engine):
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    schema=''
    for table_name in table_names:
        schema+="\n"
        schema=schema+f"Table {table_name}, Columns= ["
        columns = inspector.get_columns(table_name)
        for column in columns:
            schema+=f"{column['name']}:{column['type']},"
        schema=schema[:-1]+"];"
        foreign_keys = inspector.get_foreign_keys(table_name)
        if(len(foreign_keys)>0):
            schema += "\nForeign_Keys=["
        for foreign_key in foreign_keys:
            
            schema += f"{table_name}.{foreign_key['constrained_columns'][0]}={foreign_key['referred_table']}.{foreign_key['referred_columns'][0]},"
        if(len(foreign_keys)>0):
            schema=schema[:-1]+'];'
    return schema


def return_schema_short_with_input(engine,query=None,limit=1):
    Session = sessionmaker(bind=engine)
    session = Session()
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    schema=''
    for table_name in table_names:
        schema+="\n"
        schema=schema+f"Table {table_name}, Columns= ["
        columns = inspector.get_columns(table_name)
        if query:
            pass
        else:
            query=f"select * from {table_name} limit {limit};"
        first_row=return_result_after_query_schema(session, query)
   
        
    
        for column in columns:
            schema+=f"{column['name']}:{column['type']},"
        schema=schema[:-1]+"];\n"
        schema+=f"Few sample of row is listed down  in {table_name} database table \n"

        schema+=first_row
        foreign_keys = inspector.get_foreign_keys(table_name)
        if(len(foreign_keys)>0):
            schema += "\nForeign_Keys=["
        for foreign_key in foreign_keys:
            
            schema += f"{table_name}.{foreign_key['constrained_columns'][0]}={foreign_key['referred_table']}.{foreign_key['referred_columns'][0]},"
        if(len(foreign_keys)>0):
            schema=schema[:-1]+'];'
    return schema
    


if __name__=="__main__":
    connection_string=f'sqlite:///../TEXTSQL/database/bike_1/bike_1.sqlite'
    session=return_session(connection_string)
    engine=return_engine(connection_string)
    schema=return_schema_short(engine)
    print(schema)
    query='Select * from station;'
    result=return_result_after_query_in_df(session, query)
    print(result)