from selenium.webdriver.common.by import By


class LogonPage(object):
    def __init__(self, browser):
        self.browser = browser
        self.element_id_username = "UserName"
        self.element_id_password = "Password"

    def fill_input_text(self, element_id, text_value):
        description = f'{element_id} input Element'
        element = self.browser.wait_for_element(By.ID, element_id, description, 10)
        element.this_element.send_keys(text_value)
        print(f'Value "{text_value}" inserted into "{element_id}" input field')

    def logon_submit(self):
        logon_button = self.browser.wait_for_element(By.CSS_SELECTOR, "button[type='submit']",
                                                     "Logon Submit Button", 10)
        logon_button.this_element.click()
        print('Logon complete')
