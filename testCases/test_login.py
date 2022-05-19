import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info("*******  Test_001_Login *******")

        self.logger.info("*********  Verifying Home page title ******** ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title=self.driver.title

        if act_title =="Administration | Login":
            print("from login page title")
            assert True

            self.logger.info("***** Home page title test is passed *********")
            time.sleep(2)
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.logger.error("***** Home page title test is failed *********")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.logger.info("***** Verifying Login test *********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title =='Customer-Alberta | Dashboard':
            print("from dashboard page")
            assert True

            self.logger.info("*****  Login testcase passed *********")
            time.sleep(2)
            self.driver.close()
        else:
            self.logger.error("*****  Login testcase failed *********")

            assert False
            self.driver.close()
