# -*- coding: utf-8 -*-
# Convert the html tables to csv file format
import pandas as pd
import os


def convert_to_csv(**tables):
    """
    Create an output folder if not exists,
    Browse through the dictionary of tables which is pass him,
    get the couple (key, value) browse each value and read it with pandas library
    after he browse dataframe to convert his content to csv format.
    """
    # Creating of the output folder if isn't exists
    try:
        os.makedirs("output", exist_ok=True)
    except:
        if not os.path.isdir("output"):
            pass
    # End of folder creating
    print("Conversion process...")
    nb_total_table_convert = 0
    # browse through dictionary
    for table_key, table_value in tables.items():
        # Value of dictionary: it's a list of tables
        print("Begin conversion of tables of page {}".format(table_key))
        list_of_tables = table_value
        nb_of_csv_file_on_same_page = 0
        nb_tables_on_page = 0
        # browse through the list
        for table in list_of_tables:
            print("Le tableau est : {}".format(table))
            dataframe = pd.read_html(table, header=0)
            # browse through dataframe
            for table_df in dataframe:
                nb_of_csv_file_on_same_page += 1
                table_df.to_csv('output/' + table_key + "_" + str(nb_of_csv_file_on_same_page) + ".csv", index=False)

            nb_tables_on_page += 1
        print("All tables of {} has been converted".format(table_key))
        nb_total_table_convert += nb_tables_on_page

    # print("{} CSV files has been created".format(nb_total_table_convert))
