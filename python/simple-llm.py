import bedrock_client

bedrock = bedrock_client.BedrockClient()

prompt = "The capital of France is"
completion = "Paris"

bedrock.create_completion(
    prompt=prompt, 
    completion=completion,
    model="text-davinci-003",
    temperature=0.5,
    max_tokens=60
)

print("Created completion:")
print(prompt, completion)