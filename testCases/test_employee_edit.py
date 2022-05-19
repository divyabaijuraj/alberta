import pytest
import time

import softest
from ddt import data
from selenium import webdriver
from pageObjects.Employee import Employee
from pageObjects.EmployeeEdit import EmployeeEdit
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.utils import Utilities
from ddt import ddt, unpack, data

@ddt
class Test_002_Employee(softest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lg = LoginPage(self.driver)
        self.emp_edit=EmployeeEdit(self.driver)
   # def test_edit_employee(self):
    #    self.lg.login_page_credentials(self.username, self.password)
        ## self.logger.info("Login passed in  test_employee_search")
     #   self.emp_edit.searchpage_Checkbox()



    @data(*Utilities.read_data_from_excel("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\TestData\\editusers.xlsx", "Sheet1"))
    @unpack
    def test_edit_employee(self, Firstname, Lastname, Phone, Address1, Address2, City, State, Zipcode, Usertype,Status, Posid, Password, Cpassword):
               self.lg.login_page_credentials(self.username, self.password)
              ## self.logger.info("Login passed in  test_employee_search")
               #.emp_edit.searchpage_Checkbox()
               self.emp_edit.ddtEditUser(Firstname, Lastname, Phone, Address1, Address2, City, State, Zipcode, Usertype,Status, Posid, Password, Cpassword)

               self.logger.info(" passed in  test_edit_employee")
