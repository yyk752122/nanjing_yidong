import time

import pytest

from base.analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestMassage:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # @pytest.mark.parametrize(("phone","content"),[('18888888888','hello'),('13333333333','nihao')])
    @pytest.mark.parametrize("agse", analyze_file('send_massage.yaml', 'test_send_massage'))
    def test_send_massage(self,agse):
        phone = agse['phone']
        content = agse["content"]

        # 点击新建短信
        self.page.massage_list.click_new_massage()
        # 点击输入联系人
        self.page.newmassage.input_text(phone)
        # 点击输入内容
        self.page.newmassage.inout_texts(content)
        # 点击发送
        self.page.newmassage.click_send()
