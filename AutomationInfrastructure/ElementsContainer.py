from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementsContainer(object):

    def __init__(self, container, description):
        self.container = container
        self.description = description

    def wait_for_element(self, by, selector, description="", timeout=30):
        element = WebDriverWait(self.container, timeout).until(EC.presence_of_element_located((by, selector)))
        element.description = description

        from AutomationInfrastructure.BrowserElement import BrowserElement

        browser_element = BrowserElement(element)
        return browser_element

    def wait_to_disappear(self, by, selector, appear_timeout=5, disappear_timeout=30):
        try:
            WebDriverWait(self.container, appear_timeout).until(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            print("Warning: The Element is not present! No need to wait to disappear.")
            return

        try:
            WebDriverWait(self.container, disappear_timeout).until_not(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            print("Timeout Exception")
            raise
