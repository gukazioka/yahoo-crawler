from src.service.crawler import Crawler
import sys

if __name__ == '__main__':
    crawler = Crawler(sys.argv[1])
    crawler.get_equities('China')