# imports

import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from IPython.display import Markdown, display, update_display
import gradio as gr
import google.generativeai

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")


openai = OpenAI()


system_message = "You are an assistant that is great at answer what you asked"
user_prompt = "who is recep tayip erdogan"

force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

def stream_model(prompt, language):
    text = f"answer to this: {prompt}, with this language {language}"
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": text}
      ]
    stream = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result



gr.Interface(fn=stream_model, inputs=[gr.Textbox(label="Your message:", lines=6),
                                      gr.Dropdown(["EN", "TR"], label="Select language", value="EN")],
              outputs=[gr.Markdown(label="Response:")], flagging_mode="never", js= force_dark_mode).launch()