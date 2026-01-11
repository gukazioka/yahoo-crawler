from bs4 import BeautifulSoup
from src.model.equity import Equity

class WebParser:
    @staticmethod
    def parse(source : str) -> list[Equity]:
        parser = BeautifulSoup(source, "lxml")
        body = parser.find('tbody')
        rows = body.find_all('tr')
        equities = []
        for row in rows:
            ticker_cell = row.select_one('[data-testid="table-cell-ticker"]')
            ticker = ticker_cell.find_all('span')[-1].get_text(strip=True)
            name_cell = row.select_one('[data-testid-cell="companyshortname.raw"]')
            name = name_cell.find('div').get_text(strip=True)
            price_cell = row.select_one('[data-testid-cell="intradayprice"]')
            price = price_cell.find('span').get_text(strip=True)
            equity = Equity(name, ticker, price)
            equities.append(equity)

        return equities
