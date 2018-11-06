import unittest

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options

from AutomationInfrastructure.Browser import Browser
from Helpers.Comment import Comment
from Helpers.Discussion import Discussion
from Helpers.Generator import Generator
from Helpers.HelperEnums import DiscussionCategory
from Helpers.TypeValidator import TypeValidator
from MvcForumApp import MvcForumApp
from PageObjects.DiscussionPage import DiscussionPage


class MvcForumTests(unittest.TestCase):

    # <editor-fold desc="TestInitialization">
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
        self.mvc_forum_app = MvcForumApp(self.browser)

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

    # </editor-fold>

    # <editor-fold desc="TestUtilities">
    def __register_new_users(self, amount_of_users):
        TypeValidator.validate_type(amount_of_users, int)
        if not amount_of_users > 0:
            raise ValueError("Amount of Users should be a number greater than 0")

        users_list = []
        for i in range(amount_of_users):
            user = Generator.generate_user()
            is_registration_done = self.mvc_forum_app.register_new_user(user)
            if is_registration_done:
                users_list.append(user)
                self.mvc_forum_app.logoff()
            else:
                raise Exception(f"User '{user.username}' registration failed!")
        return users_list

    def __create_discussion(self, category):
        magic_number = Generator.get_random_number(10)
        discussion_title = f"Discussion {magic_number}"
        tag = f"Tag - {category.name}"
        discussion_content = f'This is a new Discussion, with the Magic Number: {magic_number}'
        discussion = Discussion(discussion_title, category, tag, discussion_content)
        self.mvc_forum_app.create_new_discussion(discussion)
        return discussion

    def __is_discussion_on_main_page(self, discussion):
        main_page = self.mvc_forum_app.open_main_page()
        return main_page.is_discussion_present(discussion)

    def __take_screenshot(self, description):
        self.browser.take_screenshot(description)

    def __create_comment_for_discussion(self, discussion):
        discussion_page = self.mvc_forum_app.enter_to_discussion(discussion)
        magic_number = Generator.get_random_number(7)
        comment = Comment(f"This is a comment with Magic Number '{magic_number}' to discussion '{discussion.title}'")
        discussion_page.write_comment(comment)
        discussion_page.add_comment()
        return comment

    def __is_comment_on_discussion_page(self, comment, discussion_page):
        TypeValidator.validate_type(discussion_page, DiscussionPage)
        return discussion_page.is_comment_displayed(comment)

        # </editor-fold>

    # <editor-fold desc="Tests">
    def test_user_can_see_his_username_after_registration_logoff_and_login_again(self):
        app = self.mvc_forum_app
        users_list = self.__register_new_users(1)
        user = users_list[0]

        app.logon(user)

        username_from_menu = app.get_username_from_menu()

        self.__take_screenshot("Username is shown in the Menu")  # TODO: Make Screenshot save file
        self.assertEqual(user.username, username_from_menu,
                         f'Username "{username_from_menu}" should be "{user.username}"')

    def test_user_can_see_discussion_that_other_user_posted(self):
        app = self.mvc_forum_app
        users_list = self.__register_new_users(2)
        user1 = users_list[0]
        user2 = users_list[1]

        app.logon(user1)
        category = DiscussionCategory.Python
        discussion = self.__create_discussion(category)
        app.logoff()

        app.logon(user2)
        is_discussion_on_main_page = self.__is_discussion_on_main_page(discussion)

        assert is_discussion_on_main_page

    def test_user_can_see_vote_up_badge_of_other_user_after_voting_up(self):
        app = self.mvc_forum_app
        users_list = self.__register_new_users(2)
        user1 = users_list[0]
        user2 = users_list[1]

        app.logon(user1)
        category = DiscussionCategory.ExampleCategory
        self.__create_discussion(category)
        app.logoff()

        app.logon(user2)
        category = DiscussionCategory.Python
        discussion2 = self.__create_discussion(category)
        app.logoff()

        app.logon(user1)
        discussion_page = app.enter_to_discussion(discussion2)
        discussion_page.like_the_discussion()
        is_first_vote_up_badge = app.is_first_vote_up_badge_appeared_on_activity_tab(user2)

        assert is_first_vote_up_badge

    def test_user_can_see_comment_that_other_user_posted(self):
        app = self.mvc_forum_app
        users_list = self.__register_new_users(2)
        user1 = users_list[0]
        user2 = users_list[1]

        app.logon(user1)
        category = DiscussionCategory.Java
        discussion = self.__create_discussion(category)
        app.logoff()

        app.logon(user2)
        comment = self.__create_comment_for_discussion(discussion)
        app.logoff()

        app.logon(user1)
        discussion_page = app.enter_to_discussion(discussion)

        is_comment_on_discussion_page = self.__is_comment_on_discussion_page(comment, discussion_page)
        assert is_comment_on_discussion_page

    # </editor-fold>


if __name__ == '__main__':
    unittest.main()
