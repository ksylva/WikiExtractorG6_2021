# Convert the html tables to csv file format
import pandas

def convert_to_csv(**tables):
    for table_key, table_value in tables.items():
        list_of_tables = table_value
        for value in list_of_tables:
            table = value