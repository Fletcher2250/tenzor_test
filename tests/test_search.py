
from selenium.webdriver.common.keys import Keys

from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


def test_search_tensor_is_first_result(driver):
    page = MainPage(driver)
    page.open()

    search_field = page.enter_search_query("Тензор")

    assert search_field.get_attribute("value") == "Тензор"

    page.wait_for_suggest()
    search_field.send_keys(Keys.ENTER)

    results_page = SearchResultsPage(driver)
    first_url = results_page.first_result_url()

    assert first_url is not None, "Результаты поиска не найдены"

    assert "tensor.ru" in first_url, (
        f"Первый результат ведёт не на tensor.ru: {first_url}"
    )
