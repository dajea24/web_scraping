from bs4 import BeautifulSoup
import requests

class Web_scraping:

    def __int__(self,soup,report, url, ):

        self.html = str
        self.text = str
        self.url = str

    def get_html_from_url(self):
        response = requests.get(self.url).content
        # Parse the html content

        soup = BeautifulSoup(response, "html.parser")
        print(soup.title.get_text())
        return soup

    def get_price_from_html(self):
        prevision = self.html.find("tr", attrs={"class": "pdg-tp-0"})
        location = self.html.find("h1", attrs={"id": "wb-cont"})
        temperature = html.find("span", attrs={"class": "wxo-metric-hide"})
        report = (prevision.get_text(), location.get_text(), temperature.get_text())
        return report

    def trouver_ville_prov(loc: str):
        parts = loc.split('\n')
        return parts[0].strip()

    def cleanup_text(text: str):
        if not text:
            return text

        text = text.strip()
        return text