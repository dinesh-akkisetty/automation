from selenium.webdriver.common.by import By
from page import BasePage
import time


class LoginPage(BasePage):
    user_id = (By.ID, 'txtUserID')
    operator_id =(By.ID, 'txtOperID')
    Password = (By.ID, 'txtPwd')
    login_btn = (By.ID, 'loginFormButton')
    # skip = (By.ID, 'ac')
    # submit_btn = (By.ID, 'ucChallengeUser_btnSubmitAnswer')
    # answer = (By.ID, 'ucChallengeUser_txtAnswer')

    def login(self, username, operatorid, password):
        self.type_value(self.user_id, username)
        #time.sleep(5)
        self.type_value(self.operator_id, operatorid)
        #time
        self.type_value(self.Password, password)
        #time.sleep(5)
        self.click_button(self.login_btn)
        time.sleep(10)
        if 'Security Challenge' in self.driver.title:
            question = self.get_text(By.ID, 'ucChallengeUser_lblChallengeQuestion')
            # label = self.driver.find_element_by_id('challengeQuestionLabelId')
            # question = label.getText()
            if 'car' in question.lower():
                self.type_value(self.answer, 'Lincoln town car')
                self.click_button(self.submit_btn)
            elif 'friend' in question.lower():
                self.type_value(self.answer, 'Nguyen')
                self.click_button(self.submit_btn)
            elif 'concert' in question.lower():
                self.type_value(self.answer, 'Ricki Martin')
                self.click_button(self.submit_btn)
            elif 'food' in question.lower():
                self.type_value(self.answer, 'Italian')
                self.click_button(self.submit_btn)
            elif 'school' in question.lower():
                self.type_value(self.answer, 'Kansas City')
                self.click_button(self.submit_btn)


