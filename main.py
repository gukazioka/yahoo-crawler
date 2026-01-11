from src.service.crawler import Crawler
from src.storage.csv import CSVWriter

if __name__ == '__main__':
    crawler = Crawler('https://finance.yahoo.com/research-hub/screener/equity/', CSVWriter)
    crawler.get_equities('China')