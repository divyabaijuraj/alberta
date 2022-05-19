import pytest
from selenium import webdriver
import time
from pageObjects.Employee import Employee
from pageObjects.EmployeeAddUser import EmployeeAddUser
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddEmployee:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def  test_addemployee(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)

        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.emp = Employee(self.driver)
        self.emp.EmployeeClick()
        self.emp.SubmenuEmployeeClick()

        time.sleep(2)
        self.emp.AddNewEmployeeClick()
        time.sleep(2)

        ##Employee Add userpage object creation
        emp_adduser=EmployeeAddUser(self.driver)
        emp_adduser.setAddFirstname()

        emp_adduser.setAddLastname()
        emp_adduser.setAddPhone()
        emp_adduser.setAddress1()
        emp_adduser.setAddress2()
        emp_adduser.setCity()

        emp_adduser.setState()
        emp_adduser.setZipcode()

        emp_adduser.setUsertype()

        emp_adduser.setStatus()

        emp_adduser.acess()
        emp_adduser.albertaPos()

        emp_adduser.saveCustomer()
        
