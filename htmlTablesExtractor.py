# -*- coding: utf-8 -*-
# Find tables in html pages and extract it
import urllib.request as u_req
import urllib.error as u_error
import urllib.parse as u_parse
import requests
import sys
from bs4 import BeautifulSoup

dict = {
    "Comparison_between_Esperanto_and_Ido": "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido",
    "Comparison_between_Esperanto_and_Interlingua": "https://en.wikipedia.org/wiki"
                                                    "/Comparison_between_Esperanto_and_Interlingua"
}


# Return a dictionnary of url.
def get_urls():
    url = """https://en.wikipedia.org/wiki/"""
    urlList = {}
    with open('wikiurls.txt', "r") as wikiurls:
        for line in wikiurls:
            # print(type(line))
            # line.encode('latin-1', 'ignore').decode('utf-8', 'ignore')
            # u_req.url
            # print(type(line))
            # l = u_parse.quote(str(line).decode("utf-8").encode("latin1"))
            l = '+'.join(u_parse.quote(n) for n in line.split())
            link = url + l
            # req = requests.get(link)
            # print(req.url)
            # print(req.encoding)
            # print(link)
            urlList.update({line: link})
    return urlList


# Return state of url: i.e if status code equals 200 he return true and false else
def __url_state(url):
    try:
        return u_req.urlopen(url).getcode() == 200
    except u_error.URLError:
        return False


# Take the dictonnary of url
# test each url to verify if it's valid
# if yes, he request the content of page
def get_html_tables(urls):
    print("Tables extraction...")
    tables = {}
    for url_key, url_value in urls.items():
        # print("URL encodee : "+url_value)
        if __url_state(url_value):
            # print("here")
            # url_encoded = u_parse.quote(url_value)
            html = u_req.urlopen(url_value).read().decode("utf-8")
            soup = BeautifulSoup(html, "lxml")
            list_of_tables = []
            print("Extraction tables of " + url_key)
            for table in soup.find_all("table", "wikitable"):
                # fill list of tables
                list_of_tables.append(str(table))
            # update dictionnary
            tables.update({url_key: list_of_tables})
            print("Extraction tables of " + url_key + " ..... OK")
    # Return tables dictionnary
    return tables


def get_number_of_tables_per_page(urls):
    nb_tables = {}
    for url_key, url_value in urls.items():
        html = u_req.urlopen(url_value).read().decode("utf-8")
        soup = BeautifulSoup(html, "lxml")
        nb_table = len(soup.find_all("table", "wikitable"))
        nb_tables.update({url_key: nb_table})

    return nb_tables


# get_number_of_tables_per_page(dict)
# get_urls()
# print(get_urls())
# print(sys.stdin.encoding)