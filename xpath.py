#example arguments

# "https://www.castorama.pl/produkty/budowa/cementy-i-zaprawy-budowlane/tynki-elewacyjne.html" 

#"//*[@id='categoryMainContent']/div/section[1]/div/div[2]/section/section/h3/a"

"""
Usage:
python xpath.py <url> <xpath>
"""

import click
import requests
from lxml.html import fromstring


def text_preprocessing(text):
    """
    Replaces "\n" with space
    Removes spaces at the start and at the end of a string.
    """
    product_name = text.replace("\n", " ").lstrip().rstrip()
    return product_name


def dom_fromstring (url_):
    """
    Convers URL into dom.
    Requires URL as argument.
    """
    response = requests.get(url_)
    html = response.text
    dom = fromstring (html)
    return dom


def product_list (dom, xpath_):
    """
    Returns list of strings from dom based on given xpath.
    Requires dom and xpath as arguments
    """
    elements = (dom.xpath (xpath_))
    elements_content = [text_preprocessing(element.text_content()) for element in elements]
    return elements_content
    

@click.command()
@click.argument("url")
@click.argument("xpath")
def main(url, xpath):
    """
    Prints list of strings from defined xpath of a defined URL.
    Requires URL and xppath as arguments
    """
    dom = dom_fromstring (url)
    products = product_list (dom, xpath)
    for product in products:
        print (product)

if __name__ == "__main__":
    main()