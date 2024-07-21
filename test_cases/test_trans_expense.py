import pytest
from page_objects.login_page import LoginPage
from page_objects.trans_expense import Expense
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time


class Test_003Trans_Expense:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.log_gen()

    def test_transaction_expense(self, setup):
        self.logger.info("*****  Test_003_Trans_Expense  *****")
        self.logger.info("*****  Verifying Transaction of Expense  *****")
        self.driver = setup
        self.driver.get(self.base_url)
        # self.login_page = LoginPage(self.driver)
        self.create_expense_entry = Expense(self.driver)

        try:
            # Step 1: Login
            # self.login_page.set_username("testsuper")
            # self.login_page.set_password("pass123")
            # self.login_page.click_signin()
            # time.sleep(5)  # Use WebDriverWait for better reliability

            # Step 2: Navigate to Extra Income
            self.create_expense_entry.click_on_menu_transactions()
            self.create_expense_entry.click_on_submenu_expense()
            time.sleep(5)
            self.create_expense_entry.click_button_new()

            # Step 3: Fill Extra Income Form
            self.create_expense_entry.select_expense_type("General")
            self.create_expense_entry.select_mode_of_expense("CASH")

            self.create_expense_entry.set_amount(510)
            self.create_expense_entry.add_random_remarks()
            self.create_expense_entry.click_on_save()

            self.logger.info("******  Expense Transaction validation  ******* ")

            # Step 4: Validate Success Message
            actual_message = self.create_expense_entry.successful_msg()
            expected_message = "Successful\nExpenses Created"
            assert actual_message == expected_message
            self.logger.info("*****  Transaction entry of Expense is Successful *****")

            # Step 5: Verify Remarks in Table
            assert self.create_expense_entry.verify_remarks_in_table(), "Random remarks not found in the table"
            self.logger.info("*****  Random remarks verified in the table *****")

        except Exception as e:
            self.driver.save_screenshot(".\\screenshots\\test_transaction_expense.png")
            self.logger.error(f"Test failed due to: {str(e)}")
            raise

        finally:
            self.driver.close()
