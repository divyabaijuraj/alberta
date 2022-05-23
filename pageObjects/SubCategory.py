import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from utilities.base_class import BaseFunc
from selenium.webdriver.common.by import By

class SubCategory(BaseFunc):
    #// a[contains(text(), 'INVENTORY')]


    link_inventory_xpath="//a[@class ='nav-link  dropdown-toggle sub text-uppercase'][1]"
    link_subcategory_xpath=" //a [contains(text(),' Sub Category ')]"
    button_addnewsubcat_xpath="//i[@class='fa fa-plus']"
    ####subcategory add new items
    textbox_subcatname_id = 'add_vsubcategoryname'
    dropdown_category_id='add_cat_code'
    button_savesubcat_id='save_subcategory'
    button_cancelsubcat_xpath="//button[contains(text(),'Cancel')]"



    #######  Validating subcat add
    link_subcatname_xpath='//tbody/tr/td/input'

    alert_msg="//*[contains(text(),'SubCategory Already Exist!!')]"
    def __init__(self,driver):
        self.driver=driver

    def inventory_subcategoryClick(self):
       #self.driver.find_element(By.XPATH, self.link_inventory_xpath).click()
       #time.sleep(2)
       inventory= self.driver.find_element(By.XPATH,self.link_inventory_xpath)
       subcategory=self.driver.find_element(By.XPATH,self.link_subcategory_xpath)

       actions= ActionChains(self.driver)
       actions.move_to_element(inventory)
       actions.click(subcategory)
       actions.perform()
       time.sleep(2)
    def addNewSubCategoryClick(self):
       return  self.wait_presence_of_element_located(By.XPATH,self.button_addnewsubcat_xpath).click()

    def get_subcat_name(self):
        return self.wait_presence_of_element_located(By.ID, self.textbox_subcatname_id)

    def add_Subcat_name(self, Name):
        if(Name is None):
            pass
        else:
            for i in Name:
                self.get_subcat_name().send_keys(i)

    def add_Category_name(self,Category):
        if Category is None:
            pass
        else:
            dropdown=Select(self.wait_presence_of_element_located(By.ID,self.dropdown_category_id))
            dropdown.select_by_visible_text(Category)
            time.sleep(2)

    def saveSubCatClick(self):
        self.wait_presence_of_element_located(By.ID,self.button_savesubcat_id).click()

        if  (self.wait_presence_of_element_located(By.ID, self.textbox_subcatname_id).get_attribute("value")=="") :
            print("Please fill the field in save")
            subcat_name=self.wait_presence_of_element_located(By.ID, self.textbox_subcatname_id)
            subcat_name.send_keys("TESTING")
            self.wait_presence_of_element_located(By.ID, self.button_savesubcat_id).click()
            time.sleep(2)

        elif(self.wait_presence_of_element_located(By.ID,self.dropdown_category_id).get_attribute("value") =="") :
            dropdown = Select(self.wait_presence_of_element_located(By.ID, self.dropdown_category_id))
            dropdown.select_by_visible_text("Kiosk")
            self.wait_presence_of_element_located(By.ID, self.button_savesubcat_id).click()
            time.sleep(2)


    def validateSubcatAdd(self):

        print("reached validate category")
        search_input = "Test"

        try:


            elements = self.driver.find_elements(By.XPATH, self.link_subcatname_xpath)
            print("Length of elements:",len(elements))
            for i in elements:
                if(i.get_attribute("value") == search_input):
                    print("Subcategory Added successfully")


            time.sleep(2)

        except NoSuchElementException:
            print("No such element exist")

    def cancelSubCatClick(self):
        self.wait_presence_of_element_located(By.XPATH,self.button_cancelsubcat_xpath)