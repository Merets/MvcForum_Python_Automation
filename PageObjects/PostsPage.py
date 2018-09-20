import time

from selenium.webdriver.common.by import By


class PostsPage(object):
    def __init__(self, browser):
        self.browser = browser

    def write_post(self, post_string):
        self.browser.switch_to_iframe("PostContent_ifr")
        post_text_field = self.browser.wait_for_element(By.ID, "tinymce", "Post Text Field")
        post_text_field.move_to_element()
        post_text_field.send_keys(post_string)
        self.browser.switch_back_to_main()

    def add_post(self):
        add_post_button = self.browser.wait_for_element(By.ID, "createpostbutton", "Add Post Button")
        add_post_button.click()

    def is_string_on_posts_page(self, string_to_search):
        if type(string_to_search) is not str:
            raise Exception("Search value should be a string!")
        all_p_elements = self.browser.driver.find_elements(By.TAG_NAME, "p")
        for p in all_p_elements:
            if string_to_search in p.text:
                return True
        return False

