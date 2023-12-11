import openai

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # You can try different engines based on your preference
        prompt=prompt,
        temperature=0.7,  # Adjust the temperature for more creative or focused responses
        max_tokens=150  # Adjust the maximum number of tokens in the response
    )

    return response.choices[0].text.strip()

# Simple conversation loop
print("Welcome to the ChatGPT Python Learning Assistant!")
print("You can start by asking questions about Python or JavaScript.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("ChatGPT: Goodbye! If you have more questions, feel free to ask later.")
        break

    prompt = f"You: {user_input}\nChatGPT:"
    response = chat_with_gpt3(prompt)
    print(response)
