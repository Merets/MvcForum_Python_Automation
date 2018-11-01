from selenium.webdriver.common.by import By

from Helpers.Discussion import Discussion
from PageObjects.DiscussionPage import DiscussionPage


class MainPage(object):
    def __init__(self, browser):
        self.browser = browser

    def enter_to_discussion(self, discussion):
        discussion_rows_list = self.browser.driver.find_elements(By.CLASS_NAME, "topicrow")
        for row in discussion_rows_list:
            title_link = row.wait_for_child_element(By.CSS_SELECTOR, "h3 a")
            if title_link.text == discussion.title:
                title_link.click()
                return DiscussionPage(self.browser)

    def is_discussion_present(self, discussion):
        if not isinstance(discussion, Discussion):
            raise TypeError("Discussion should be valid for search!")

        topic_rows = self.browser.driver.find_elements(By.CLASS_NAME, "topicrow")
        for topic in topic_rows:
            h3_title = topic.wait_for_child_element(By.TAG_NAME, "h3", "h3 Title Element")
            if discussion.title in h3_title.text:
                return True
        return False


