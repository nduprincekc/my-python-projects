import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.environ.get("CHAT_API_KEY")

# Set OpenAI API key
openai.api_key = API_KEY

# Define function to get ChatGPT response
def chatgpt_response(content):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=content,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

PAGE_BG_COLOR = '#FFFFFF'
Default_prompts = [
    ("What is ", "\n Kcemma GPT"),
    ("What is ", "\nKcemma GPT"),
    ("What is ", "\nGoogle"),
    ("What is ", "\n AI")
]
my_IMAGE_URL = "https://th.bing.com/th/id/OIP.TuouWODaFlPuZHkAh4mNxgHaGj?rs=1&pid=ImgDetMain"
chat_gpt = "https://th.bing.com/th/id/OIP.GLQNF_2BXTBcR8haHE9jpgAAAA?pid=ImgDet&w=170&h=170&c=7&dpr=1.5"

# Print ChatGPT response
print(chatgpt_response("who is peter"))
