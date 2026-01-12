import pytest
from src.parser.parser import WebParser
from bs4 import BeautifulSoup

@pytest.fixture
def get_parser():
    return WebParser

@pytest.fixture
def sample_html():
    return '''
        <tr>
            <td data-testid="table-cell-ticker">
                <span>ABC</span>
                <span>ABC Corp</span>
            </td>
            <td data-testid-cell="companyshortname.raw">
                <div>ABC Corporation</div>
            </td>
            <td data-testid-cell="intradayprice">
                <span>123.45</span>
            </td>
        </tr>
    '''

@pytest.mark.usefixtures("get_parser", "sample_html")
class TestParser:
    def test_parse_row(self, get_parser, sample_html):
        parser = BeautifulSoup(sample_html, "lxml")
        row = parser.find('tr')
        equity = get_parser.parse_row(row)
        assert equity.symbol == 'ABC Corp'
        assert equity.name == 'ABC Corporation'
        assert equity.price == '123.45'

    def test_parse_invalid_row(self, get_parser):
        invalid_html = '''
            <tr>
                <td data-testid="table-cell-ticker">
                    <span>XYZ</span>
                </td>
                <td data-testid-cell="companyshortname.raw">
                    <div>XYZ Inc</div>
                </td>
            </tr>
        '''
        parser = BeautifulSoup(invalid_html, "lxml")
        row = parser.find('tr')
        with pytest.raises(AttributeError):
            get_parser.parse_row(row)
