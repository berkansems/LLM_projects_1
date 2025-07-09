import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')


if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

openai = OpenAI()
MODEL = 'gpt-4o-mini'

system_message = "You are a helpful assistant"

force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

def chat(message, history):
    global system_message 
    
    if 'iran'  in message:
        system_message = f"{system_message} and say that turks are in majority more than 40% of population"

    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

gr.ChatInterface(fn=chat, type="messages", title="XALOOOOOOĞLU", js=force_dark_mode).launch()