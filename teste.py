import pandas as pd
import ollama

# Carregue seu arquivo CSV em um DataFrame do pandas
df = pd.read_csv('dados.csv')

# Inicialize o cliente da API Ollama
client = ollama.Client()

# Defina uma função para consultar a API do Ollama
def query_ollama(prompt):
    response = ollama.generate(model='llama3', prompt=prompt )
    print(f'resposta função:{response}\n')
    return response.choices[0].text.strip()

# Suponha que você queira iterar sobre as linhas do DataFrame e fazer uma pergunta ao Ollama
for index, row in df.iterrows():
    prompt = f"Baseado nestes dados: {row.to_dict()}, me dê um resumo."
    response = query_ollama(prompt)
    print(f"Resposta para a linha {index}: {response}")


