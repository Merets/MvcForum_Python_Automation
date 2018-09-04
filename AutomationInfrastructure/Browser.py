from AutomationInfrastructure.ElementsContainer import ElementsContainer


class Browser(ElementsContainer):

    def __init__(self, driver, browser_name):
        ElementsContainer.__init__(self, container=driver, description=browser_name)
        self.container = driver
        self.locator_type = None
        self.locator = None

    def quit(self):
        self.container.quit()








