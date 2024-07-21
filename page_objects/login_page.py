from selenium.webdriver.common.by import By

from utilities.wait_helper import HelperFunc


class LoginPage:
    textbox_username_xpath = "//input[@placeholder='Username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_signin_xpath = "//span[@class='p-button-label p-c']"
    displayed_dashboard_xpath = "//span[normalize-space()='Dashboard']"
    button_signout_xpath = "(//button[normalize-space()='Sign out'])[1]"

    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunc(driver)

    def set_username(self, username):
        username_field = self.helper.find_element(By.XPATH, self.textbox_username_xpath)
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.helper.find_element(By.XPATH, self.textbox_password_xpath)
        password_field.clear()
        password_field.send_keys(password)

    def click_signin(self):
        signin_button = self.helper.wait_for_element_to_be_clickable(By.XPATH, self.button_signin_xpath)
        signin_button.click()

    def click_signout(self):
        signout_button = self.helper.wait_for_element_to_be_clickable(By.XPATH, self.button_signout_xpath)
        signout_button.click()

    def displayed_dashboard(self):
        try:
            dashboard_element = self.helper.wait_for_element_to_be_visible(By.XPATH, self.displayed_dashboard_xpath)
            return dashboard_element.is_displayed()
        except:
            return False
