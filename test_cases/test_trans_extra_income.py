import pytest
from page_objects.login_page import LoginPage
from page_objects.trans_extra_income_page import ExtraIncome
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time


class Test_002_Trans_Extra_Income:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.log_gen()

    def test_transaction_extra_income(self, setup):
        self.logger.info("*****  Test_002_Trans_Extra_Income  *****")
        self.logger.info("*****  Verifying Transaction of Extra Income  *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.create_extra_income = ExtraIncome(self.driver)

        try:
            # Step 1: Login
            # self.login_page.set_username("testsuper")
            # self.login_page.set_password("pass123")
            # self.login_page.click_signin()
            # time.sleep(5)  # Use WebDriverWait for better reliability

            # Step 2: Navigate to Extra Income
            self.create_extra_income.click_on_menu_transactions()
            time.sleep(5)
            self.create_extra_income.click_on_submenu_transactions()
            time.sleep(5)
            self.create_extra_income.click_button_new()

            # Step 3: Fill Extra Income Form
            self.create_extra_income.select_income_type("Sundry")
            self.create_extra_income.select_mode_of_income("CASH")
            self.create_extra_income.set_amount(510)
            self.create_extra_income.add_random_remarks()
            self.create_extra_income.click_on_save()

            self.logger.info("******  Transaction validation  ******* ")

            # Step 4: Validate Success Message
            actual_message = self.create_extra_income.successful_msg()
            expected_message = "Successful\nIncome Created"
            assert actual_message == expected_message
            self.logger.info("*****  Transaction of Extra Income added Successfully  *****")

        except Exception as e:
            self.driver.save_screenshot(".\\screenshots\\test_transaction_extra_income.png")
            self.logger.error(f"Test failed due to: {str(e)}")
            raise

        finally:
            self.driver.close()
