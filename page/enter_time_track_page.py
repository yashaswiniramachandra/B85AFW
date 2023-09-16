from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class EnterTimeTrackPage:
    __logout = (By.ID, "logoutLink")

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(*self.__logout).click()

    def verify_home_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__logout))
            print("Home Page is displayed")
            return True
        except:
            print("Home Page is NOT displayed")
            return False
