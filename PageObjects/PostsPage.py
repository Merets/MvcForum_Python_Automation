import time

from selenium.webdriver.common.by import By


class PostsPage(object):
    def __init__(self, browser):
        self.browser = browser

    def write_post(self, post_string):
        self.browser.switch_to_iframe("PostContent_ifr")
        post_text_field = self.browser.wait_for_element(By.ID, "tinymce", "Post Text Field")
        # post_text_field.this_element.move_to_element()    #TODO: check how to make move_to_element() work in this case
        post_text_field.this_element.send_keys(post_string)
        self.browser.switch_back_to_main()

    def add_post(self):
        add_post_button = self.browser.wait_for_element(By.ID, "createpostbutton", "Add Post Button")
        add_post_button.this_element.click()

    def is_string_on_posts_page(self, string_to_search):
        if type(string_to_search) is not str:
            raise Exception("Search value should be a string!")
        all_p_elements = self.browser.container.find_elements(By.TAG_NAME, "p")
        for p in all_p_elements:
            if string_to_search in p.text:
                return True
        return False

