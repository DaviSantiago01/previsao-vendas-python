import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression 

# 1. Carregar os dados históricos de vendas
tabela_historico = pd.read_csv("historico.csv")

#Testando fucnaide divner para ver infroçaos  da tabe com int flao, ver descriça~co medio, max, min, etc
print(tabela_historico.info())
print(tabela_historico.describe())
print(tabela_historico.head(5))
print(tabela_historico.tail(5))

# Comparando Ano 1 (meses 1-12) com Ano 2 (meses 13-24)
ano1 = tabela_historico[tabela_historico["Mês"] <= 12]
ano2 = tabela_historico[tabela_historico["Mês"] > 12]
print("Média de vendas Ano 1:", ano1["Vendas"].mean())
print("Média de vendas Ano 2:", ano2["Vendas"].mean())

# 2. Definir variáveis
y = tabela_historico["Vendas"]          # O que quero prever (variável dependente)
x = tabela_historico[["Mês"]]           # Dados que vou usar para prever (variável independente)

# 3. Criar e treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(x, y)

# 4. Criar novos meses para prever
meses_prever = pd.DataFrame({"Mês": [25, 26, 27]})
previsoes = modelo.predict(meses_prever)

# 5. Construir tabela com previsões
tabela_previsoes = pd.DataFrame({
    "Mês": [25, 26, 27],
    "Vendas": previsoes
})

# 6. Adicionar coluna para identificar histórico vs previsões
tabela_historico["Tipo"] = "Histórico"
tabela_previsoes["Tipo"] = "Previsão"

# 7. Concatenar os dois dataframes
tabela_final = pd.concat([tabela_historico, tabela_previsoes])

# 8. Criar gráfico interativo
grafico = px.scatter(
    tabela_final, 
    x="Mês", 
    y="Vendas", 
    color="Tipo", 
    trendline="ols",
    title="Previsão de Vendas"
)
grafico.show()