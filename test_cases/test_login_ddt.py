import pytest
import os
from page_objects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils



class Test_001_DDT_Login:
    base_url = ReadConfig.get_application_url()
    path = os.path.join(os.path.dirname(__file__), '..', 'test_cases', 'test_data', 'smps.xlsx')

    logger = LogGen.log_gen()

    def test_login_ddt(self, setup):
        self.logger.info("******  Test_002_DDT_login  ******")
        self.logger.info("******  Verifying Login DDT test ******")
        self.driver = setup
        self.driver.get(self.base_url)

        self.login_page = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        list_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            # self.login_page.set_username(self.user)
            # self.login_page.set_password(self.password)
            # self.login_page.click_signin()

            dashboard_displayed = self.login_page.displayed_dashboard()

            if dashboard_displayed:
                if self.exp == "pass":
                    self.logger.info(f"Test Case Passed for user: {self.user}")
                    self.login_page.click_signout()
                    list_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info(f"Test Case Failed for user: {self.user}")
                    self.login_page.click_signout()
                    list_status.append("fail")
            else:
                if self.exp == "pass":
                    self.logger.info(f"Test Case Failed for user: {self.user}")
                    list_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info(f"Test Case Passed for user: {self.user}")
                    list_status.append("pass")

        # print(list_status)
        if "fail" not in list_status:
            self.logger.info("********  Login DDT test passed   *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("********  Login DDT test failed   *****")
            self.driver.close()
            assert False

