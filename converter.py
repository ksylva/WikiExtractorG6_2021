# Convert the html tables to csv file format
import pandas as pd


def convert_to_csv(**tables):
    print("Converter in course...")
    # Parcours le dico
    for table_key, table_value in tables.items():
        list_of_tables = table_value # Une valeur du dico
        nb_table = 1
        # Parcours la liste de tables
        for value in list_of_tables:
            table = value # une table
            dataframe = pd.read_html(table, header=0)
            # Parcours le dataframe
            for table_df in dataframe:
                table_df.to_csv('output/'+table_key+"_"+str(nb_table)+".csv", index=False)
                nb_table = nb_table + 1 # Incrémente le nb de tables
                print("One table is converted")