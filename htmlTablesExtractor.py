# -*- coding: utf-8 -*-
# Find tables in html pages in extract it
import urllib.request
from bs4 import BeautifulSoup
import csv


# Return a dictionnary of url.
def get_urls():
    url = "https://en.wikipedia.org/wiki/"
    urlList = {}
    with open("wikiurls.txt", "r") as wikiurls:
        for line in wikiurls:
            link = url + line
            urlList.update({line: link})
    return urlList
