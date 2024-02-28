from anthropic_bedrock import AnthropicBedrock, HUMAN_PROMPT, AI_PROMPT

client = AnthropicBedrock()

stream = client.completions.create(
    prompt=f"{HUMAN_PROMPT} Write a very short essay about space travel to Mars{AI_PROMPT}",
    max_tokens_to_sample=300,
    model="anthropic.claude-v2",
    stream=True,
)
for completion in stream:
    print(completion.completion, end="", flush=True)