# -*- coding: utf-8 -*-
# Find tables in html pages and extract it
import urllib.request as u_req
import urllib.error as u_error
import urllib.parse as u_parse
import pandas as pd
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
        if url_state(url_value):
            header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
            request = u_req.Request(url_value, headers=header)
            html = u_req.urlopen(request).read().decode("utf-8")
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
        if url_state(url_value):
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
    if url_state(url):
        page = u_req.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(page, "lxml")
        return len(soup.find_all("table", "wikitable"))
    else:
        print("URL is not valid")
    return 0


def get_number_of_table_cells(**get_urls):
    exam_data = get_html_tables(**get_urls())
    tables = exam_data.items()
    for one_table in tables:
        df = pd.DataFrame(data=one_table)
        total_rows = len(df.axes[0])
        total_cols = len(df.axes[0])
    return total_rows*total_cols

def get_number_of_rows_in_the_table(url, table_num):
    """"
    :param url url to request
    :param table_num number of table which will be rows count
    :return the number of rows in selected table or zero if table don't exists on page
    """
    header = {'User-Agent': 'Mozilla/5.0'}
    if url_state(url):
        request = u_req.Request(url, headers=header)
        html = u_req.urlopen(request).read().decode("utf-8")
        soup = BeautifulSoup(html, "lxml")
        tables = soup.find_all("table", "wikitable")
        table = tables[table_num]
        nb_rows = 0
        for tr in table.find_all("tr"):
            # print("tr_"+str(nb_rows)+" : "+str(tr))
            nb_rows += 1
        return nb_rows
    else:
        return 0

#
# def get_number_of_columns_in_the_table(url):
#     header = {'User-Agent': 'Mozilla/5.0'}
#     if url_state(url):
#         request = u_req.Request(url, headers=header)
#         html = u_req.urlopen(request).read().decode("utf-8")
#         soup = BeautifulSoup(html, "lxml")
#         tables = soup.find_all("table", "wikitable")
#         list_of_number_columns = {}
#         num_table = 1
#         for table in tables:
#             print("table_{}".format(num_table))
#             nb_cols = 0
#             first_tr = table.find("tr")
#             print("First tr : "+str(first_tr))
#             for td in table.find_all("tr>td"):
#                 print("td_"+str(nb_cols)+" : "+str(td))
#                 nb_cols += 1
#             list_of_number_columns.update({"table_" + str(num_table): nb_cols})
#             num_table += 1
#         return list_of_number_columns
#     else:
#         return 0
#
# nb = get_number_of_rows_in_the_table("https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido", 0)
# print("Le table : {}".format(nb))
