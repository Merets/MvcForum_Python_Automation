from selenium.webdriver.common.by import By

from AutomationInfrastructure.BrowserElement import BrowserElement
from PageObjects.LogonPage import LogonPage
from PageObjects.MainPage import MainPage
from PageObjects.NavigationBar import NavigationBar
from PageObjects.RegistrationPage import RegistrationPage


class MvcForumApp(object):
    def __init__(self, browser):
        self.browser = browser
        self.main_page = MainPage(browser=browser)

    def __open_registration_form(self):
        mvcforum_nav = self.browser.wait_for_element(By.ID, "mvcforum-nav", 10, "mvcforum-nav div element")
        register_button = BrowserElement(mvcforum_nav).wait_for_element(By.LINK_TEXT, "Register", 10, "Register Button")
        register_button.click()
        registration_form = RegistrationPage(self.browser)
        return registration_form

    def register_new_user(self, user):
        registration_form = self.__open_registration_form()

        registration_form.fill_input_text(registration_form.element_id_username, user.username)
        registration_form.fill_input_text(registration_form.element_id_password, user.password)
        registration_form.fill_input_text(registration_form.element_id_confirm_password, user.password)
        registration_form.fill_input_text(registration_form.element_id_email, user.email)

        registration_form.register_submit()

    def logoff(self):
        navbar = NavigationBar(self.browser)
        navbar.logoff()

    def logon(self, user):
        logon_form = self.__open_logon_form()

        logon_form.fill_input_text(logon_form.element_id_username, user.username)
        logon_form.fill_input_text(logon_form.element_id_password, user.password)

        logon_form.logon_submit()

    def __open_logon_form(self):
        logon_button = self.browser.wait_for_element(By.CSS_SELECTOR, "#mvcforum-nav a[href*='/logon/']", 10,
                                                     "Logon Button")
        logon_button.click()
        logon_form = LogonPage(self.browser)
        return logon_form

    def get_username_from_menu(self):
        navbar = NavigationBar(self.browser)
        username_text = navbar.get_text_from_edit_user_menu_item()
        username_text = username_text.split()[1]
        return username_text
