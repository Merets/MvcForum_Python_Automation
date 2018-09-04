import random

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options

from AutomationInfrastructure.Browser import Browser
from Helpers.User import User
from MvcForumApp import MvcForumApp

URL = 'http://localhost:8080/'


def initialize_browser(url):
    chrome_options = chrome.options.Options()

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)

    new_browser = Browser(driver, "Chrome")
    return new_browser


def get_random_number():
    number = random.randint(100000, 999999)
    return number


def generate_user():
    random_number = get_random_number()
    username = "user" + str(random_number)
    password = random_number
    email = username + '@gmail.com'
    new_user = User(username, password, email)
    return new_user


def test_user_can_see_his_username_after_registration_logoff_and_login_again():
    browser = initialize_browser(URL)
    user = generate_user()
    print(user)

    mvc_forum_app = MvcForumApp(browser)
    mvc_forum_app.register_new_user(user)
    mvc_forum_app.logoff()
    mvc_forum_app.logon(user)
    username_from_menu = mvc_forum_app.get_username_from_menu()

    assert user.username == username_from_menu
    print(f'Username "{username_from_menu}" should be "{user.username}"')
    print("Test passed!")

    browser.quit()


test_user_can_see_his_username_after_registration_logoff_and_login_again()
