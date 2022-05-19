import time
from pageObjects.Employee import Employee
from pageObjects.EmployeeAddUserddt import EmployeeAddUserddt

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
import pytest
import softest
from ddt import ddt, unpack, data

from utilities.utils import Utilities


@ddt
class Test_003_AddEmployee(softest.TestCase):
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
        self.emp_add = EmployeeAddUserddt(self.driver)
        self.ut=Utilities()


    @data(*Utilities.read_data_from_excel("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\TestData\\addUsers.xlsx","Sheet1"))
    @unpack
    def test_add_employee(self,Firstname, Lastname, Phone, Address1, Address2, City, State,Zipcode,Usertype,Status,Posid,Password,Cpassword):

            self.lg.login_page_credentials(self.username, self.password)
            self.emp_add.ddtAddUser(Firstname, Lastname, Phone, Address1, Address2, City, State,Zipcode,Usertype,Status,Posid,Password,Cpassword)
