
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI
import ollama


gpt_model = "gpt-4o-mini"
claude_model = "claude-3-haiku-20240307"

gpt_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

claude_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

gpt_messages = ["Hi there"]
claude_messages = ["Hi"]
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment")
openai = OpenAI(api_key=api_key)



def call_gpt():
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, claude in zip(gpt_messages, claude_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": claude})
    completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages
    )
    return completion.choices[0].message.content

for item in range(5):
    if item == 0:
        print(gpt_messages[0])
        print(claude_messages[0])

    new_message = call_gpt()
    
    if len(claude_messages) < len(gpt_messages):

        claude_messages.append(new_message)
        print(new_message)

        continue
    gpt_messages.append(new_message)
    print('---------------')
    print(new_message)

