import pytest
import time
from selenium import webdriver
from pageObjects.Employee import Employee
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Employee:
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
        self.emp=Employee(self.driver)

    '''
    def test_employee_delete(self):
      self.lg.login_page_credentials(self.username, self.password)
      self.emp.find_search_rows()
    '''

    def test_employee_search(self):
        self.lg.login_page_credentials(self.username, self.password)
        self.logger.info("Login passed in  test_employee_search")

        self.emp_cellno = '984-800-1200'
        self.emp_name = 'Deepak'
        self.emp_email = "harikt@gmail.com"
        self.emp_status = "Active"
        self.emp.Search_emp_details(self.emp_name, self.emp_cellno, self.emp_email, self.emp_status)





    '''

    def test_dashboard(self,setup):
        self.logger.info("*******  Test_002_Employee *******")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.login=  LoginPage(self.driver)

        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        self.logger.info("******* Dashboard test case passed*******")
        self.driver.close()

        time.sleep(2)
    '''
    '''
    def test_emplyee_page(self,setup):
        self.driver =setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)

        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.emp = Employee(self.driver)
        self.emp.EmployeeClick()
        self.emp.SubmenuEmployeeClick()
        emp_title=self.driver.title


        if(emp_title =='Customer-Alberta | Employee' ):
            assert True
            self.logger.info("***** Employee page title test is passed *********")
        else:
            assert False
            self.logger.info("***** Employee page title test is failed*********")
        self.emp_cellno = '123-456-7891'
        self.emp_name = 'anusha'
        self.emp_email = "harikt@gmail.com"
        self.emp_status="Active"


       # self.emp.Search_emp_details(self.emp_name,self.emp_cellno,self.emp_email,self.emp_status)

        ###Delete rows
        self.emp.find_search_rows()

    '''