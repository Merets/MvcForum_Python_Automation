from selenium.webdriver.common.by import By
from PageObjects.LogonPage import LogonPage
from PageObjects.MainPage import MainPage
from PageObjects.NavigationBar import NavigationBar
from PageObjects.PostsPage import PostsPage
from PageObjects.RegistrationPage import RegistrationPage


class MvcForumApp(object):
    def __init__(self, browser):
        self.browser = browser
        self.main_page = MainPage(browser=browser)

    def __open_registration_form(self):
        mvcforum_nav = self.browser.wait_for_element(By.ID, "mvcforum-nav", "mvcforum-nav div element", 10)
        register_button = mvcforum_nav.wait_for_element(By.LINK_TEXT, "Register", "Register Button", 10)
        register_button.this_element.click()
        registration_form = RegistrationPage(self.browser)
        return registration_form

    def register_new_user(self, user):
        print(f'Registering new User: "{user.username}"...')
        registration_form = self.__open_registration_form()

        registration_form.fill_input_text(registration_form.element_id_username, user.username)
        registration_form.fill_input_text(registration_form.element_id_password, user.password)
        registration_form.fill_input_text(registration_form.element_id_confirm_password, user.password)
        registration_form.fill_input_text(registration_form.element_id_email, user.email)

        registration_form.register_submit()

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
        logon_button.this_element.click()
        logon_form = LogonPage(self.browser)
        return logon_form

    def get_username_from_menu(self):
        navbar = NavigationBar(self.browser)
        username_text = navbar.get_text_from_edit_user_menu_item()
        username_text = username_text.split()[1]
        return username_text

    def take_screenshot(self, description):
        self.browser.take_screenshot(description)

    def create_new_post(self, post_string):
        print(f'Creating new post...')
        posts_page = self.__open_posts_page()
        posts_page.write_post(post_string)
        posts_page.add_post()

    def __open_posts_page(self):
        readme_button = self.browser.wait_for_element(By.CLASS_NAME, 'glyphicon-exclamation-sign', "Read Me Button")
        readme_button.this_element.click()

        posts_page = PostsPage(self.browser)
        return posts_page

    def search_for_string_on_posts_page(self, string_to_search):
        print(f'Searching for string: "{string_to_search}"...')
        posts_page = self.__open_posts_page()
        is_string_on_page = posts_page.is_string_on_posts_page(string_to_search)
        if is_string_on_page:
            print("String found.")
        return is_string_on_page
