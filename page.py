from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import sys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BasePage(object):

    # driver = webdriver.Chrome(executable_path='C:/drivers_selenium/chromedriver.exe')
    download_dir = "C:/Users/DA063101/PycharmProjects/BHMG/bills"
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        "plugins.plugins_list": [{"enabled": False,
                                  "name": "Chrome PDF Viewer"}],
        "download": {
            "prompt_for_download": False,
            "default_directory": download_dir
        }
    })
    chrome_options.add_argument("--kiosk-printing")
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['version'] = "10"
    driver =webdriver.Chrome(executable_path='C:/drivers_selenium/chromedriver.exe', chrome_options=chrome_options)
    # driver = webdriver.Firefox(executable_path='C:/drivers_selenium/geckodriver.exe', desired_capabilities={'browserName': 'firefox'})
    # driver = webdriver.Remote(command_executor=' http://10.182.240.157:5555/wd/hub',desired_capabilities={'browserName': 'firefox'})
    before = os.listdir(download_dir)

    def setup(self):
        self.driver.get('https://www.treasury.pncbank.com/idp/esec/login.ht')
        self.driver.maximize_window()
        window_before = self.driver.window_handles[0]
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.close()

    def is_title(self, page_title):
        return page_title in self.driver.title

    def click_button(self, button_locator):
        # self.driver.implicitly_wait(30)
        link = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(button_locator))
        link.click()

    def type_value(self, field_locator, value):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(field_locator))
        element.clear()
        element.send_keys(value)

    def select_dropdown(self, param, ident, value):
        menu = Select(self.driver.find_element(param, ident))
        menu.select_by_value(value)

    def logout(self):
        logout_link = self.driver.find_element_by_xpath('//*[@id="LOUT"]')
        logout_link.click()
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/header/div[3]/div[1]/div/div/div[3]/a').click()"""

    def verify_download(self):
        # before = os.listdir(self.download_dir)
        flag = 0
        while flag == 0:
            after = os.listdir(self.download_dir)
            change = set(after) - set(self.before)
            if len(change) == 1:
                file_name = change.pop()
                ext = file_name.split('.')
                if len(ext) == 1 and ext[0] == 'pdf':
                    flag = 1
                    print(file_name + "download success")
                    sys.exit()
            else:
                # print(len(change))
                time.sleep(2)
                print("not")
                flag = 0

    def get_text(self, identifier, value):
        label = self.driver.find_element(identifier, value).text
        return label

    def find_element_presence(self, identifier, value):
        ele = self.driver.find_element(identifier, value)
        return ele

    def find_elements_presence(self, identifier, value):
        ele = self.driver.find_elements(identifier, value)
        return ele





