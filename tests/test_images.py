from pages.images_page import ImagesPage


def test_yandex_images_navigation(driver):
    page = ImagesPage(driver)

    page.open()
    page.open_first_image()

    original_image = page.get_current_image()
    assert original_image, "Изображение не загрузилось"

    next_image = page.next_image()

    assert next_image != original_image, (
        "Следующее изображение не изменилось"
    )

    previous_image = page.previous_image()

    assert previous_image == original_image, (
        "Не удалось вернуться к исходному изображению"
    )