from LoginPage import LoginPage
from Dashboard import Dashboard
from rename import Rename
from AccountPage import AccountPage


class PageFactory(object):
    @staticmethod
    def get_object(page_name):
        page_obj = None
        page_name = page_name.lower()
        if page_name == "loginpage":
            page_obj = LoginPage()
        elif page_name == "rename":
            page_obj = Rename()
        elif page_name == "dashboard":
            page_obj = Dashboard()
        elif page_name == "accountpage":
            page_obj = AccountPage()
        return page_obj
