from cli_chat_bot.llm_config import client, MODEL

SYSTEM_PROMPT = "You are a helpful, concise assistant."
MAX_MESSAGES = 20

messages = [{"role": "system", "content": SYSTEM_PROMPT}]


def trim_history():
    if len(messages) > MAX_MESSAGES:
        # Remove the oldest user/assistant pair (keep the system prompt at index 0)
        messages.pop(1)  # oldest user message
        messages.pop(1)  # corresponding assistant message


def main():
    print("CLI Chat — type /exit to quit, /reset to clear history, /history to view it")
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "/exit":
            break
        elif user_input.lower() == "/reset":
            messages.clear()
            messages.append({"role": "system", "content": SYSTEM_PROMPT})
            print("History cleared.")
            continue
        elif user_input.lower() == "/history":
            for msg in messages:
                print(f"{msg['role']}: {msg['content']}")
            continue

        messages.append({"role": "user", "content": user_input})
        trim_history()
        response = client.chat.completions.create(model=MODEL, messages=messages)
        assistant_reply = response.choices[0].message.content
        print(f"Assistant: {assistant_reply}")
        messages.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()