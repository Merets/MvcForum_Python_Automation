from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementsContainer(object):

    def __init__(self, container, description):
        self.container = container
        self.description = description

    def wait_for_element(self, by, selector,  timeout=30, description=""):
        element = WebDriverWait(self.container, timeout) \
            .until(EC.presence_of_element_located((by, selector)))
        return element


