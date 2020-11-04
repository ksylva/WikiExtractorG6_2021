# Convert the html tables to csv file format
import pandas as pd
import os


def convert_to_csv(**tables):
    """
    Create an output folder if not exists,
    Browse through the dictionnary of tables which is pass him,
    get the couple (key, value) browse each value and read it with pandas librairy
    after he browse dataframe to convert his content to csv format.
    """
    # Creating of the output folder if isn't exists
    try:
        os.makedirs("output", exist_ok=True)
    except:
        if not os.path.isdir("output"):
            pass
    # End of folder creating
    print("Start convertion...")
    # browse through dictionnary
    for table_key, table_value in tables.items():
        # Value of dictionnary: it's a list of tables
        list_of_tables = table_value
        nb_table = 1
        # browse through the list
        for value in list_of_tables:
            table = value
            dataframe = pd.read_html(table, header=0)
            # browse through dataframe
            for table_df in dataframe:
                table_df.to_csv('output/' + table_key + "_" + str(nb_table) + ".csv", index=False)
                nb_table = nb_table + 1
        # print("Tables converted +: {}".format(nb_table))
