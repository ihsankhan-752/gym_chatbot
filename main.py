from openai import RateLimitError, APIConnectionError
from gemini import get_response
from config import system_prompt


def main():
    messages = [{"role": "system", "content": system_prompt}]

    while True:
        user_prompt = input("You: ")
        if user_prompt == "quit":
            break
        if not user_prompt.strip():
            continue

        messages.append({"role": "user", "content": user_prompt})

        try:
            reply = get_response(messages=messages)
        except RateLimitError:
            print("Limit reached. Wait a minute and try again.")
            messages.pop()
            continue
        except APIConnectionError:
            print("Can't reach the server. Check your internet and try again.")
            messages.pop()
            continue
        except Exception as e:
            print(f"Something went wrong: {e}")
            messages.pop()
            continue

        messages.append({"role": "assistant", "content": reply})
        print(reply)


if __name__ == "__main__":
    main()