from src.service.crawler import Crawler
from src.storage.csv import CSVWriter
import sys

if __name__ == '__main__':
    try:
        region = sys.argv[1]
        crawler = Crawler('https://finance.yahoo.com/research-hub/screener/equity/', CSVWriter)
        crawler.get_equities(region)
    except IndexError:
        print('Region must be informed.')