"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import random

api = [
    "AIzaSyAI_JokMlA3uq4sUpYjWENVY7EKKyfgNs8",
    "AIzaSyBy0PUlN3oWDivnMn9pGqxCJolPPP2Sp0U",
    "AIzaSyCeckwAPPPJsDhIGFgE5EB9MsOlf25x3k4"
]
import google.generativeai as genai
def apiGemini(text):
  random_api = random.choice(api)
  genai.configure(api_key=random_api)
  # Set up the model
  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[
  ])

  convo.send_message(text)
  # convo.send_message("---- ขอสอบถามหน่อยค่ะ หลั่งนอกและทำไมยัง ขึ้นสองขีดค่ะ ----")
  return convo.last.text