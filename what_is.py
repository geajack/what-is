from requests import get

from bs4 import BeautifulSoup
from nltk import sent_tokenize

def fetch_wikipedia_html(title):
    URL_TEMPLATE = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&redirects=&titles={title}"
    url = URL_TEMPLATE.format(title=title)
    api_response = get(url).json()
    pages = api_response["query"]["pages"]
    page = list(pages.values())[0]
    return page["extract"]

def strip_html(html):
    return BeautifulSoup(html, features="html.parser").get_text().strip()

def first_sentence(text):
    return sent_tokenize(text)[0]

def what_is(thing):
    return first_sentence(strip_html(fetch_wikipedia_html(thing)))

if __name__ == "__main__":
    print(what_is("charlemagne"))