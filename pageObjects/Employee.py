import time
import random
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.base_class import BaseFunc


class Employee(BaseFunc):
    link_employee_linktext = 'EMPLOYEE'
    link_subemp_css_selector = "//a[@class='dropdown-item sub-dropdown text-uppercase'][normalize-space()='EMPLOYEE']"
    button_addnew_linktext = 'ADD NEW'

    # search by name,email,status and phone
    search_name_xpath = '//*[@id="name"]'
    search_cellno_id = 'cell_number'
    search_email_id = 'email'
    search_status_id = "status"

    # delete rows

    all_checkboxes_name='selected[]'
    delete_button_id='employee_delete'
###element exist or not

    search_name_exists_xpath='//span[contains(text(),"Emp")]'

    def __init__(self, driver):
        self.driver = driver

    def EmployeeClick(self):
        # self.driver.find_element(By.LINK_TEXT,self.link_employee_linktext).click()
        return self.wait_presence_of_element_located(By.LINK_TEXT, self.link_employee_linktext).click()

    def SubmenuEmployeeClick(self):
        # self.driver.find_element(By.XPATH,self.link_subemp_css_selector).click()
        return self.wait_presence_of_element_located(By.XPATH, self.link_subemp_css_selector).click()

    def AddNewEmployeeClick(self):

        # self.element=self.driver.find_element(By.LINK_TEXT, self.button_addnew_linktext)
        self.element = self.wait_presence_of_element_located(By.LINK_TEXT, self.button_addnew_linktext).click()

        return self.mouse_actions(self.element)

    def get_emp_status(self):
        return self.wait_presence_of_element_located(By.ID, self.search_status_id)

    def Search_By_Status(self, emp_status):
        for i in emp_status:
            self.get_emp_status().send_keys(i)

            self.search_element_exist(emp_status)

            self.driver.refresh
            #self.wait_presence_of_element_located(By.ID, self.search_status_id).clear()

    def get_emp_email(self):
        return self.wait_presence_of_element_located(By.ID, self.search_email_id)

    def Search_By_Email(self, emp_email):
        for i in emp_email:
            self.get_emp_email().send_keys(i)
        self.search_element_exist(emp_email)

        self.wait_presence_of_element_located(By.ID, self.search_email_id).clear()
        self.driver.refresh()

    def get_emp_cellno(self):
        return self.wait_presence_of_element_located(By.ID, self.search_cellno_id)

    def Search_By_Cellno(self, emp_cellno):

        for i in emp_cellno:
            self.get_emp_cellno().send_keys(i)

        self.search_element_exist(emp_cellno)
        self.wait_presence_of_element_located(By.ID, self.search_cellno_id).clear()
        self.driver.refresh()

    def get_emp_name(self):
        return self.wait_presence_of_element_located(By.XPATH, self.search_name_xpath)

    def Search_By_Name(self, emp_name):
        for i in emp_name:
            self.get_emp_name().send_keys(i)
        time.sleep(2)

        self.search_element_exist( emp_name)
        time.sleep(2)
        self.wait_presence_of_element_located(By.XPATH, self.search_name_xpath).clear()
        self.driver.refresh()

    def Search_emp_details(self, emp_name, emp_cellno, emp_email, emp_status):
        self.EmployeeClick()
        self.SubmenuEmployeeClick()

        self.Search_By_Name(emp_name)
        self.Search_By_Cellno(emp_cellno)
        self.Search_By_Email(emp_email)
        self.Search_By_Status(emp_status)

    def search_element_exist(self,element):
        dict1={}
        for td in self.wait_presence_of_all_elements_located(By.XPATH,"//tbody/tr/td"):

            if element in td.text:

                dict1.update({element:"Match Found"})
            else:

                dict1.update({element: "Match do not Found"})
        print(dict1)
    ##################
    # Delete the rows
    def find_search_rows(self):
        self.EmployeeClick()
        self.SubmenuEmployeeClick()
        checkboxes = self.wait_presence_of_all_elements_located(By.NAME, self.all_checkboxes_name)
        num=len(checkboxes)
        try:
            if(num >0):
                print("Found")
        except NoSuchElementException:
            print("End")
            quit()
        rand_num=random.randint(0,num)
        rand_list=random.sample(range(0,num),3)


        ####Click on delete button
        for i in range(0,num):
            if(i==rand_num):
                if not checkboxes[rand_num].is_selected():
                    checkboxes[rand_num].click()
                    time.sleep(2)
                    self.wait_presence_of_element_located(By.ID, self.delete_button_id).click()
                    time.sleep(2)

                    try:
                          #alert=BaseFunc.alert_is_present()
                          #print("alert:",alert)
                          if(BaseFunc.alert_is_present(self)):

                                alert = self.driver.switch_to.alert
                                alert.accept()
                                print("alert Exists in page")
                    except TimeoutException:
                          print("alert does not Exist in page")


           # if i in rand_list:
              #  for j in rand_list:
                    #if not checkboxes[j].is_selected():
                    #    checkboxes[j].click()

        time.sleep(3)





