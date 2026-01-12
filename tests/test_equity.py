from src.model.equity import Equity

class TestEquity:
    def test_create_equity(self):
        equity = Equity(
            name='TESTE',
            symbol='TST',
            price=10.1
        )

        assert equity.name == 'TESTE'
        assert equity.symbol == 'TST'
        assert equity.price == 10.1