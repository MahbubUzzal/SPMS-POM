import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelperFunc:
    __TIMEOUT = 20

    def __init__(self, driver):
        self._driver = driver
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)

    @staticmethod
    def random_str_generator(size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def wait_for_element_to_be_visible(self, by, value):
        return self._driver_wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value):
        return self._driver_wait.until(EC.element_to_be_clickable((by, value)))

    def find_element(self, by, value):
        return self._driver_wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.wait_for_element_to_be_clickable(by, value)
        element.click()
        return element

    def send_keys_to_element(self, by, value, keys):
        element = self.wait_for_element_to_be_visible(by, value)
        return element.send_keys(keys)

    def select_from_dropdown(self, dropdown_by, dropdown_value, option_by, option_value):
        self.click_element(dropdown_by, dropdown_value)  # Click the dropdown to reveal options
        self.click_element(option_by, option_value)  # Select the desired option

    def get_element_text(self, by, value):
        element = self.wait_for_element_to_be_visible(by, value)
        return element.text

    def is_entry_present_in_table(self, table_locator, entry_text):
        table = self.wait_for_element_to_be_visible(By.XPATH, table_locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            if entry_text in row.text:
                return True
        return False