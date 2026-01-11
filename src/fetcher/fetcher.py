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
        # TODO: Adicionar options necessárias para melhorar o desempenho
        options.page_load_strategy = 'eager'
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.driver.get(url)

    # ElementClickInterceptedException
    def set_region(self, region : str):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-filters-button"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-category-market_data"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-metric-region"]'))).click()
        # TODO: Verificar se mais algum está selecionado.
        eua_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'label[title="United States"] input')))
        if eua_input.is_selected():
            eua_input.click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'label[title="{region}"] input'))).click()
        # old_table = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]').get_attribute('innerHTML')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-apply"]'))).click()
        # self.wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]').get_attribute('innerHTML') != old_table)
        # table = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]')

    def get_table(self):
        yield self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]').get_attribute('innerHTML')

        next_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="next-page-button"]')
        while next_button.is_enabled():
            old_table = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]').get_attribute('innerHTML')
            next_button.click()
            self.wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]').get_attribute('innerHTML') != old_table)
            table = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]')
            yield table.get_attribute('innerHTML')