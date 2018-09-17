from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from AutomationInfrastructure.ElementsContainer import ElementsContainer


class Browser(ElementsContainer):

    def __init__(self, driver, browser_name):
        ElementsContainer.__init__(self, container=driver, description=browser_name)
        self.container = driver
        self.locator_type = None
        self.locator = None

    def quit(self):
        self.container.quit()

    def take_screenshot(self, description):
        description.replace(" ", "")
        self.container.save_screenshot('/Screenshots/' + description + '.png')

    def move_to_element(self, element):
        ActionChains(self.container).move_to_element(element.this_element).perform()

    def switch_to_iframe(self, iframe_id):
        WebDriverWait(self.container, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe_id))

    def switch_back_to_main(self):
        self.container.switch_to.default_content()

