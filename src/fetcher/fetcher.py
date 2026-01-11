from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebFetcher:

    def __init__(
        self,
        url : str
    ):
        options = webdriver.ChromeOptions()
        # TODO: Adicionar options necessárias para melhorar o desempenho
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.1)
        self.driver.get(url)

    # ElementClickInterceptedException
    def set_region(self, region : str):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-filters-button"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-category-market_data"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-metric-region"]'))).click()
        # TODO: Verificar se mais algum está selecionado.
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'label[title="United States"] input')))
        eua_input = self.driver.find_element(By.CSS_SELECTOR, f'label[title="United States"] input')
        if eua_input.is_selected():
            eua_input.click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'label[title="{region}"] input'))).click()
        updated = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="table-cell-ticker"]').get_attribute('innerHTML')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="filter-apply"]'))).click()
        self.wait.until(lambda e : e.find_element(By.CSS_SELECTOR, '[data-testid="table-cell-ticker"]').get_attribute('innerHTML') != updated)

    def get_table(self):
        table = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]')
        yield table.get_attribute('innerHTML')

        next_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="next-page-button"]')
        while next_button.is_enabled():
            updated = table.find_element(By.CSS_SELECTOR, '[data-testid="table-cell-ticker"]').get_attribute('innerHTML')
            next_button.click()
            start = time.perf_counter()
            self.wait.until(lambda e : e.find_element(By.CSS_SELECTOR, '[data-testid="table-cell-ticker"]').get_attribute('innerHTML') != updated)
            end = time.perf_counter()
            print(f'demorou {end - start:.8f}')
            table = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="screener-table"]')
            yield table.get_attribute('innerHTML')