import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMassage(BaseAction):
    # 输入联系人
    input_person_text = By.ID, 'com.android.mms:id/recipients_editor'
    # 输入内容
    # input_texts = By.ID, 'com.android.mms:id/embedded_text_editor'
    input_texts = By.XPATH, "//*[contains(@text,'入信息')]"
    # 点击发送
    send_button = By.XPATH, '//*[@content-desc="发送"]'

    @allure.step(title='点击输入收件人电话')
    def input_text(self, text):
        self.send_keys(self.input_person_text, text)

    @allure.step(title='点击输入短信内容')
    def inout_texts(self, texts):
        self.send_keys(self.input_texts, texts)

    @allure.step(title='点击发送短信')
    def click_send(self):
        self.click(self.send_button)
