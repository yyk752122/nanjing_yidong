import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MassagePage(BaseAction):
    # 点击加号
    new_massage_button = By.ID, 'com.android.mms:id/action_compose_new'

    # 点击加号
    @allure.step(title='点击新建短信')
    def click_new_massage(self):
        self.click(self.new_massage_button)
