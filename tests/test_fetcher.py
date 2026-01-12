import pytest
from src.fetcher.fetcher import WebFetcher
from src.errors.error import InvalidRegion

@pytest.fixture
def fetcher() -> WebFetcher:
    return WebFetcher('https://finance.yahoo.com/research-hub/screener/equity/')

@pytest.mark.usefixtures("fetcher")
class TestFetcher:
    def test_fetch_invalid_region(self, fetcher):
        with pytest.raises(InvalidRegion):
            fetcher.set_region('Invalid')
