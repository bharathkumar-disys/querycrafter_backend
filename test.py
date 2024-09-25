from services.schema_generation import return_result_after_query_in_df,return_schema_short
from services.connection_to_database import return_engine,return_session
from services.prompt_template import return_prompt_template
from services.connection_to_gpt import get_completion
from services.preprocessresponse import process_response
from services.question_to_viz import question_to_viz

connection_string=f'sqlite:///../TEXTSQL/database/bike_1/bike_1.sqlite'
# session=return_session(connection_string)
# engine=return_engine(connection_string)
# schema=return_schema_short(engine)
# #print(schema)
# # query='Select * from station;'
# # result=return_result_after_query_in_df(session, query)
# # print(result)

# question="What is the distribution of car makers by country?"
# prompt=return_prompt_template(question,schema)
# print(prompt)


# model='gpt-35-turbo'
# response,all_resp = get_completion(prompt)
# print(response)

# usd=83.25
# if(model=='gpt-35-turbo'):
#     print(f"total token:{all_resp['usage']['total_tokens']}")
#     print(f"cost : {all_resp['usage']['total_tokens']*2*0.000001*usd} indian rupees")
# elif (model=='gpt-4'):
#     print(f"total token:{all_resp['usage']['total_tokens']}",'blue')
#     print(f"cost : {all_resp['usage']['total_tokens']*6*0.00001*usd} indian rupees")
    
# code,data=process_response(response,session)
# print(code,data)

# question="What is the distribution of car makers by country?"
# code,data=question_to_viz(connection_string,question)
# print(code,data)






