import unittest

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from AutomationInfrastructure.Browser import Browser
from Helpers.Generator import Generator
from MvcForumApp import MvcForumApp


class MvcForumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print(f'Test "{self._testMethodName}" is running...')
        self.url = 'http://localhost:8080/'
        self.my_tuple = ("One", "Two", "Three", "Four")
        self.browser = self.initialize_browser()

    def tearDown(self):
        self.browser.quit()
        print(f'Test "{self._testMethodName}" finished.\n')

    def initialize_browser(self):
        chrome_options = chrome.options.Options()

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.url)
        driver.set_page_load_timeout(30)
        driver.maximize_window()

        new_browser = Browser(driver, "Chrome")

        return new_browser

    def test_user_can_see_his_username_after_registration_logoff_and_login_again(self):
        user = Generator.generate_user()

        mvc_forum_app = MvcForumApp(self.browser)
        mvc_forum_app.register_new_user(user)
        mvc_forum_app.logoff()
        mvc_forum_app.logon(user)
        username_from_menu = mvc_forum_app.get_username_from_menu()

        self.assertEqual(user.username, username_from_menu,
                         f'Username "{username_from_menu}" should be "{user.username}"')
        print("Username is displayed after Login.")
        mvc_forum_app.take_screenshot("Username is shown in the Menu")  # TODO: Make Screenshot save file

    def test_user_can_see_post_that_other_user_posted(self):
        user1 = Generator.generate_user()
        user2 = Generator.generate_user()

        mvc_forum_app = MvcForumApp(self.browser)

        mvc_forum_app.register_new_user(user1)
        mvc_forum_app.logoff()
        mvc_forum_app.register_new_user(user2)
        mvc_forum_app.logoff()

        mvc_forum_app.logon(user1)

        magic_number1 = Generator.get_random_number(10)
        post1 = f'This is a new Post, and this is the Magic Number: {magic_number1}'
        mvc_forum_app.create_new_post(post1)
        mvc_forum_app.logoff()

        mvc_forum_app.logon(user2)
        is_magic_number1_appeared_on_page = mvc_forum_app.search_for_string_on_posts_page(str(magic_number1))
        if is_magic_number1_appeared_on_page:
            mvc_forum_app.move_to_bottom_of_page()
        assert is_magic_number1_appeared_on_page


if __name__ == '__main__':
    unittest.main()
