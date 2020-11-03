# Run extractor and converter to provide the csv files
import htmlTablesExtractor as extractor
import converter

if __name__ == '__main__':
    urls = extractor.get_urls()
    html_tables = extractor.get_html_tables(urls)

    converter.convert_to_csv(html_tables)
