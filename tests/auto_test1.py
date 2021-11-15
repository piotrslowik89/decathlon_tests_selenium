import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time, sys


class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized");
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        self.base_url = ('https://www.decathlon.pl/')
        self.driver = webdriver.Chrome(executable_path=r"/usr/local/share/chromedriver")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    def test_go(self):
        driver=self.driver
        driver.get(self.base_url)
        from selenium.webdriver.common.keys import Keys

        # finding search bar

        search_bar=driver.find_element_by_xpath('//*[@id="search-bar"]/div/form/input')

        search_bar.send_keys("czapka",Keys.ENTER)

        # driver.execute_script("window.scrollTo(0, 1080)")
        # time.sleep(3)
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)
        # time.sleep(3)
        # html.send_keys(Keys.PAGE_DOWN)
        # time.sleep(3)
        # html.send_keys(Keys.PAGE_DOWN)
        # time.sleep(3)
        # html.send_keys(Keys.PAGE_DOWN)
        # time.sleep(3)
        # html.send_keys(Keys.PAGE_DOWN)
        # time.sleep(3)


        blue_cap = driver.find_element_by_xpath('//a[@href="/p/czapka-narciarska-dla-doroslych-wedze-firstheat/_/R-p-165131"]')
        # href="/p/czapka-narciarska-dla-dzieci-wedze-flap/_/R-p-332202?mc=8642494"
        blue_cap.click()


        time.sleep(4)

        # adding to cart

        add_to_cart= driver.find_element_by_xpath('//*[@id="fitAnalytics-pdp-add-to-cart"]').click()

        time.sleep(4)

        go_to_cart =driver.find_element_by_xpath('//*[@id="ab-prebasket-container"]/div[3]/a').click()

        # go to go to delivery

        go_to_delivery = driver.find_element_by_xpath('//*[@id="cart-summary__snrs"]/div/footer/button').click()