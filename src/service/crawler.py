import sys
from src.fetcher.fetcher import WebFetcher
from src.parser.parser import WebParser
from src.model.equity import Equity
from src.storage.writer import Writer
from src.errors.error import InvalidRegion

class Crawler:
    def __init__(
            self,
            url: str,
            writer: Writer
            ):
        self.fetcher = WebFetcher(url)
        self.writer = writer

    def get_equities(self, region: str) -> list[Equity]:
        try:
            self.fetcher.set_region(region)
            table_generator = self.fetcher.get_table()
            for table in table_generator:
                equities = WebParser.parse(source=table)
                self.writer.save_equities(equities)
        except InvalidRegion as e:
            print(e)
            sys.exit(1)
        except Exception as e:
            print(e)

