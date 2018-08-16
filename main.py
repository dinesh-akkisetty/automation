from PageFactory import PageFactory
# from PaymentsPage import PaymentsPage
import time
import unittest


class Driver(object):
    fp = open('credentials.txt', 'r')
    operator, username, password = fp.read().split(',')
    login_page = PageFactory.get_object('loginpage')
    login_page.setup()
    time.sleep(5)
    login_page.login(operator, username, password)
    time.sleep(10)
    Dashboard_page = PageFactory.get_object('dashboard')
    Dashboard_page.select_account()
    time.sleep(5)
    Account_page = PageFactory.get_object('accountpage')
    Account_page.select_account()
    rename_obj = PageFactory.get_object('rename')
    rename_obj.rename()
    time.sleep(3)
    login_page.logout()
