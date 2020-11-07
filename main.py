# Run extractor and converter to provide the csv files
import htmlTablesExtractor as extractor
import converter


if __name__ == '__main__':
    urls = extractor.get_urls()
    html_tables = extractor.get_html_tables(**urls)

    converter.convert_to_csv(**html_tables)
    #
    # sum_of_tables = 0
    #
    # for value in extractor.get_number_of_tables_per_page(**urls).items():
    #     sum_of_tables += value[1]
    #
    # print("Number of tables : {}".format(sum_of_tables))
