import pandas as pd

# Criando uma tabela simples
dados = {
    "Nome": ["Ana", "João", "Carlos"],
    "Nota": [8.5, 7.2, 9.0]
}

df = pd.DataFrame(dados)

print(df)