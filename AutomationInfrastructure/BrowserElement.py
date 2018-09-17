import time
from datetime import datetime

from AutomationInfrastructure.ElementsContainer import ElementsContainer
from AutomationInfrastructure.TimeConversions import TimeConversions


class BrowserElement(ElementsContainer):

    def __init__(self, element, description=""):
        ElementsContainer.__init__(self, container=element, description=description)
        self.locator_type = None
        self.locator = None
        self.this_element = element

    def wait_until_element_visible(self, timeout):
        if timeout is None:
            timeout = datetime.time(0, 0, 30)
        until_time = TimeConversions.add_time(datetime.now(), timeout)
        while datetime.now() < until_time:
            if self.this_element.is_displayed():
                return
            time.sleep(1)
        raise Exception("Exception: Element is not visible!")
