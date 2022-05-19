import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from utilities.base_class import BaseFunc

class EmployeeAddUser(BaseFunc):
    textbox_firstname_id='input-vfname'
    textbox_lastname_id='input-vlname'
    textbox_phone_id='input-phone'
    textbox_address1_id='input-vaddress1'
    textbox_address2_id='input-vaddress2'
    textbox_city_id='input-city'
    textbox_state_id='input-state'
    textbox_zip_id='input-zip'
    dropdown_usertype_id='input-vusertype'
    dropdown_status_id='input-estatus'

    #checkbox_access_class='form-check-label font-weight-bold'

    checkbox_pos_xpath='//*[@id="vendorForm"]/div[2]/div[2]/div/div/div/div/div[1]/label/input'
    textbox_posuserid_id='input-vuserid'
    textbox_pospassword_id='input-vpassword'
    textbox_pos_confirm_id="input-re-vpassword"

    button_save_id='saveCustomer'

    def __init__(self,driver):
        self.driver=driver

    def setAddFirstname(self,Firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(self.Firstname)
        #return self.wait_presence_of_element_located(By.ID, self.textbox_firstname_id).send_keys("Anu")

    def setAddLastname(self):
        #self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(self.Lastname)
        return self.wait_presence_of_element_located(By.ID, self.textbox_lastname_id).send_keys("K")


    def setAddPhone(self):
        self.driver.find_element(By.ID, self.textbox_phone_id).click()
        time.sleep(2)
        return self.wait_presence_of_element_located(By.ID, self.textbox_phone_id).send_keys("456-128-2605")


    def setAddress1(self):
        #self.driver.find_element(By.ID,self.textbox_address1_id).send_keys(self.Address1)
        return self.wait_presence_of_element_located(By.ID, self.textbox_address1_id).send_keys("RMnagar")

    def setAddress2(self):
        #self.driver.find_element(By.ID,self.textbox_address2_id).send_keys(self.Address2)
        return self.wait_presence_of_element_located(By.ID, self.textbox_address2_id).send_keys("Indira Nagar")
    def setCity(self):
        #self.driver.find_element(By.ID,self.textbox_city_id).send_keys(self.City)
        return self.wait_presence_of_element_located(By.ID, self.textbox_city_id).send_keys("Bangalore")
        time.sleep(2)

    def setState(self):
        #self.driver.find_element(By.ID, self.textbox_state_id).send_keys(self.State)
        return self.wait_presence_of_element_located(By.ID, self.textbox_state_id).send_keys("Karnataka")

    def ddtAddUser(self,Firstname,Lastname,Phone,Address1,Address2,City,State):

       print("firstname :",self.list1)
       self.setAddFirstname(Firstname)

       '''
       self.setAddLastname(Lastname)
       self.setAddPhone(Phone)
       self.setAddress1(Address1)
       self.setAddress2(Address2)
       self.setCity(City)
       self.setState(State)
    
    '''



    ######################################################33333333333333333
    '''
    def setZipcode(self):

            return self.wait_presence_of_element_located(By.ID, self.textbox_zip_id).send_keys("560016")

    def setUsertype(self):

       dropdown=Select(self.wait_presence_of_element_located(By.ID, self.dropdown_usertype_id))
       dropdown.select_by_index(2)


    def setStatus(self):
        #dropdn=Select(self.driver.find_element(By.ID, self.dropdown_status_id))
        dropdn=Select(self.wait_presence_of_element_located(By.ID, self.dropdown_status_id))
        dropdn.select_by_visible_text('Active')
        time.sleep(2)

    def acess(self):
        self.wait_presence_of_element_located(By.XPATH, self.checkbox_pos_xpath).click()
        time.sleep(2)

    def albertaPos(self):
        self.wait_presence_of_element_located(By.ID,self.textbox_posuserid_id).send_keys("504")

        self.wait_presence_of_element_located(By.ID, self.textbox_pospassword_id).send_keys("WXYZ")

        self.wait_presence_of_element_located(By.ID, self.textbox_pos_confirm_id).send_keys("WXYZ")


    def saveCustomer(self):
        self.driver.find_element(By.ID,  self.button_save_id).click()
        time.sleep(2)
   
'''