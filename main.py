from src.service.crawler import Crawler
from src.storage.csv import CSVWriter
import sys
import os

if __name__ == '__main__':
    try:
        if os.path.exists('equities.csv'):
            os.remove('equities.csv')

        region = sys.argv[1]
        crawler = Crawler('https://finance.yahoo.com/research-hub/screener/equity/', CSVWriter)
        crawler.get_equities(region)
    except IndexError:
        print('Region must be informed.')