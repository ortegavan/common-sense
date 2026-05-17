from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()

assistant_message = "Pergunte-me algo." 
print(f"Assistente: {assistant_message}\n")
user_message = input("Usuário: ")
history = [
    {"role": "developer", "content": "Você é um professor, escritor e divulgador da ciência especialista em física que sempre responde de forma clara, objetiva e didática, utilizando exemplos e analogias para facilitar a compreensão dos conceitos, alguém como Marcelo Leite."},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_message}
]

while user_message != "sair":
    response = llm.responses.create(
        model="gpt-5.4-mini",
        temperature=0.5,
        input=history
    )
    
    print(f"\nAssistente: {response.output_text}")
    user_message = input("\nUsuário: ")

    history += [
        {"role": "assistant", "content": response.output_text},
        {"role": "user", "content": user_message}
    ]