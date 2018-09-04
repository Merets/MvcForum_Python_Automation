from selenium.webdriver.common.by import By


class RegistrationPage(object):
    def __init__(self, browser):
        self.browser = browser
        self.element_id_username = "UserName"
        self.element_id_password = "Password"
        self.element_id_confirm_password = "ConfirmPassword"
        self.element_id_email = "Email"

    def fill_input_text(self, element_id, text_value):
        description = f'{element_id} input Element'
        element = self.browser.wait_for_element(By.ID, element_id, 10, description)
        element.send_keys(text_value)
        print(f'Value "{text_value}" inserted into "{element_id}" input field')

    def register_submit(self):
        register_button = self.browser.wait_for_element(By.CSS_SELECTOR, "button[type='submit']", 10, "Register Submit Button")
        register_button.click()
        print('Registration complete')

