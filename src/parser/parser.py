from bs4 import BeautifulSoup, Tag
from src.model.equity import Equity

class WebParser:
    @classmethod
    def parse(cls, source : str) -> list[Equity]:
        parser = BeautifulSoup(source, "lxml")
        body = parser.find('tbody')
        rows = body.find_all('tr')
        equities = [cls.parse_row(row) for row in rows]
        return equities

    @classmethod
    def parse_row(cls, row : Tag) -> Equity:
        ticker_cell = row.select_one('[data-testid="table-cell-ticker"]')
        ticker = ticker_cell.find_all('span')[-1].get_text(strip=True)
        name_cell = row.select_one('[data-testid-cell="companyshortname.raw"]')
        name = name_cell.find('div').get_text(strip=True)
        price_cell = row.select_one('[data-testid-cell="intradayprice"]')
        price = price_cell.find('span').get_text(strip=True)
        return Equity(name, ticker, price)
