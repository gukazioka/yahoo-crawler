import sys
from src.fetcher.fetcher import WebFetcher
from src.parser.parser import WebParser
from src.model.equity import Equity
from src.storage.writer import Writer
from src.errors.error import InvalidRegion
from src.logger.log import logger

class Crawler:
    def __init__(
            self,
            url: str,
            writer: Writer
            ):
        """
        Initialize the Crawler.

        :param url: URL to fetch equities.
        :type url: str
        :param writer: Storage provider
        :type writer: Writer
        """
        self.fetcher = WebFetcher(url)
        self.writer = writer

    def get_equities(self, region: str):
        """
        Get equities and saves them using the provided writer.

        :param region: Filter region for equities.
        :type region: str
        """
        try:
            self.fetcher.set_region(region)
            table_generator = self.fetcher.get_table()
            for table in table_generator:
                equities = WebParser.parse(source=table)
                self.writer.save_equities(equities)
            logger.info('Equities fetched successfully.')
        except InvalidRegion as e:
            logger.error(e)
            sys.exit(1)
        except Exception as e:
            logger.error('Error while fetching equities')
            sys.exit(1)

