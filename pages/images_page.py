from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class ImagesPage(BasePage):

    URL = "https://yandex.ru/images/search?text=кот"

    def open(self):
        self.driver.get(self.URL)

        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        self.wait.until(
            lambda driver: len(
                driver.find_elements(By.TAG_NAME, "img")
            ) > 0
        )

    def open_first_image(self):
        self.wait.until(
            lambda driver: driver.execute_script("""
                return Array.from(document.images).some(img =>
                    img.complete &&
                    img.naturalWidth > 200 &&
                    img.offsetWidth > 150 &&
                    !img.className.includes('PopularRequestList-Thumb')
                );
            """)
        )

        self.driver.execute_script("""
            const images = Array.from(document.images);

            const image = images.find(img =>
                img.complete &&
                img.naturalWidth > 200 &&
                img.offsetWidth > 150 &&
                !img.className.includes('PopularRequestList-Thumb')
            );

            if (!image) {
                throw new Error('Изображение не найдено');
            }

            const clickable = image.closest(
                'a, button, [role="button"]'
            ) || image.parentElement;

            clickable.click();
        """)

        self.wait.until(
            lambda driver: driver.execute_script("""
                return document.querySelectorAll(
                    '[role="dialog"], .MMViewer, .MediaViewer'
                ).length > 0;
            """)
        )

    def get_current_image(self):
        return self.wait.until(
            lambda driver: self._get_viewer_image(driver)
        )

    @staticmethod
    def _get_viewer_image(driver):
        return driver.execute_script("""
            const dialog = document.querySelector(
                '[role="dialog"], .MMViewer, .MediaViewer'
            );

            if (!dialog) return null;

            const images = Array.from(dialog.querySelectorAll('img'));

            const visible = images.filter(img =>
                img.complete &&
                img.naturalWidth > 200 &&
                img.offsetWidth > 200
            );

            if (!visible.length) return null;

            return visible.sort(
                (a, b) =>
                    b.getBoundingClientRect().width *
                    b.getBoundingClientRect().height -
                    a.getBoundingClientRect().width *
                    a.getBoundingClientRect().height
            )[0].src;
        """)

    def next_image(self):
        old_image = self.get_current_image()

        self.driver.find_element(
            By.TAG_NAME, "body"
        ).send_keys(Keys.ARROW_RIGHT)

        self.wait.until(
            lambda driver: (
                self._get_viewer_image(driver) is not None
                and self._get_viewer_image(driver) != old_image
            )
        )

        return self.get_current_image()

    def previous_image(self):
        old_image = self.get_current_image()

        self.driver.find_element(
            By.TAG_NAME, "body"
        ).send_keys(Keys.ARROW_LEFT)

        self.wait.until(
            lambda driver: (
                self._get_viewer_image(driver) is not None
                and self._get_viewer_image(driver) != old_image
            )
        )

        return self.get_current_image()