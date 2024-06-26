import json
import boto3
import json
import os
client = boto3.client('bedrock-runtime')
def lambda_handler(event, context):
    client = boto3.client('bedrock-runtime')

    modelId = "anthropic.claude-v2"
    accept = 'application/json'
    contentType = 'application/json'

    # create the prompt
    prompt_data = event['prompt']

    # titan_input = json.dumps({
    #     "inputText": prompt_data, 
    #     "textGenerationConfig" : { 
    #         "maxTokenCount": 512,
    #         "stopSequences": [],
    #         "temperature":0.1,  
    #         "topP":0.9
    #     }
    #     })

    claude_input = json.dumps({
        "prompt": f'Human: {prompt_data}\nAssistant:', 
        "max_tokens_to_sample": 500,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 1,
        "stop_sequences": [
        ]
    })

    # if modelId == "amazon.titan-text-express-v1":
    #     response = client.invoke_model(body=titan_input, modelId=modelId, accept=accept, contentType=contentType)
    #     response_body = json.loads(response.get("body").read())
    #     print(response_body.get("results")[0].get("outputText"))
    print("invoke_model")
    response = client.invoke_model(body=claude_input, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    return response_body['completion']
