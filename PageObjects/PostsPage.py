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

    def __is_string_on_posts_page(self, string_to_search):
        if type(string_to_search) is not str:
            raise Exception("Search value should be a string!")
        all_p_elements = self.browser.driver.find_elements(By.TAG_NAME, "p")
        for p in all_p_elements:
            if string_to_search in p.text:
                return True
        return False

    def __is_show_more_posts_visible(self):
        show_more_posts_link = self.__get_more_posts_link_element()
        return show_more_posts_link.is_displayed()

    def __show_more_posts(self):
        show_more_posts_link = self.__get_more_posts_link_element()
        if show_more_posts_link is None:
            return
        show_more_posts_link.move_to_element()
        show_more_posts_link.click()
        time.sleep(1)

    def __get_more_posts_link_element(self):
        return self.browser.driver.find_element(By.CLASS_NAME, "showmoreposts")

    def search_for_string(self, string_to_search):
        while True:
            is_string_on_page = self.__is_string_on_posts_page(string_to_search)
            is_show_more_posts_visible = self.__is_show_more_posts_visible()
            stop_condition = is_string_on_page or not is_show_more_posts_visible
            if stop_condition:
                break
            else:
                self.__show_more_posts()
        return is_string_on_page
