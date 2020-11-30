# -*- coding: utf-8 -*-
# Find tables in html pages and extract it
import urllib.request as u_req
import urllib.error as u_error
import urllib.parse as u_parse
from bs4 import BeautifulSoup


# Return a dictionary of url.
def get_urls():
    url = """https://en.wikipedia.org/wiki/"""
    urlList = {}
    with open('wikiurls.txt', "r") as wikiurls:
        for line in wikiurls:
            # url parsing
            l = '+'.join(u_parse.quote(n) for n in line.split())
            link = url + l
            urlList.update({l: link})
    return urlList


# Return state of url: i.e if status code equals 200 he return true and false else
def __url_state(url):
    try:
        return u_req.urlopen(url).getcode() == 200
    except u_error.URLError:
        return False


def url_state(url):
    try:
        return u_req.urlopen(url).getcode() == 200
    except u_error.URLError:
        return False


# Take the dictionary of url
# test each url to verify if it's valid
# if yes, he request the content of page
# Return a tables dictionary
def get_html_tables(**urls):
    print("Extraction process...")
    tables = {}
    for url_key, url_value in urls.items():
        if __url_state(url_value):
            html = u_req.urlopen(url_value).read().decode("utf-8")
            soup = BeautifulSoup(html, "lxml")
            list_of_tables = []
            print("Extraction tables of " + url_key)
            for table in soup.find_all("table", "wikitable"):
                # fill list of tables
                list_of_tables.append(str(table))
            # update dictionary
            tables.update({url_key: list_of_tables})
            print("Tables extracted successfully")
        else:
            print("URL is not valid")
    # Return tables dictionary
    return tables


def get_number_of_tables_per_page(**urls):
    """
    Count the number of tables on each page browsed
    :param urls:
    :return: a dictionnary {page_title: nb_of_table_on_page}
    """
    nb_tables = {}
    for url_key, url_value in urls.items():
        if __url_state(url_value):
            html = u_req.urlopen(url_value).read().decode("utf-8")
            soup = BeautifulSoup(html, "lxml")
            nb_table = len(soup.find_all("table", "wikitable"))
            nb_tables.update({url_key: nb_table})
        else:
            print("URL is not valid")
    return nb_tables


def get_number_of_tables_on_page(url):
    """
    Count the number of table on the page and return it if url is valid else return 0
    :param url: url of the page
    :return int: result of count
    """
    if __url_state(url):
        page = u_req.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(page, "lxml")
        return len(soup.find_all("table", "wikitable"))
    else:
        print("URL is not valid")
    return 0
