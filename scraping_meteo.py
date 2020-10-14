import requests
from bs4 import BeautifulSoup
#import collections



def main():
    print_header()
    #code = input('Indiquer votre code postal pour avoir la mÃ©tÃ©o (H4N1L4)? ')
    code="H1kXC"
    html = get_html_from_url( )
    report = get_meteo_from_html(html)

    print('Condition mÃ©tÃ©o: {} \n Location:{} \n Temperature:{}'.format(
        report[0] ,report[1], report[2]
    ))


def print_header():
    print('---------------------------------')
    print('           METEO TOTO')
    print('---------------------------------')
    print()


def get_html_from_url():
    url="https://meteo.gc.ca/city/pages/qc-147_metric_f.html"
    response = requests.get(url).content
    # Parse the html content

    soup =  BeautifulSoup(response, "html.parser")
    print(soup.title.get_text())
    return soup



def get_meteo_from_html(html):
    prevision = html.find("tr",attrs={"class": "pdg-tp-0"})
    location= html.find("h1",attrs={"id": "wb-cont"})
    temperature = html.find("span",attrs={"class": "wxo-metric-hide"})
    report = (prevision.get_text(),location.get_text(), temperature.get_text())
    return report


def trouver_ville_prov(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()