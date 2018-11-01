from selenium.webdriver.common.by import By


class DiscussionPage(object):
    def __init__(self, browser):
        self.browser = browser

    def like_the_discussion(self):
        discussion_topic_post = self.browser.wait_for_element(By.CLASS_NAME, "topicstarterpost",
                                                              "Discussion Topic Post div")
        vote_up_link = discussion_topic_post \
            .wait_for_child_element(By.CSS_SELECTOR, ".topicstarterpost .postsocial a[data-votetype='up']")
        vote_up_link.click()
