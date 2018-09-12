from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait

from AutomationInfrastructure.ElementsContainer import ElementsContainer


class BrowserElement(ElementsContainer):

    def __init__(self, element, description=""):
        ElementsContainer.__init__(self, container=element, description=description)
        # self.container = element
        self.locator_type = None
        self.locator = None
        self.this_element = element

    # def wait_to_disappear(self):
    #     self.this_element
    #     # element = WebDriverWait(self.container, 10).until(lambda x: x.find_element_by_id("someId"))
    #     is_disappeared = WebDriverWait(self.container, 5, 1, ElementNotVisibleException)\
    #         .until_not(lambda x: x.find_element_by_id("someId").is_displayed())
    #     return is_disappeared
