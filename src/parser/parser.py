from bs4 import BeautifulSoup

class WebParser:
    def __init__(
            self,
            source):
        self.parser = BeautifulSoup(source, "html.parser") 