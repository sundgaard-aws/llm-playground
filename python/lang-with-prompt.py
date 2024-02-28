import json
import os
import sys
from utils import bedrock
import boto3
from langchain.llms.bedrock import Bedrock

# https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/01_Generation/02_contextual_generation.ipynb

module_path = ".."
sys.path.append(os.path.abspath(module_path))

boto3_bedrock = bedrock.get_bedrock_client(

)

inference_modifier = {'max_tokens_to_sample':4096, 
                      "temperature":0.5,
                      "top_k":250,
                      "top_p":1,
                      "stop_sequences": ["\n\nHuman"]
                     }

textgen_llm = Bedrock(model_id = "anthropic.claude-v2",
                    client = boto3_bedrock, 
                    model_kwargs = inference_modifier 
                    )