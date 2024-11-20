# Clusterização de Ações por Características Fundamentais

Este projeto visa agrupar ações com base em características fundamentais utilizando técnicas de aprendizado de máquina não supervisionado, como o K-Means.

## Objetivo

Agrupar ações com base em métricas financeiras, como:
- P/L (Preço/Lucro)
- ROE (Retorno sobre Patrimônio Líquido)
- Crescimento de Receita
- Dívida Líquida/EBITDA

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Clusterizacao-Acoes-Fundamentais.git

2. Crie e ative um ambiente virtual:

   bash
   Copiar código
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   3. Instale as dependências:
   
   bash
   Copiar código
   pip install -r requirements.txt
4. Execute o código:

   bash
   Copiar código
   python src/clusterizacao.py
