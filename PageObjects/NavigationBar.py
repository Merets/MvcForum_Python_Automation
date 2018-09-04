import time

from selenium.webdriver.common.by import By


class NavigationBar(object):
    def __init__(self, browser):
        self.browser = browser

    def open_my_tools_menu(self):
        my_tools_menu = self.browser.wait_for_element(By.CLASS_NAME, "mytoolslink", 10, "My Tools Menu Button")
        my_tools_menu.click()

    def get_text_from_edit_user_menu_item(self):
        menu_items_href = self.get_menu_items()
        edit_user_item = menu_items_href[1]
        return edit_user_item.text

    def get_menu_items(self):
        self.open_my_tools_menu()
        menu_items_href = self.browser.container.find_elements_by_css_selector("#mvcforum-nav > ul > li > ul > li > a")
        return menu_items_href

    def logoff(self):
        menu_items_href = self.get_menu_items()
        logoff = menu_items_href[3]
        logoff.click()

