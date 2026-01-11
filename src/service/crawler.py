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
            all_equities = []
            self.fetcher.set_region(region)
            table_generator = self.fetcher.get_table()
            for table in table_generator:
                equities = WebParser.parse(table)
                all_equities.extend(equities)
            self.writer.save_equities(all_equities)
        except InvalidRegion as e:
            print(e)

