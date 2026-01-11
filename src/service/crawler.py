from src.fetcher.fetcher import WebFetcher
from src.parser.parser import WebParser
from src.model.equity import Equity

class Crawler:
    def __init__(
            self,
            url : str
            ):
        self.fetcher = WebFetcher(url)
    
    def get_equities(self, region: str) -> list[Equity]:
        all_equities = []
        self.fetcher.set_region(region)
        table_generator = self.fetcher.get_table()
        for table in table_generator:
            equities = WebParser.parse(table)
            all_equities.extend(equities)
        print(all_equities)