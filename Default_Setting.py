from testrail import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


usr = "qscroll"
pwd = "sure"
scm_git = "http://qatest@192.168.0.136:7990/scm/qat/server191.git"
scm_svn = "https://qa-server/VPES_Source"
scm_dir = "miro"

class default(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_project_init(self):
        driver = self.driver
        driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
        driver.find_element_by_id("username").send_keys(usr) # 로그인
        driver.find_element_by_id("pwd").send_keys(pwd)
        driver.find_element_by_id("pwd").send_keys(Keys.RETURN)

        try:
            while 1 :
                # 프로젝트 반복 삭제
                driver.find_element_by_class_name("caret").click()
                driver.find_element_by_link_text("삭제").click()
                time.sleep(1)
                driver.find_element_by_id("deleteY").click()
                time.sleep(4)


        except NoSuchElementException: # 엘리먼트 없으면 VPES 메인 페이지로 이동 클릭
            driver.find_element_by_xpath("//*[@id='leftWrap']/h1/a/img").click()
        time.sleep(5)

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()