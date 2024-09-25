import openai
import os
def get_completion(prompt,system_message=None, model="gpt-4"):
    openai.api_type = "azure"
    openai.api_version = "2023-07-01-preview"
    
    
    if(model=="gpt-3"):
        openai.api_base = "https://texttosqlproject.openai.azure.com/"
        try:
            openai.api_key=""
            
        except:
            print("not found key")
        engine='Gpt3TextSql'
       
        
    if(model=="gpt-4"):
        openai.api_base = "https://texttosqlproject.openai.azure.com/"
        openai.api_key =""
        engine='Gpt4TextSql'
        
        
    if system_message:
         messages = [
        {"role": "system",
         "content": system_message},
        {"role": "user",
         "content": prompt}
        ]
    else:
           messages = [
        {"role": "user",
         "content": prompt}
        ]
        
   
    response = openai.ChatCompletion.create(
        engine=engine,
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"],response


if __name__=="__main__":
    prompt="give me a sql query to fetch best grade in student table"
    response,_=get_completion(prompt)
    response_s,_=get_completion(prompt,system_message="You are an excellent sql query writer.")
    print("response without system:",response)
    print("response with system:",response_s)
    
    