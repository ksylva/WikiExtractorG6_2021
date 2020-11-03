# -*- coding: utf-8 -*-
# Find tables in html pages and extract it
import urllib.request as u_req
import urllib.error as u_error
from bs4 import BeautifulSoup

dict = {
    "Comparison_between_Esperanto_and_Ido": "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido",
    "Comparison_between_Esperanto_and_Interlingua": "https://en.wikipedia.org/wiki"
                                                    "/Comparison_between_Esperanto_and_Interlingua"
}


# Return a dictionnary of url.
def get_urls():
    url = "https://en.wikipedia.org/wiki/"
    urlList = {}
    with open("wikiurls.txt", "r") as wikiurls:
        for line in wikiurls:
            # line = line.encode("utf-8")
            link = ''.join(url + line).encode("utf-8")
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
        if __url_state(url_value):
            html = u_req.urlopen(url_value).read().decode("utf-8")
            soup = BeautifulSoup(html, "lxml")
            list_of_tables = []
            print("Extraction tables of "+url_key)
            for table in soup.find_all("table", "wikitable"):
                # fill list of tables
                list_of_tables.append(table)
            # update dictionnary
            tables.update({url_key: list_of_tables})
            print("Extraction tables of "+url_key+" ..... OK")
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
print(get_urls())