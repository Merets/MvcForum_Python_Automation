from AutomationInfrastructure.ElementsContainer import ElementsContainer


class BrowserElement(ElementsContainer):

    def __init__(self, element, description=""):
        ElementsContainer.__init__(self, container=element, description=description)
        self.container = element
        self.locator_type = None
        self.locator = None
