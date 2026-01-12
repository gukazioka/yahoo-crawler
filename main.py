from src.service.crawler import Crawler
from src.storage.csv import CSVWriter
from src.logger.log import logger
import sys
import os

if __name__ == '__main__':
    if os.path.exists('equities.csv'):
        logger.info('Removing existing equities.csv file.')
        os.remove('equities.csv')

    if len(sys.argv) < 2:
        logger.error('Region must be informed.')
        sys.exit(1)

    region = sys.argv[1]
    crawler = Crawler('https://finance.yahoo.com/research-hub/screener/equity/', CSVWriter)
    crawler.get_equities(region)
