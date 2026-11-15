
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    RESULT_LINKS = (By.CSS_SELECTOR, "a.OrganicTitle-Link")

    def wait_for_results(self):
        self.wait.until(
            EC.presence_of_element_located(self.RESULT_LINKS)
        )

    def first_result_url(self):
        self.wait_for_results()

        links = self.driver.find_elements(*self.RESULT_LINKS)

        for link in links:
            url = link.get_attribute("href") or ""

            # Исключаем рекламные ссылки Яндекса
            if url and "yabs.yandex.ru/count" not in url:
                return url

        return None
