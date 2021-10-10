# Ass2Python

## Installation
1. clone this
1. install requirements `pip install -r requirements.txt`

## Usage
```python
from src.assignment2 import CryptocurrencyParser
cryptoBitcoin = CryptocurrencyParser()
listOfArticles = cryptoBitcoin.getArticles("bitcoin")
cryptoBitcoin.articlesTag(listOfArticles)
```

## Examples
```python
cryptoBitcoin.getArticles("bitcoin")
cryptoEth.getArticles("ethereum")
"""
Bitcoin price today, BTC to USD live, marketcap and chart
CoinMarketCap: Cryptocurrency Prices, Charts And Market ...
Bitcoin (BTC) Цена, Графики, Рыночная капитализация
Bitcoin Cash price today, BCH to USD live, marketcap and chart
Global Cryptocurrency Market Charts | CoinMarketCap
All Cryptocurrencies | CoinMarketCap
Bitcoin Price (BTC) - CoinMarketCap
Bitcoin SV price today, BSV to USD live, marketcap and chart
Bitcoin Analytics and Statistics | CoinMarketCap
Bitcoin Gold price today, BTG to USD live, marketcap and chart


Ethereum price today, ETH to USD live, marketcap and chart
Ethereum (ETH) Цена, Графики, Рыночная капитализация
CoinMarketCap: Cryptocurrency Prices, Charts And Market ...
Ethereum Classic price today, ETC to USD live, marketcap and chart
Ethereum (ETH) Fiyatı, Grafikler, Piyasa Değeri | CoinMarketCap
Ethereum Price (ETH) - CoinMarketCap
Harga Ethereum (ETH), grafik, kap pasar, dan metrik lainnya
Ethereum (ETH) prezzo, grafici, capitalizzazione di mercato e altre ...
Top Ethereum Tokens by Market Capitalization | CoinMarketCap
Global Cryptocurrency Market Charts | CoinMarketCap
"""
```

## License
MIT