from page.massage_list_page import MassagePage
from page.new_massage_page import NewMassage


class Page:
    def __init__(self,driver):
        self.driver=driver
    @property
    def massage_list(self):
        return MassagePage(self.driver)
    @property
    def newmassage(self):
        return NewMassage(self.driver)
