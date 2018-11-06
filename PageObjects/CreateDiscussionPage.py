from selenium.webdriver.common.by import By

from Helpers.Discussion import Discussion
from Helpers.DropDownList import DropDownList
from Helpers.HelperEnums import DiscussionCategory
from Helpers.TypeValidator import TypeValidator


class CreateDiscussionPage(object):
    def __init__(self, browser):
        self.browser = browser
        self.categories = {DiscussionCategory.ExampleCategory: "Example Category",
                           DiscussionCategory.Python: "Python",
                           DiscussionCategory.CSharp: "C#",
                           DiscussionCategory.Java: "Java",
                           DiscussionCategory.DesignPatterns: "Design Patterns"}

    def create_new_discussion(self, discussion):
        self.__fill_discussion_form(discussion)
        self.__submit_discussion()

    def __fill_discussion_form(self, discussion):
        TypeValidator.validate_type(discussion, Discussion)
        title_input = self.browser.wait_for_element(By.ID, "Name", "Title Input Element")
        title_input.send_keys(discussion.title)

        category_dd_list = DropDownList(By.ID, "Category", self.categories, self.browser)
        category_dd_list.select_by_enum(DiscussionCategory, discussion.category)

        tag_input = self.browser.wait_for_element(By.ID, "Tags_tag", "Tag Input Element")
        tag_input.send_keys(discussion.tag)

        self.browser.switch_to_iframe("Content_ifr")
        text_input = self.browser.wait_for_element(By.ID, "tinymce", "Discussion Text Input Element")
        text_input.send_keys(discussion.content)
        self.browser.switch_back_to_main()

    def __submit_discussion(self):
        submit_button = self.browser.wait_for_element(By.CSS_SELECTOR, "div.submit-holder > button", "Submit Button")
        submit_button.click()
