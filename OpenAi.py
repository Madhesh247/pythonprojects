from openai import OpenAI

client = OpenAI(
    api_key="Enter Your Api"
)

messages = [
    {"role": "system", "content": "You are an intelligent assistant."}
]

while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        print("ChatGPT: Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("ChatGPT:", reply)

    messages.append({"role": "assistant", "content": reply})

