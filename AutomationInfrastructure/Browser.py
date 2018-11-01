from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from AutomationInfrastructure.WebElementExtensions import WebElementExtensions


class Browser(object):

    def __init__(self, driver, browser_name):
        self.driver = driver
        self.browser_name = browser_name
        self.initialize_web_element_class()

    def wait_for_element(self, by, selector, description="", timeout=30):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, selector)))
        element.by = by
        element.selector = selector
        element.description = description
        return element

    def quit(self):
        self.driver.quit()

    def take_screenshot(self, description):
        description = description.replace(" ", "")
        import os
        full_path = os.path.abspath('Screenshots/' + description + '.png')
        ok = self.driver.save_screenshot(full_path)
        # TODO: Save the screenshot to file
        # if not ok:
        #     raise Exception(f'failed to save screenshot to {full_path}')

    def switch_to_iframe(self, iframe_id):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_id))

    def switch_back_to_main(self):
        self.driver.switch_to.default_content()

    def initialize_web_element_class(self):
        WebElement.web_driver = self.driver
        WebElement.by = ""
        WebElement.selector = ""
        WebElement.wait_for_child_element = WebElementExtensions.wait_for_child_element
        WebElement.move_to_element = WebElementExtensions.move_to_element
        WebElement.wait_to_disappear = WebElementExtensions.wait_to_disappear

