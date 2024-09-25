from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL 
import pandas as pd
import os 


os.environ["SQLALCHEMY_SILENCE_UBER_WARNING"]="1"

def return_session(connection_string):
    engine = create_engine(connection_string,echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def return_engine(connection_string):
    #engine = create_engine(connection_string,echo=True)
    engine = create_engine(connection_string)
    return engine


def return_result_after_query_in_df(session, query):
    results = session.execute(query)
    column_names = [description for description in results.keys()]
    results_list = [dict(zip(column_names, row)) for row in results]
    result_df = pd.DataFrame(results_list)
    return result_df

def connectdatabasename_to_database(name):
    value=f"sqlite:///../database/{name}/{name}.sqlite"
    return value

def return_all_databases():
    sqlite=os.listdir('../database')
    return sqlite

if __name__=="__main__":
    connection_string=f'sqlite:///../database/bike_1/bike_1.sqlite'
    session=return_session(connection_string)
    query='Select * from station;'
    result=return_result_after_query_in_df(session, query)
    print(result)
            
  
   
    