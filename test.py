from src.assignment2 import CryptocurrencyParser

cryptoBitcoin = CryptocurrencyParser()
listOfArticles = cryptoBitcoin.getArticles("bitcoin")
cryptoBitcoin.articlesTag(listOfArticles)