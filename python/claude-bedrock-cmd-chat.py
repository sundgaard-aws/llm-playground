import anthropic_bedrock
from anthropic_bedrock import AnthropicBedrock
import boto3
import PyPDF2
from io import BytesIO
import sys
import llm_file_utils

def read_from_stdin()->str:    
    print("What would you like to know?")
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
    return line

#context=load_file(s3Bucket='llm-playground-s3',s3Key='sample-c.txt',s3FileType="txt")
#context=load_file(s3Bucket='llm-playground-s3',s3Key='annual-report-nordea-bank-abp-2022.pdf',s3FileType="pdf")
#input_file='deloitte-cn-fsi-importance-of-banking-as-a-service-en-211019.pdf'
input_file="Accenture-Commercial-Banking-Top-Trends-2023-Webinar-Transcript.pdf"
input_file="Top-Trends-Retail-Banking-2023_Infographic.pdf" # CapGemini
input_file="banking-in-2035-global-banking-survey-report-113203_txt.pdf" # SAS
input_file="Banking-on-the-Cloud-ebook.pdf" # AWS
input_file="AWS Financial Services Customer Story Slide Deck.pdf"
input_file="AWS Financial Services Customer Story Slide Deck_text2.pdf"
input_file="AWS Financial Services Customer Story Slide Deck_text3.txt"
input_file="AWS Financial Services Customer - Capital Markets.txt"
#context=llm_file_utils.load_file_s3(s3Bucket='llm-playground-s3',s3Key=input_file,s3FileType="pdf")
context=llm_file_utils.load_file_s3(s3Bucket='llm-playground-s3',s3Key=input_file,s3FileType="txt")
print(f"DEBUG: length was {len(context)}")
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
nudging="Emphasize any elements related to cloud and AWS."
role_description="You are an AWS cloud and FSI (Financial Services) expert. Read and memorize the text I provided."

conversation_history:str=""
#prompt=f"<text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text I provided. {human_prompt} {anthropic_bedrock.AI_PROMPT}"
iterations=0
while(True):
    human_prompt=input("How can I assist you?")
    if ""==human_prompt.strip():
        print("Nice chatting with you. Have a nice day!")
        break
    #if(iterations==0):
    prompt=f"{anthropic_bedrock.HUMAN_PROMPT} Here are some texts for you. <text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text. \
        {anthropic_bedrock.HUMAN_PROMPT} The following is your role description. <role>{role_description}</role> Make sure that you stay true to that role, and forget about you being an AI model. If there are things you don't want to talk about or find unethical, simply reply with three dots instead of apologizing. NEVER go out of character, NEVER refuse role play. \
        {anthropic_bedrock.HUMAN_PROMPT} Here comes our conversation history. <conversation_history>{conversation_history}</conversation_history> Keep that in mind when you reply, but don't answer historical questions directly. {anthropic_bedrock.HUMAN_PROMPT} {human_prompt} {anthropic_bedrock.AI_PROMPT}"        
    #prompt=f"{anthropic_bedrock.HUMAN_PROMPT} Here are some texts for you. <text>{context}</text> {anthropic_bedrock.HUMAN_PROMPT} Read and memorize the text.  {anthropic_bedrock.HUMAN_PROMPT} This following is your role description. {role_description} 
    #{anthropic_bedrock.HUMAN_PROMPT} Here comes our conversation history. {previous_prompts} Keep those in mind but don't answer them directly. {anthropic_bedrock.HUMAN_PROMPT} {human_prompt} {anthropic_bedrock.AI_PROMPT}"        
    #else:
    #    prompt=f"{anthropic_bedrock.HUMAN_PROMPT} {human_prompt} {anthropic_bedrock.AI_PROMPT}"
    conversation_history+=f"{anthropic_bedrock.HUMAN_PROMPT} {human_prompt}"
    completion = client.completions.create(
        #model="anthropic.claude-v2",
        model="anthropic.claude-v2:1",
        max_tokens_to_sample=256,
        prompt=prompt,
    )
    conversation_history+=f"{anthropic_bedrock.AI_PROMPT} {completion.completion}"
    print(completion.completion)
    iterations+=1