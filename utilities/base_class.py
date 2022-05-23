import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseFunc():
    def __init__(self, driver):
        self.driver = driver

    def wait_presence_of_element_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((id_type, ele_id)))

    def wait_presence_of_all_elements_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_all_elements_located((id_type, ele_id)))

    def mouse_actions(self,element):
        ## Mouse Hover
        action=ActionChains(self.driver)
        return action.move_to_element(element).click().perform()

    def get_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(locator))

    def select_by_text(self,locator,option):
        select=Select(self.get_element(locator))
        select.select_by_visible_text(option)

    def alert_is_present(self):

        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.alertIsPresent())

