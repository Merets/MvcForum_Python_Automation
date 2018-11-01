from selenium.webdriver.common.by import By


class ActivityPage(object):
    def __init__(self, browser):
        self.browser = browser

    def search_for_first_vote_up_badge(self, user):
        activity_entries_list = self.browser.driver.find_elements(By.CLASS_NAME, "activityentry")
        for activity in activity_entries_list:
            link_of_username = activity\
                .wait_for_child_element(By.CSS_SELECTOR, ".activityinfotext a", "Activity Username Link")
            if link_of_username.text == user.username:
                img = activity.wait_for_child_element(By.TAG_NAME, "img", "Activity img Element")
                alt = img.get_attribute("alt")
                if alt == "First Vote Up Received":
                    return True
        return False
