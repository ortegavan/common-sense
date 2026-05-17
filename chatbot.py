from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()

response = llm.responses.create(
    model="gpt-5.4-mini",
    temperature=0.5,
    input="Quem é a mulher mais importante da história da computação?"
)

print(response.output_text)