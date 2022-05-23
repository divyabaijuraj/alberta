import time
from random import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from utilities.base_class import BaseFunc
class EmployeeEdit(BaseFunc):
    #link_employee_linktext = 'EMPLOYEE'

    link_employee_xpath='/html/body/nav[1]/div/div/div/ul/li[4]/a'
    link_subemp_css_selector = "//a[@class='dropdown-item sub-dropdown text-uppercase'][normalize-space()='EMPLOYEE']"
    button_addnew_linktext = 'ADD NEW'

    textbox_firstname_id = 'input-vfname'
    textbox_lastname_id = 'input-vlname'
    textbox_phone_id = 'input-phone'
    textbox_address1_id = 'input-vaddress1'
    textbox_address2_id = 'input-vaddress2'
    textbox_city_id = 'input-city'
    textbox_state_id = 'input-state'
    textbox_zip_id = 'input-zip'
    dropdown_usertype_id = 'input-vusertype'
    dropdown_status_id = 'input-estatus'

    # checkbox_access_class='form-check-label font-weight-bold'

    checkbox_pos_xpath = '//*[@id="vendorForm"]/div[2]/div[2]/div/div/div/div/div[1]/label/input'
    textbox_posuserid_id = 'input-vuserid'
    textbox_pospassword_id = 'input-vpassword'
    textbox_pos_confirm_id = "input-re-vpassword"
##fetching all checkboxes in search page
    all_search_names_xpath = '//tbody//tr/td'

    button_save_id = 'saveCustomer'
    ##   save message to validate

    message_save_exist_xpath = '//div[@class="alert alert-danger"]'
    message_save_new_xpath = '//div[@class="alert alert-success"]'

    def __init__(self, driver):
        self.driver = driver

    # def _init_(self, driver):
    #  super()._init_(driver)
    # self.driver = driver

    def EmployeeClick(self):
        self.driver.find_element(By.XPATH, self.link_employee_xpath).click()
        #self.wait_presence_of_element_located(By.XPATH, self.link_employee_xpath).click()
        time.sleep(2)

    def SubmenuEmployeeClick(self):
        self.driver.find_element(By.XPATH, self.link_subemp_css_selector).click()
        #self.wait_presence_of_element_located(By.XPATH, self.link_subemp_css_selector).click()



    def setAddFirstname(self, Firstname):
        self.wait_presence_of_element_located(By.ID, self.textbox_firstname_id).clear()

        return self.wait_presence_of_element_located(By.ID, self.textbox_firstname_id).send_keys(Firstname)
    def setAddLastname(self, lastname):

        self.wait_presence_oflement_located(By.ID, self.textbox_lastname_id).clear()
        return self.wait_presence_of_element_located(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def setAddPhone(self, phone):
        #self.driver.find_element(By.ID, self.textbox_phone_id).clear()
        self.driver.find_element(By.ID, self.textbox_phone_id).click()
        return self.wait_presence_of_element_located(By.ID, self.textbox_phone_id).send_keys(phone)

    def setAddress1(self, Address1):
        self.wait_presence_of_element_located(By.ID, self.textbox_address1_id).clear()
        return self.wait_presence_of_element_located(By.ID, self.textbox_address1_id).send_keys(Address1)

    def setAddress2(self, Address2):
        self.wait_presence_of_element_located(By.ID, self.textbox_address2_id).clear()

        return self.wait_presence_of_element_located(By.ID, self.textbox_address2_id).send_keys(Address2)

    def setCity(self, City):
        self.wait_presence_of_element_located(By.ID, self.textbox_city_id).clear()
        return self.wait_presence_of_element_located(By.ID, self.textbox_city_id).send_keys(City)

    def setState(self, State):
        self.wait_presence_of_element_located(By.ID, self.textbox_state_id).clear()

        return self.wait_presence_of_element_located(By.ID, self.textbox_state_id).send_keys(State)

    def setZipcode(self, Zipcode):
        self.wait_presence_of_element_located(By.ID, self.textbox_zip_id).clear()
        return self.wait_presence_of_element_located(By.ID, self.textbox_zip_id).send_keys(Zipcode)

    def setUsertype(self, Usertype):
        dropdown = Select(self.wait_presence_of_element_located(By.ID, self.dropdown_usertype_id))
        dropdown.select_by_index(Usertype)

    def setStatus(self, Status):
        # dropdn=Select(self.driver.find_element(By.ID, self.dropdown_status_id))
        dropdn = Select(self.wait_presence_of_element_located(By.ID, self.dropdown_status_id))
        dropdn.select_by_visible_text(Status)
        time.sleep(2)

    def acess(self):
        if(self.wait_presence_of_element_located(By.XPATH, self.checkbox_pos_xpath).is_selected()):
            pass
        else:
            self.wait_presence_of_element_located(By.XPATH, self.checkbox_pos_xpath).click()
        time.sleep(2)

    def albertaPos(self, Posid, Password, Cpassword):
        self.wait_presence_of_element_located(By.ID, self.textbox_posuserid_id).send_keys(Posid)

        self.wait_presence_of_element_located(By.ID, self.textbox_pospassword_id).send_keys(Password)

        self.wait_presence_of_element_located(By.ID, self.textbox_pos_confirm_id).send_keys(Cpassword)

    def saveCustomer(self):
        self.driver.find_element(By.ID, self.button_save_id).click()
        time.sleep(2)
        print(self.driver.title, "***")
        if (self.driver.title == "Customer-Alberta | Employee Create"):

            if (self.driver.find_element(By.XPATH, self.message_save_exist_xpath).is_displayed()):
                msg = self.driver.find_element(By.XPATH, self.message_save_exist_xpath).text
                user_exist = msg.split('.')
                if (user_exist[0] == 'Pos User id is already exists'):
                    print("testcase passed .User already exists.")

        elif (self.driver.title == "Customer-Alberta | Employee"):

            if (self.driver.find_element(By.XPATH, self.message_save_new_xpath).is_displayed()):
                new_msg = self.driver.find_element(By.XPATH, self.message_save_new_xpath).text
                print(new_msg)

        # time.sleep(2)


    def searchpage_Checkbox(self):
        self.EmployeeClick()
        self.SubmenuEmployeeClick()

        search_input = "Amrita"
        try:
            name = self.driver.find_element(By.XPATH, "//tbody/tr/td/a/span[contains(text(),'" + search_input + "')]")
            name.click()
            time.sleep(2)

        except NoSuchElementException:
            print("No such element exist")



        time.sleep(2)
    def ddtEditUser(self, Firstname, Lastname, Phone, Address1, Address2, City, State, Zipcode, Usertype, Status, Posid,Password, Cpassword):
        print("******************ddt")
        self.EmployeeClick()
        self.SubmenuEmployeeClick()
        self.searchpage_Checkbox()
        time.sleep(3)
        self.setAddFirstname(Firstname)

        self.setAddLastname(Lastname)
        self.setAddPhone(Phone)
        self.setAddress1(Address1)
        self.setAddress2(Address2)
        self.setCity(City)
        self.setState(State)
        self.setZipcode(Zipcode)
        self.setUsertype(Usertype)
        self.setStatus(Status)
        self.acess()
        self.albertaPos(Posid, Password, Cpassword)
        self.saveCustomer()