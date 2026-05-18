import tiktoken

encoding_model = tiktoken.encoding_for_model("gpt-4")

with open("livro.md", "r", encoding="utf-8") as f:
    text = f.read()

# Conta os tokens
tokenized_text = encoding_model.encode(text)
num_tokens = len(tokenized_text)

print(f"Número de tokens: {num_tokens}")