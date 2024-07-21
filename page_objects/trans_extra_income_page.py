from selenium.webdriver.common.by import By
from utilities.wait_helper import HelperFunc


class ExtraIncome:
    lnk_menu_transactions_xpath = "//span[normalize-space()='Transactions']"
    lnk_submenu_extra_income_xpath = "(//span[normalize-space()='Extra Income'])[1]"
    btn_new_css_selector = "button[aria-label='New']"

    # Selectors for a new transaction.
    txt_box_income_type_xpath = "//div[@class='p-dropdown p-component p-inputwrapper']"
    income_type_sundry_xpath = "//li[@aria-label='Sundry']"

    txt_box_mode_of_income_xpath = "//span[normalize-space()='CASH']"
    lst_mode_of_income_xpath = "//li[@aria-label='BANK']"

    txt_box_amount_xpath = "//input[@id='amount']"

    txt_box_bank_type_xpath = "//input[@placeholder='Select']"
    lst_bank_name_xpath = "//td[normalize-space()='Test']"

    txt_box_remarks_xpath = "//textarea[@class='p-inputtextarea p-inputtext p-component']"
    btn_save_xpath = "//span[normalize-space()='Save']"
    txt_msg_success_xpath = "//div[@class='p-toast-message-text']"
    tbl_body_xpath = "//tbody"

    def __init__(self, driver):

        self.driver = driver
        self.helper = HelperFunc(driver)
        self.random_comment = ""

    def click_on_menu_transactions(self):
        self.helper.click_element(By.XPATH, self.lnk_menu_transactions_xpath)

    def click_on_submenu_transactions(self):
        self.helper.click_element(By.XPATH, self.lnk_submenu_extra_income_xpath)

    def click_button_new(self):
        self.helper.click_element(By.CSS_SELECTOR, self.btn_new_css_selector)

    def select_income_type(self, option_text):
        self.helper.select_from_dropdown(By.XPATH, self.txt_box_income_type_xpath, By.XPATH,
                                         f"//li[@aria-label='{option_text}']")

    def select_mode_of_income(self, option_text):
        self.helper.select_from_dropdown(By.XPATH, self.txt_box_mode_of_income_xpath, By.XPATH,
                                         f"//li[@aria-label='{option_text}']")

    def set_amount(self, amount):
        self.helper.send_keys_to_element(By.XPATH, self.txt_box_amount_xpath, amount)

    def add_random_remarks(self):
        self.random_comment = self.helper.random_str_generator(size=15)
        self.helper.send_keys_to_element(By.XPATH, self.txt_box_remarks_xpath, self.random_comment)

    def click_on_save(self):
        self.helper.click_element(By.XPATH, self.btn_save_xpath)

    def successful_msg(self):
        return self.helper.get_element_text(By.XPATH, self.txt_msg_success_xpath)

    def verify_remarks_in_table(self):
        return self.helper.is_entry_present_in_table(self.tbl_body_xpath, self.random_comment)


