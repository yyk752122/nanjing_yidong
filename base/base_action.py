from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=20, poll=1):
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        # return self.driver.find_element(feature_by, feature_value)
        return element

    def click(self, feature,timeout=10, poll=1):
        self.find_element(feature,timeout,poll).click()

    def send_keys(self, feature, keys):
        self.find_element(feature).send_keys(keys)

    def clear(self, farture):
        self.find_element(farture).clear()
