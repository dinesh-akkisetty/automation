from page import BasePage
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta


class AccountPage(BasePage):

    date_title = '/html/body/table/tbody/tr['
    dashboard_path = '//*[@id="ARS"]'
    title_path = '//*[@id="title"]'
    batch_index_path = (By.XPATH, '//*[@id="navbar"]/ul/li/a')

    def select_summary_link(self):
        found = 0
        temp = 2
        while found == 0:
            date_path = '/html/body/table/tbody/tr['+str(temp)+']/td[1]'
            print temp
            date_label = self.find_element_presence(By.XPATH, date_path).text
            day = (datetime.now()).strftime("%W")
            # day = 'saturday'
            if day.lower() == 'sunday':
                target_date = (datetime.now() - timedelta(3)).strftime("%m/%d/%Y")
            elif day.lower() == 'saturday':
                target_date = (datetime.now() - timedelta(2)).strftime("%m/%d/%Y")
            else:
                target_date = (datetime.now()).strftime("%m/%d/%Y")
            time.sleep(2)
            # target_date = '08/04/2018'
            print date_label
            print target_date
            if target_date == date_label:
                link_path = '/html/body/table/tbody/tr['+str(temp)+']//td[2]/a'
                summary_link = self.find_element_presence(By.XPATH, link_path)
                summary_link.click()
                found = 1
            else:
                temp = temp + 1

    """def select_check(self):
        index_link = self.find_element_presence(By.XPATH, self.check_path)
        index_link.click()"""

    def print_batch(self):
        print_links = self.find_elements_presence(By.PARTIAL_LINK_TEXT, 'Printable Batch PDF')
        no_of_links = len(print_links)
        print no_of_links
        for i in range(0, no_of_links):
            print 'link-'+str(i)
            print_links[i].click()
            time.sleep(5)
            window_before = self.driver.window_handles[0]
            window_after = self.driver.window_handles[1]
            self.driver.switch_to.window(window_after)
            time.sleep(5)
            pdf_links = self.find_elements_presence(By.PARTIAL_LINK_TEXT, 'PDF')
            for j in range(0, len(pdf_links)):
                print 'pdf'+str(j)
                time.sleep(2)
                pdf_links[j].click()
                time.sleep(5)
            time.sleep(5)
            self.driver.close()
            time.sleep(1)
            self.driver.switch_to.window(window_before)
            self.driver.switch_to.frame('contentIframe')

    def go_to_batch_index(self):
        self.click_button(self.batch_index_path)

    def select_source(self):
        rows = self.driver.find_elements_by_xpath('/html/body/table[1]/tbody/tr')
        no_of_rows = len(rows)
        for r in range(1, no_of_rows):
            mode_title_path = '/html/body/table[1]/tbody/tr['+str(r+1)+']/td[1]'
            mode_title = self.find_element_presence(By.XPATH, mode_title_path).text
            if 'edi' not in mode_title.lower():
                mode_link = '/html/body/table[1]/tbody/tr['+str(r+1)+']/td[2]/a'
                self.find_element_presence(By.XPATH, mode_link).click()
                time.sleep(5)
                self.print_batch()
                time.sleep(2)
                self.go_to_batch_index()

    def go_to_dashboard(self):
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dashboard_path).click()
        time.sleep(5)

    def select_account(self):
        self.driver.switch_to.frame('contentIframe')
        account_links = self.find_elements_presence(By.PARTIAL_LINK_TEXT, 'PHL-')
        no_of_account_links = len(account_links)
        for k in range(0, no_of_account_links):
            if k > 0:
                self.driver.switch_to.frame('contentIframe')
                account_links = self.find_elements_presence(By.PARTIAL_LINK_TEXT, 'PHL-')
            print 'account'+str(k)
            account_links[k].click()
            self.select_summary_link()
            self.select_source()
            self.go_to_dashboard()
















