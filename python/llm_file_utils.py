import os
import PyPDF2
import boto3
from io import BytesIO

def load_file_s3(s3Bucket:str, s3Key:str, s3FileType:str)->str:
    print("load_file_s3()")
    fileContents=read_from_cache(s3bucket=s3Bucket,s3key=s3Key)
    if(fileContents==None):
        if s3FileType == "pdf":
            fileContents=read_pdf_file_s3(s3Bucket,s3Key)
        else:
            fileContents=read_text_file_s3(s3Bucket,s3Key)
        #write_to_cache(s3bucket=s3Bucket,s3key=s3Key,data=fileContents)
        return fileContents
    else:
        return fileContents
    
def read_bytes_s3(s3Bucket:str, s3Key:str):
    s3Client = boto3.client('s3')
    obj = s3Client.get_object(Bucket=s3Bucket, Key=s3Key)
    file_bytes = obj['Body'].read()
    return file_bytes

def read_text_file_s3(s3Bucket:str, s3Key:str):
    s3Client = boto3.client('s3')
    obj = s3Client.get_object(Bucket=s3Bucket, Key=s3Key)
    file_bytes = obj['Body'].read()
    file_string = file_bytes.decode('utf-8')
    return file_string
    
def read_pdf_file_s3(s3Bucket:str, s3Key:str):
    pdf_bytes=read_bytes_s3(s3Bucket, s3Key)
     # Convert bytes to a file-like object
    pdf_file = BytesIO(pdf_bytes)
    pdf_reader = PyPDF2.PdfReader(pdf_file) 
    file_contents = ""
    
    # Extract text from each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        file_contents += page.extract_text()
        
    pdf_file.close()
    return file_contents

def write_to_cache(s3bucket:str, s3key:str, data:str):
    file = open(f"cache/{s3bucket}.{s3key}", "w")
    file.write(data) 
    file.close()

def read_from_cache(s3bucket:str, s3key:str)->str:
    file_path=f"cache/{s3bucket}.{s3key}"
    if os.path.exists(file_path):
        print("cache hit!")
        with open(file_path, 'r') as f:
            return f.read()
    else:
        print("cache miss!")
        return None