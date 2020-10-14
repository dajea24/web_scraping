import requests
from bs4 import BeautifulSoup

def print_header():
    print('--------------------------------------------------------------')
    print('           Price - Walmart - HomeDepot - BestBuy')
    print('--------------------------------------------------------------')
    print()


def get_html_from_url(url):

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    response = requests.get(url, headers=headers)

    # Parse the html content
    soup = BeautifulSoup(response)
    print(soup.title.get_text())
    return soup


def get_price_from_html(html):
    prevision = html.find("tr", attrs={"class": "pdg-tp-0"})
    location = html.find("h1", attrs={"id": "wb-cont"})
    temperature = html.find("span", attrs={"class": "wxo-metric-hide"})
    report = (prevision.get_text(), location.get_text(), temperature.get_text())
    return report


def main():
    print_header()

    # Sites web à scraper

    #url = ["https://www.homedepot.ca/fr/accueil.html",
           #"https://www.bestbuy.ca/fr-ca",
           #"https://www.walmart.ca/fr"]

    url = "https://www.homedepot.ca/fr/accueil.html"

    html = get_html_from_url(url)
            #get_html_from_url(url[1]),
            #get_html_from_url(url[2])]

    #report = [get_price_from_html(html[0]),
              #get_price_from_html(html[1]),
              #get_price_from_html(html[2])]

    #print('Condition météo: {} \n Location:{} \n Temperature:{}'.format(
        #report[0], report[1], report[2]
    #))

if __name__ == '__main__':
    main()

