from src.parser.parser import WebParser
from src.fetcher.fetcher import WebFetcher
import sys

if __name__ == '__main__':
    fetcher = WebFetcher(sys.arg[1])