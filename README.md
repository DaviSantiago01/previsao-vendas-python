# 📈 Previsão de Vendas com Python

Um projeto básico de análise e previsão de vendas utilizando regressão linear, desenvolvido para demonstrar conceitos fundamentais de machine learning e visualização de dados.

## 🎯 Objetivo

Este projeto tem como objetivo:
- Analisar dados históricos de vendas
- Criar um modelo de previsão usando regressão linear
- Visualizar os resultados de forma interativa
- Demonstrar o uso de bibliotecas Python para ciência de dados

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** - Manipulação e análise de dados
- **Scikit-learn** - Machine learning (Regressão Linear)
- **Plotly Express** - Visualização interativa de dados

## 📊 Funcionalidades

- ✅ Carregamento de dados históricos de vendas
- ✅ Análise exploratória dos dados (estatísticas descritivas)
- ✅ Comparação entre diferentes períodos (Ano 1 vs Ano 2)
- ✅ Treinamento de modelo de regressão linear
- ✅ Previsão de vendas para meses futuros
- ✅ Visualização interativa com gráfico de dispersão e linha de tendência

## 📁 Estrutura do Projeto

```
previsao-vendas-python/
│
├── main.py          # Código principal do projeto
├── historico.csv    # Dados históricos de vendas
├── requirements.txt # Dependências do projeto
└── README.md       # Documentação do projeto
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/DaviSantiago01/previsao-vendas-python.git
cd previsao-vendas-python
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o projeto:
```bash
python main.py
```

## 📈 Dados

O arquivo `historico.csv` contém dados de vendas mensais com as seguintes colunas:
- **Mês**: Número do mês (1-24, representando 2 anos)
- **Vendas**: Valor das vendas no respectivo mês

## 🔍 Como Funciona

1. **Carregamento dos Dados**: O programa lê o arquivo CSV com histórico de vendas
2. **Análise Exploratória**: Exibe informações estatísticas dos dados
3. **Comparação Temporal**: Compara médias de vendas entre Ano 1 e Ano 2
4. **Modelagem**: Treina um modelo de regressão linear usando os meses como variável independente
5. **Previsão**: Gera previsões para os próximos 3 meses (25, 26, 27)
6. **Visualização**: Cria um gráfico interativo mostrando dados históricos e previsões

## 📊 Resultados

O projeto gera:
- Estatísticas descritivas dos dados
- Comparação entre períodos
- Previsões numéricas para meses futuros
- Gráfico interativo com:
  - Pontos dos dados históricos
  - Pontos das previsões
  - Linha de tendência (regressão linear)
  - Diferenciação visual entre histórico e previsões

## 🎓 Conceitos Aprendidos

- Manipulação de dados com Pandas
- Regressão linear com Scikit-learn
- Visualização de dados com Plotly
- Análise exploratória de dados
- Previsão de séries temporais básica

## 🔮 Próximos Passos

Possíveis melhorias para o projeto:
- [ ] Implementar validação cruzada
- [ ] Adicionar métricas de avaliação (R², RMSE, MAE)
- [ ] Testar outros algoritmos de machine learning
- [ ] Implementar previsões sazonais
- [ ] Adicionar interface web com Streamlit
- [ ] Incluir mais variáveis explicativas

## 👨‍💻 Autor

**Davi Santiago**
- GitHub: [@DaviSantiago01](https://github.com/DaviSantiago01)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!