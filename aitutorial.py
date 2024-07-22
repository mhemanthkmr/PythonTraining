import os
import requests
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import textwrap



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def aiCalling(text):
    genai.configure(api_key="AIzaSyCElt4ZlzOIpJmMlyGLz-dVdYQ-pUuxYjg")
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(text)
    return response.text


while True:
    n = int(input("1. Chat With AI\n2. Exit\n"))
    if n == 1:
        print("Welcome To AI")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            response = aiCalling(user_input)
            print(f"AI: {response}")
    elif n == 2:
        break
    else:
        print("Invalid input.")

