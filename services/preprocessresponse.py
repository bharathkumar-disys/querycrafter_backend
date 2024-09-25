

import regex as re
from services.schema_generation import return_result_after_query_in_df
import json

def process_response(response,session):
    query=re.findall("'query':'(.*;)",response,re.DOTALL)[0]
    chart_type=re.findall("'chart_type':'(.*)',",response)[0]
    code=re.findall("'chart_code':'(.*)'",response,re.DOTALL)[0]
    
    df=return_result_after_query_in_df(session,query)
    data=[]

    for i in df.columns:
        temp={}
        temp['label']=i
        temp['values']=list(df[i])
        data.append(temp)
        
    # for j,i in enumerate(data):
    #     val=i['label']
    #     labl=f'[{val}]'
    #     code=code.replace(labl,f"this.data[{j}]['values']")
        
    
    y=code.replace('\n', '').replace('  ', '').replace("\'", "'").replace('\t', '').replace('\\', '')
    y="["+y+"]"
    code=json.loads(y)
    
    
    return code,data

    








