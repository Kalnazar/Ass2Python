import requests
from bs4 import BeautifulSoup as bs


class CryptocurrencyParser():

    def getArticles(self, cryptocurrency):
        link = requests.get("https://www.google.com/search?q=site:coinmarketcap.com+" + cryptocurrency)
        soup = bs(link.content, 'html.parser')
        result = soup.find_all("h3")
        return result

    def articlesTag(self, listOfArticles): # this method just to output the information
        for tag in listOfArticles:
            print(tag.find("div").get_text())


if __name__ == '__main__':
    # 1st object, in this object we have live information about cryptocurrency Bitcoin(BTC)
    cryptoBitcoin = CryptocurrencyParser()
    listOfArticles = cryptoBitcoin.getArticles("bitcoin")
    cryptoBitcoin.articlesTag(listOfArticles)

    print("\n") # just line feed

    #2nd object, in this object we have live information about cryptocurrency Ethereum(ETH)
    cryptoEth = CryptocurrencyParser()
    listOfArticles = cryptoEth.getArticles("ethereum")
    cryptoEth.articlesTag(listOfArticles)

    # Yes, we can also get information about other cryptocurrencies