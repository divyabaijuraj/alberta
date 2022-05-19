import pytest
import softest
from ddt import ddt,  data,unpack
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from utilities.utils import Utilities
@ddt
class Test_001_Login_ddtold(softest.TestCase):
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    @pytest.fixture(autouse=True)
    def test_login(self,setup):
        self.logger.info("***** Verifying Login test *********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        #lst=Utilities.read_data_from_excel("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\TestData\\loginData.xlsx", "Sheet1")
        #print(lst,"*****************")


    @data(*Utilities.read_data_from_excel("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\TestData\\LoginData.xlsx", "Sheet1"))
    @unpack
    def test_login_ddt(self,username,password,exp):
           
            print("reached ******")
            self.lp.login_page_credentials(username, password)
    '''         
            act_title=self.driver.title
            list1=[]
            expected_title='Customer-Alberta | Dashboard'
            if act_title ==expected_title:
                if exp=="pass":

                    print("!11111111111111111111")

                    self.logger.info("*****   passed *********")
                    self.lp.clickLogout()
                    list1.append("pass")
                   # time.sleep(2)

                elif exp=="fail":
                      print("!222222222222222")
                      self.logger.error("*****   failed *********")
                      self.lp.clickLogout()
                      list1.append("fail")



            elif act_title !='Customer-Alberta | Dashboard':
                if exp == "pass":
                            self.logger.info("*****   failed *********")
                            self.lp.clickLogout()
                            list1.append("fail")


                elif exp == "fail":
                              self.logger.error("*****   passed*********")
                              list1.append("pass")

            if "fail" not in list1:
                self.logger.info("** Login DDT test passed **")
                self.logger.info("** End of the login DDT test **")
                self.logger.info("** completed Test_002_DDT_Login **")
                # self.driver.close()
                assert True
            else:
                self.logger.info("** Login DDT test passed **")
                self.driver.close()
                assert False

            self.logger.info("** End of login DDT test **")
            self.logger.info("** Completed class Test_002_ddt_login **")
'''







##############################
    '''
    
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
                
                
                
                
                
                
                
                
                
                
                
                
                
                 if "fail" not in list1:
                    print("List1 is pass")
                    self. logger.info("************Login DDT test case passed********")
                    self.driver.close()
                    assert True
            else:
                    self.logger.info("************Login DDT test case is failed ********")
                    self.driver.close()
                    assert False
                
                

    '''