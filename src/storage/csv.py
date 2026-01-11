import csv
from src.storage.writer import Writer
from src.model.equity import Equity

class CSVWriter(Writer):
    @classmethod
    def save_equities(cls, equities: list[Equity]):
        with open('equities.csv', newline='', mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for equity in equities:
                writer.writerow([equity.name, equity.symbol, equity.price])