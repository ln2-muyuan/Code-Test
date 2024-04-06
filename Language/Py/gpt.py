import openai
openai.api_key = "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"

user_input = input("Input Your Question: ")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}],
    # max_tokens=100
)

print(completion.choices[0].message.content)