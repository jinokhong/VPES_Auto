from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from testrail import *

# TestRail 접속 정보
# client = APIClient('http://211.116.223.42/testrail')
# client.user = 'johong@suresofttech.com'
# client.password = '12345'

# TestRail run_id, Testcase_id, Message 정보
# run_id = 240
# case_id = 11111
# msg = 'Test Auto Checking'

class C11112(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_C11111(self):
        driver = self.driver
        driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
        driver.find_element_by_id("signUp").click()
        driver.find_element_by_id("id").clear()
        driver.find_element_by_id("id").send_keys("qscroll")
        elem = driver.find_element_by_id("wrongId")
        print(elem.value_of_css_property('color'))
        self.assertEqual(elem.value_of_css_property('color'), "rgba(255, 0, 0, 1)")
        self.assertEqual(driver.find_element_by_id("wrongId").text, "아이디가 이미 존재합니다.")
        time.sleep(2)
    # TestRail 결과 입력
    # try :
    #     self.assertEqual(elem.value_of_css_property('color'), "rgba(255, 0, 0, 1)")
    #     self.assertEqual(driver.find_element_by_id("wrongId").text, "아이디가 이미 존재합니다.")
    #     status_id = 1
    # except :
    #     status_id = 5
    #
    # client.send_post(
    #     'add_result_for_case/%s/%s' % (run_id, case_id),
    #     {'status_id': status_id, 'comment': msg,})
    # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))



