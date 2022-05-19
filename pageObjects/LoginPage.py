from selenium.webdriver.common.by import By
from selenium import webdriver

from utilities.base_class import BaseFunc


class LoginPage(BaseFunc):
    textbox_username_id = 'input_email'
    textbox_password_id = 'input-password'
    button_login_xpath = "//*[@class='btn btn-primary btn-block login-btns text-white font-weight-bold text-uppercase']"
    link_logout_class = "//*[@class='fa fa-sign-out fa-lg']"

    def __init__(self, driver):
        self.driver = driver


    #def _init_(self, driver):
           # super()._init_(driver)
            #self.driver = driver

    def setUserName(self, username):
        try:
            return self.wait_presence_of_element_located(By.ID,self.textbox_username_id).send_keys(username)
        except:
            print("Enter valid Username")

    def setPassword(self, password):
        try:
            return self.wait_presence_of_element_located(By.ID, self.textbox_password_id).send_keys(password)
        except:
            print("Enter valid Password")

    def clickLogin(self):

        return self.wait_presence_of_element_located(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
       # self.driver.find_element(By.XPATH, self.link_logout_class).click()
        return self.wait_presence_of_element_located(By.XPATH, self.link_logout_class).click()

    def login_page_credentials(self, username, password):
        print("username:",username)
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()




