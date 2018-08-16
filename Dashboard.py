from page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dashboard(BasePage):

    account_link = (By.ID, 'ARS')

    def select_account(self):
        self.click_button(self.account_link)