import time
from utilities import xcelutilities
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


logger = LogGen.loggen()

class Test_001_Login_ddt():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_login_ddt(self, setup):
        self.path = "C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\TestData\\LoginData.xlsx"
        self.logger.info("** class Test_002_DDT_login ** ")
        self.logger.info("*** verifying login ddt test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = xcelutilities.getRowCount(self.path, 'Sheet1')

        lst = []
        for i in range(2, self.rows + 1):
            self.username = xcelutilities.readData(self.path, 'Sheet1', i, 1)
            self.password = xcelutilities.readData(self.path, 'Sheet1', i, 2)
            self.exp = xcelutilities.readData(self.path, 'Sheet1', i, 3)
            self.lp.login_page_credentials(self.username, self.password)
            time.sleep(3)

            act_title = self.driver.title
            expected_title = "Customer-Alberta | Dashboard"
            if act_title == expected_title:
                if self.exp == "pass":
                    self.logger.info("** passed ***")
                    self.lp.clickLogout()
                    lst.append("pass")
                elif self.exp == "fail":
                    self.logger.info("** failed **")
                    self.lp.clickLogout()
                    lst.append("fail")
            elif act_title != expected_title:
                if self.exp == "pass":
                    self.logger.info("** failed **")
                    self.lp.clickLogout()
                    lst.append("fail")
                elif self.exp == "fail":
                    self.logger.info("** passed **")
                    self.driver.close()

                    lst.append("pass")

            if "fail" not in lst:
                self.logger.info("** Login DDT test passed **")
                self.logger.info("** End of the login DDT test **")
                self.logger.info("** completed Test_002_DDT_Login **")

                assert True
            else:
                self.logger.info("** Login DDT test passed **")
                self.driver.close()
                assert False

        self.logger.info("** End of login DDT test **")
        self.logger.info("** Completed class Test***")