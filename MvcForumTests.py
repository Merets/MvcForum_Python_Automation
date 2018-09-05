import unittest

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options

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

        new_browser = Browser(driver, "Chrome")
        return new_browser

    def test_number1(self):
        self.assertEqual("One", self.my_tuple[0], "Check if self.widget[0] == 'One'")

    def test_number2(self):
        self.assertEqual("Two", self.my_tuple[1], "Check if self.widget[1] == 'Two'")

    @unittest.skip("demonstrating skipping")
    def test_number3(self):
        self.assertEqual("Three", self.my_tuple[2], "Check if self.widget[2] == 'Three'")

    def test_number4(self):
        self.assertEqual("Four", self.my_tuple[3], "Check if self.widget[3] == 'Four'")

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_user_can_see_his_username_after_registration_logoff_and_login_again(self):
        user = Generator.generate_user()
        print(user)

        mvc_forum_app = MvcForumApp(self.browser)
        mvc_forum_app.register_new_user(user)
        mvc_forum_app.logoff()
        mvc_forum_app.logon(user)
        username_from_menu = mvc_forum_app.get_username_from_menu()

        self.assertEqual(user.username, username_from_menu,
                         f'Username "{username_from_menu}" should be "{user.username}"')


if __name__ == '__main__':
    unittest.main()
