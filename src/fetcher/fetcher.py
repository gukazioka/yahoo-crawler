from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class WebFetcher:

    def __init__(
        self,
        url : str
    ):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, timeout=2)
        self.driver.get(url)
        self.fetch("China")

    def fetch(self, region : str):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-filters-button"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-category-market_data"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-metric-region"]'))).click()
        eua_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'label[title="United States"] input')))
        if eua_input.is_selected():
            eua_input.click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'label[title="{region}"] input'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-apply"]'))).click()
        table_div = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]')
        table = table_div.find_element(By.CSS_SELECTOR, "table")