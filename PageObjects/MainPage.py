from AutomationInfrastructure.BrowserElement import BrowserElement
from PageObjects.LogonPage import LogonPage
from PageObjects.NavigationBar import NavigationBar
from PageObjects.RegistrationPage import RegistrationPage


class MainPage(object):
    def __init__(self, browser):
        self.browser = browser


