import selenium
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote import webelement

from AutomationInfrastructure.ElementsContainer import ElementsContainer


class BrowserElement(ElementsContainer):

    def __init__(self, element, description=""):
        ElementsContainer.__init__(self, container=element, description=description)
        self.locator_type = None
        self.locator = None
        self.this_element = element
