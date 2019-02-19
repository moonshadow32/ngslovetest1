# -*- coding: utf-8 -*-



import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class NgsLoveSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/user/drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(20)

    def test_search(self):
        driver = self.driver
        driver.get("https://love.ngs.ru")
        assert u"Бесплатный сайт знакомств в Новосибирске - НГС Знакомства" in driver.title
        person = driver.find_element_by_css_selector("#lv-page-wrap > div.lv-content-wrap > div.lv-main-menu__submenu.search > form > div.lv-search__first-string > div.lv-search__sex > div > ul > li.lv-segment-ctrl__segment.lv-segment-ctrl__segment_last > label")
        person.click()
        from_age = driver.find_element_by_id("from-age")
        from_age.send_keys(Keys.CONTROL, "a")
        from_age.send_keys(Keys.DELETE)
        from_age.send_keys("18")
        to_age = driver.find_element_by_id("to-age")
        to_age.send_keys(Keys.CONTROL, "a")
        to_age.send_keys(Keys.DELETE)
        to_age.send_keys("30")
        city = driver.find_element_by_id("autocompleteCity")
        city.click()
        city.send_keys(Keys.DELETE)
        city.send_keys(u'Новосибирск')
        time.sleep(1)
        city.send_keys(Keys.ARROW_DOWN)
        city.send_keys(Keys.RETURN)
        online = driver.find_element_by_css_selector("#lv-page-wrap > div.lv-content-wrap > div.lv-main-menu__submenu.search > form > label:nth-child(6)")
        online.click()
        photo = driver.find_element_by_css_selector("#lv-page-wrap > div.lv-content-wrap > div.lv-main-menu__submenu.search > form > label:nth-child(4)")
        photo.click()
        button_login = driver.find_element_by_css_selector("#lv-page-wrap > div.lv-content-wrap > div.lv-main-menu__submenu.search > form > div.lv-search__first-string > input.lv-search__submit.custom-btn")
        button_login.click()
        assert u"Найденные люди" in driver.page_source




    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()