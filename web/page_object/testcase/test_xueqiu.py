from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.page_object.page.MainPage import MainPage


class TestXueqiu(object):
    def setup(self):
        #remote就是远程的意思，连本地不能用remote
        self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.main=MainPage(self.driver)

    def test_search(self):
        self.main.search("alibaba").follow("1688")
        #todo: add assertion

    def teardown(self):
        sleep(60)
        self.driver.quit()