from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Helpers.TypeValidator import TypeValidator


class WebElementExtensions(object):
    def move_to_element(self):
        ActionChains(self.web_driver).move_to_element(self).perform()

    def wait_for_child_element(self, by, selector, description="", timeout=30):
        TypeValidator.validate_type(by, str)
        TypeValidator.validate_type(selector, str)
        TypeValidator.validate_type(description, str)
        TypeValidator.validate_type(timeout, int)
        element = WebDriverWait(self, timeout).until(EC.presence_of_element_located((by, selector)))
        element.by = by
        element.selector = selector
        element.description = description
        return element

    def wait_to_disappear(self, appear_timeout=5, disappear_timeout=30):
        TypeValidator.validate_type(appear_timeout, int)
        TypeValidator.validate_type(disappear_timeout, int)
        try:
            WebDriverWait(self.web_driver, appear_timeout).until(
                EC.presence_of_element_located((self.by, self.selector)))
        except TimeoutException:
            print("Warning: The Element is not present! No need to wait to disappear.")
            return

        try:
            WebDriverWait(self.web_driver, disappear_timeout).until_not(
                EC.visibility_of_element_located((self.by, self.selector)))
        except TimeoutException:
            print(f"Timeout Exception: The Element was not disappeared after {disappear_timeout} seconds")
            raise
