
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):

    URL = "https://ya.ru/"

    SEARCH_FIELD = (
        By.CSS_SELECTOR,
        "textarea[aria-label='Запрос']"
    )

    SUGGEST = (
        By.CSS_SELECTOR,
        ".mini-suggest__popup"
    )

    def open(self):
        self.driver.get(self.URL)

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_FIELD)
        )

    def enter_search_query(self, query):
        search_field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_FIELD)
        )

        search_field.clear()
        search_field.send_keys(query)

        return search_field

    def wait_for_suggest(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUGGEST)
        )
