import pandas as pd
import matplotlib.pyplot as plt
# Carregando o arquivo CSV em um DataFrame de varias empresas com suas açoes a cada mes
df = pd.read_csv('Trabalho M2/archive/sp500_prices.csv')

# Recoleta as variaveis de cada ano
Companias = df["Company"].unique()
anos = df["Year"].unique()

# filtra as 10 peimiras empresas 
Sdc = df[df["Company"] == Companias[0]]
for i in Companias[1:10]:# filtro das 10 primeiras empresas
    Sdc = pd.concat([Sdc, df[df["Company"] == i]], ignore_index=True)

for J in Companias[0:1]:
    for i in anos: # filtro por ano para cada ano 1 

        # cria uma nova tavela de dados referene ao ano
        l = Sdc[Sdc["Company"] == J]
        Y = l[Sdc["Year"] == i]
        Y = Y[["Company","Open","High",	"Low","Close","Volume","Dividends",	"Year","Month"]]
        y = [ 200, 150]
        Y.to_csv(J+str(i), index=False)
        plt.title(J+str(i))

        # ralizamo uma diferença dinamica entre a abertura e o fechamento
        vetor = []
        vetor2 = []
        aux = Y["Close"].index[0]
        for i in range(Y["Close"].shape[0]):
            vetor.append([Y["Close"][i+aux],Y["Open"][i+aux] ])
            
        a = [i[0] if i[0]>i[1] else i[1] for i in vetor]
        b = [i[0] if i[0]<i[1] else i[1] for i in vetor]
        y = [ 200, 150]
        plt.ylim(min(b)-10, max(a)+10)

        plt.bar(Y["Month"], Y["High"], color="red",label=i,width=.1)
        plt.bar(Y["Month"],Y["Low"] , color="red",label=i,width=.1)

        # imprime a barra maior 
        plt.bar(Y["Month"], a ,label=i,width=.5)
        #impriem a barra menor para borrar a maior
        plt.bar(Y["Month"],b , color="w",label=i,width=.5)
        plt.bar(Y["Month"], b, color="red",label=i,width=.1)
        plt.bar(Y["Month"],Y["Low"] , color="w",label=i,width=.1)
        
        #imprime o grafico de analise de tendencia do ano 
        plt.show()
        

#  fitra pelo ano de 2022
xgroupby= Sdc.groupby("Company")["Volume"].sum()
plt.bar(Companias[0:10],xgroupby,color = 'r')
data = Sdc[Sdc["Year"] == anos.max()-1]

# filtra coliunas
novo = data[["Company","Open","High",	"Low","Close","Volume","Dividends",	"Year"]]

# soma do volume de cada compania no ano de 2022
ngroupby= novo.groupby("Company")["Volume"].sum()
plt.title("Fluxo do volume no primerio ano e no acumulo dos anos ate 2023")
plt.bar(Companias[0:10],ngroupby)
plt.show()
