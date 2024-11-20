# clusterizacao.py
import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Função para coletar dados fundamentais
def get_financial_data(tickers):
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        try:
            data.append({
                'Ticker': ticker,
                'P/L': info.get('trailingPE'),
                'ROE': info.get('returnOnEquity') * 100 if info.get('returnOnEquity') else None,
                'Crescimento Receita (%)': info.get('revenueGrowth') * 100 if info.get('revenueGrowth') else None,
                'Dívida Líquida/EBITDA': info.get('debtToEquity')
            })
        except Exception as e:
            print(f"Erro ao coletar dados de {ticker}: {e}")
    return pd.DataFrame(data)

# Função principal
def main():
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'JPM', 'V', 'PG']
    
    # Coleta dos dados
    data = get_financial_data(tickers)

    # Tratamento dos dados
    data.dropna(inplace=True)
    
    # Escalonamento dos dados
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.iloc[:, 1:])

    # Clusterização com K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(scaled_data)

    # Visualização dos clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='P/L', y='ROE', hue='Cluster', data=data, palette='viridis', s=100)
    plt.title("Clusters de Ações Baseados em Características Fundamentais")
    plt.xlabel("P/L (Preço/Lucro)")
    plt.ylabel("ROE (%)")
    plt.show()

    # Avaliação do modelo
    silhouette_avg = silhouette_score(scaled_data, data['Cluster'])
    print(f"Silhouette Score: {silhouette_avg:.2f}")
    
    # Exibindo resultados
    print("Dados com Clusters:")
    print(data)

if __name__ == '__main__':
    main()
