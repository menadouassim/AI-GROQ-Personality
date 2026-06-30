from groq import Groq

from dotenv import load_dotenv

import os

load_dotenv()

 

with open("exemple.txt", "r") as f:
    prompt = f.read()

with open("remarques.txt", "r") as f:
    remarques = f.read()



API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(api_key=API_KEY)

chat_completion = client.chat.completions.create(
    messages=[
        
        {
            "role": "system",
            "content": prompt ,
        },
        
        
        {
            "role": "user",
            "content": remarques,
        }
    ],

    
    model="llama-3.3-70b-versatile"
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)