import json
import os
import sys
from utils import bedrock, print_ww
import boto3

module_path = ".."
sys.path.append(os.path.abspath(module_path))

boto3_bedrock = bedrock.get_bedrock_client(

)