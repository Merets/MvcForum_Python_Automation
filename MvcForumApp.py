from selenium.webdriver.common.by import By

from PageObjects.ActivityPage import ActivityPage
from PageObjects.CreateDiscussionPage import CreateDiscussionPage
from PageObjects.LogonPage import LogonPage
from PageObjects.MainPage import MainPage
from PageObjects.NavigationBar import NavigationBar
from PageObjects.RegistrationPage import RegistrationPage


class MvcForumApp(object):
    def __init__(self, browser):
        self.browser = browser
        self.main_page = MainPage(browser=browser)
        self.user1 = None
        self.user2 = None
        self.magic_number1 = None
        self.discussion_title = None

    def __open_registration_form(self):
        print(f'Opening Registration Form...')
        mvcforum_nav = self.browser.wait_for_element(By.ID, "mvcforum-nav", "mvcforum-nav div element", 10)
        register_button = mvcforum_nav.wait_for_child_element(By.LINK_TEXT, "Register", "Register Button", 10)
        register_button.click()
        return RegistrationPage(self.browser)

    def __open_activity_tab(self):
        print(f'Opening Activity Tab...')
        content_strip = self.browser.wait_for_element(By.CLASS_NAME, "content-strip", "content-strip Main Menu")
        activity_link = content_strip.wait_for_child_element(By.LINK_TEXT, "Activity", "Activity link")
        activity_link.click()
        return ActivityPage(self.browser)

    def register_new_user(self, user):
        print(f'Registering new User: "{user.username}"...')
        registration_form = self.__open_registration_form()

        registration_form.fill_input_text(registration_form.element_id_username, user.username)
        registration_form.fill_input_text(registration_form.element_id_password, user.password)
        registration_form.fill_input_text(registration_form.element_id_confirm_password, user.password)
        registration_form.fill_input_text(registration_form.element_id_email, user.email)

        registration_form.register_submit()
        return True

    def logoff(self):
        print(f'Logging off...')
        navbar = NavigationBar(self.browser)
        navbar.logoff()

    def logon(self, user):
        print(f'Logging on User: {user.username}...')
        logon_form = self.__open_logon_form()

        logon_form.fill_input_text(logon_form.element_id_username, user.username)
        logon_form.fill_input_text(logon_form.element_id_password, user.password)

        logon_form.logon_submit()

    def __open_logon_form(self):
        logon_button = self.browser.wait_for_element(By.CSS_SELECTOR, "#mvcforum-nav a[href*='/logon/']",
                                                     "Logon Button", 10)
        logon_button.click()
        return LogonPage(self.browser)

    def get_username_from_menu(self):
        navbar = NavigationBar(self.browser)
        username_text = navbar.get_text_from_edit_user_menu_item()
        username_text = username_text.split()[1]
        return username_text

    def __open_new_discussion_page(self):
        create_discussion_button = self.browser.wait_for_element(By.CLASS_NAME, "createtopicbutton",
                                                                 "Create New Post Button")
        create_discussion_button.click()
        return CreateDiscussionPage(self.browser)

    def create_new_discussion(self, discussion):
        print(f'Creating new discussion...')
        create_discussion_page = self.__open_new_discussion_page()
        create_discussion_page.create_new_discussion(discussion)

    def is_first_vote_up_badge_appeared_on_activity_tab(self, user):
        activity_tab = self.__open_activity_tab()
        is_badge_on_page = activity_tab.search_for_first_vote_up_badge(user)
        return is_badge_on_page

    def open_main_page(self):
        navbar = self.browser.wait_for_element(By.CLASS_NAME, "navbar-brand", "NavBar Main Button")
        navbar.click()
        return MainPage(self.browser)

    def enter_to_discussion(self, discussion):
        print(f'Entering to discussion...')
        main_page = self.open_main_page()
        discussion_page = main_page.enter_to_discussion(discussion)
        return discussion_page
