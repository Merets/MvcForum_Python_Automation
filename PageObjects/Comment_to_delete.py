import time

from selenium.webdriver.common.by import By


class Comment(object):
    def __init__(self, browser):
        self.browser = browser

    def write_comment(self, post_string):
        self.browser.switch_to_iframe("PostContent_ifr")
        post_text_field = self.browser.wait_for_element(By.ID, "tinymce", "Post Text Field")
        post_text_field.move_to_element()
        post_text_field.send_keys(post_string)
        self.browser.switch_back_to_main()

    def add_comment(self):
        add_post_button = self.browser.wait_for_element(By.ID, "createpostbutton", "Add Post Button")
        add_post_button.click()

    def __is_string_on_comments_page(self, string_to_search):
        if type(string_to_search) is not str:
            raise Exception("Search value should be a string!")
        all_p_elements = self.browser.driver.find_elements(By.TAG_NAME, "p")
        for p in all_p_elements:
            if string_to_search in p.text:
                return True
        return False

    def __is_show_more_comments_visible(self):
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

    def __is_string_on_page(self, string_to_search):  # TODO: rename to is_string_on_page()
        while True:
            is_string_on_page = self.__is_string_on_comments_page(string_to_search)
            is_show_more_posts_visible = self.__is_show_more_comments_visible()
            stop_condition = is_string_on_page or not is_show_more_posts_visible
            if stop_condition:
                break
            else:
                self.__show_more_posts()
        return is_string_on_page

    def like_the_comment(self, user, expected_post_text):
        if self.__is_string_on_page(expected_post_text):
            list_of_user_posts = self.__get_all_user_comments(user)
            for post in list_of_user_posts:
                postcontent = post.wait_for_child_element(By.CLASS_NAME, "postcontent", "postcontent")
                p_elements = postcontent.find_elements(By.TAG_NAME, "p")
                text_p = p_elements[1].text
                if expected_post_text in text_p:
                    votelink_elements = post.find_elements(By.CLASS_NAME, "votelink")
                    for vote_link in votelink_elements:
                        if vote_link.get_attribute("data-votetype") == "up":
                            assert vote_link.get_attribute("data-hasvoted") == "false"
                            vote_link.click()

    def __get_all_user_comments(self, user):
        self.browser.wait_for_element(By.CLASS_NAME, "topicshow", "Main div of all posts")
        all_posts = self.browser.driver.find_elements(By.CLASS_NAME, "post")
        posts_from_user = []
        for post in all_posts:
            postbodytop = post.wait_for_child_element(By.CLASS_NAME, "postbodytop", "post body top")
            username_of_post = postbodytop.wait_for_child_element(By.TAG_NAME, "a", "post username link")
            if username_of_post.text == user.username:
                posts_from_user.append(post)
        return posts_from_user
