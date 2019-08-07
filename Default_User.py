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

# TestRail 접속 정보
# client = APIClient('http://211.116.223.42/testrail')
# client.user = 'johong@suresofttech.com'
# client.password = '12345'
# passMsg = 'Test Run Success !!'
# failMsg = 'Test Run Fail !!'
# run_id = 240

usr = "qscroll"
pwd = "sure"

class default_user(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_user_init(self):

        driver = self.driver
        driver.get("http://211.116.223.191:18080/vpes") # VPES 서버 진입
        driver.find_element_by_id("username").send_keys(usr) # 로그인
        driver.find_element_by_id("pwd").send_keys(pwd)
        driver.find_element_by_id("pwd").send_keys(Keys.RETURN)
        driver.find_element_by_link_text("설정").click()
        driver.find_element_by_id("userManagement-tab").click()
        time.sleep(2)

        try:
            while 1 :
                # admin 계정을 제외한 모든 계정 삭제
                driver.find_element_by_xpath("(//span[@id='userDelete'])[2]").click()
                time.sleep(1)
                driver.find_element_by_id("deleteY").click()
                time.sleep(4)
        except NoSuchElementException: # 엘리먼트 없으면 VPES 메인 페이지로 이동 클릭
           driver.find_element_by_link_text("로그아웃").click()
        time.sleep(5)

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()