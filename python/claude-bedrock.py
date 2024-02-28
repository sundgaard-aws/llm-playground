import anthropic_bedrock
from anthropic_bedrock import AnthropicBedrock
import boto3
import sys
import llm_file_utils

#context=load_file(s3Bucket='llm-playground-s3',s3Key='sample-c.txt',s3FileType="txt")
#context=load_file(s3Bucket='llm-playground-s3',s3Key='annual-report-nordea-bank-abp-2022.pdf',s3FileType="pdf")
context=llm_file_utils.load_file_s3(s3Bucket='llm-playground-s3',s3Key='deloitte-cn-fsi-importance-of-banking-as-a-service-en-211019.pdf',s3FileType="pdf")
#context=load_context()
#context="Not much to say"
client = AnthropicBedrock()
#prompt=f"<text>{context}</text>{anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text I provided. Give me a highlight from the text. {anthropic_bedrock.AI_PROMPT}"
#prompt=f"<text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text I provided. What is XTCKURATO? {anthropic_bedrock.AI_PROMPT}"
#prompt=f"<text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text I provided. According to their 2022 annual report how does Nordea intend to be the preferred financial partner in the Nordics? {anthropic_bedrock.AI_PROMPT}"
#human_prompt="Tell me about Bob the Baker in the context of BaaS."
#human_prompt="Write a perfect summary of the text I gave you in around 150 words."
#human_prompt="Write a summary of what BBVA are doing with BaaS in the text I gave you. Keep to around 150 words."
#human_prompt="Write a summary of what BBVA are doing with BaaS in the text I gave you."
human_prompt=input("What would you like to know?\n")
nudging="Emphasize any elements related to cloud and AWS. Keep to max 150 words."
#prompt=f"<text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text I provided. {human_prompt} {anthropic_bedrock.AI_PROMPT}"
prompt=f"<text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} You are an AWS cloud and FSI (Financial Services) expert. Read and memorize the text I provided. {human_prompt} {nudging} {anthropic_bedrock.AI_PROMPT}"
completion = client.completions.create(
    model="anthropic.claude-v2",
    max_tokens_to_sample=256,
    prompt=prompt
)
print(completion.completion)