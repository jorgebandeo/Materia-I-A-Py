import pandas as pd
import matplotlib.pyplot as plt

# Criando algumas variáveis fictícias para testar o código
datas = ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01']
precos = [50, 55, 53, 60, 62, 65, 70, 75, 80, 85]

# Criando um DataFrame com as variáveis fictícias
df = pd.DataFrame({'data': datas, 'preco': precos})

# Converte a coluna de datas para formato datetime
df['data'] = pd.to_datetime(df['data'])

# Define a coluna de datas como o índice do DataFrame
df.set_index('data', inplace=True)

# Plota o gráfico de linhas com a tendência de preços da ação
df['preco'].plot(figsize=(12,8))

# Adiciona um título ao gráfico
plt.title('Tendência de preços da ação')

# Adiciona um rótulo para o eixo x
plt.xlabel('Ano')

# Adiciona um rótulo para o eixo y
plt.ylabel('Preço')

# Exibe o gráfico
plt.show()