import os
import openai
from openai import OpenAI
from dotenv import *

#load_dotenv()


API_KEY = os.environ.get("CHAT_API_KEY")

#SETTINGS OPEN AI KEY
openai.api_key = API_KEY
client = OpenAI(
    api_key = "PUT YOUR API KEY",
)
#connecting with chatgot api

def search_word_information(word):
    # Define your prompt or question
    prompt = f"Search information about {word}"

    # Make a request to the OpenAI API with GPT-3.5-turbo engine
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        n=1,  # Number of completions
        #stop=None,  # You can add custom stop words if needed
        temperature=0.7,  # Adjust temperature for creativity vs. accuracy
    )

    # Extract and print the generated text
    generated_text = response.choices[0].text.strip()

    return (generated_text)
#    return response["choices"][0]["message"]["content"]

search_word_information("ONITHSA")
PAGE_BG_COLOR = '#FFFFFF'
Default_prompts =[("What is ","\n Kcemma GPT" ),
                    ("What is ","\nKcemma GPT" ),
                    ("What is ","\nGoogle" ),
                    ("What is ","\n AI" )]
my_IMAGE_URL ="https://th.bing.com/th/id/OIP.TuouWODaFlPuZHkAh4mNxgHaGj?rs=1&pid=ImgDetMain"
chat_gpt ="https://th.bing.com/th/id/OIP.GLQNF_2BXTBcR8haHE9jpgAAAA?pid=ImgDet&w=170&h=170&c=7&dpr=1.5"

#print(chatgpt_response("who is peter Obi"))