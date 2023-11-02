from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ.get('OPENAI_API_KEY'))

def generate_pet_name():
    llm = OpenAI(temperature=0.7) # max_tokens=10, top_p=1, frequency_penalty=0.5, presence_penalty=0.5)
    name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")

    return name

if __name__ == "__main__":
    print(generate_pet_name())

