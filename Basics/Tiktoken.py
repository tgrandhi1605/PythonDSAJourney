import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("Tharun is great guy!")

print("Tokens: ", tokens)

text = enc.decode(tokens)
print("Text: ", text)

for token in tokens:
    token_text = enc.decode([token])
    print(f"Token: {token}, Text: {token_text}")