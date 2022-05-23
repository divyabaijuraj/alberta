
import time
from pageObjects.SubCategory import SubCategory
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
        self.sub_cat = SubCategory(self.driver)
        self.ut=Utilities()


    @data(*Utilities.read_data_from_excel("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\alberta\\TestData\\SUBCAT.xlsx", "Sheet1"))
    @unpack
    def test_subcatadd(self,Name,Category):

            self.lg.login_page_credentials(self.username, self.password)
            self.sub_cat.inventory_subcategoryClick()
            self.sub_cat.addNewSubCategoryClick()
            self.sub_cat.add_Subcat_name(Name)
            self.sub_cat.add_Category_name(Category)
            self.sub_cat.saveSubCatClick()
            time.sleep(2)
            self.sub_cat.validateSubcatAdd()
