import requests
from bs4 import BeautifulSoup


# Convert URL website to html

def url_to_html(url: str):
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url, headers=headers)
    html = response.text
    return html


# Parse the html content to Soup object
def html_soup(html: str):
    soup = BeautifulSoup(html, "html.parser")
    return soup


def main():
    url = ["https://www.walmart.ca/fr", "https://www.homedepot.ca/fr/accueil.html"]

    html = [url_to_html(url[k]) for k in range(0, len(url))]
    soup = [html_soup(html[k]) for k in range(0, len(url))]


    print(type(html))
    print(type(soup[0]))


if __name__ == '__main__':
    main()
