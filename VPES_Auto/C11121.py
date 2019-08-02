from Default_User import *
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
# case_id = 11121
# msg = 'Test Auto Checking'

class C11121(unittest.TestCase):
    def test_C11121(self):
        p: default_user = default_user()
        p.setUp()
        p.test_user_init()
        p.driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
        p.driver.find_element_by_id("signUp").click()
        p.driver.find_element_by_id("id").clear()
        p.driver.find_element_by_id("id").send_keys("한글")
        self.assertEqual(p.driver.find_element_by_id("wrongId").text, "아이디에 한글 또는 특수문자가 포함되어 있습니다.")
        p.driver.find_element_by_id("password").clear()
        p.driver.find_element_by_id("password").send_keys("wowkw5629!@")
        p.driver.find_element_by_id("surePassword").clear()
        p.driver.find_element_by_id("surePassword").send_keys("wowkw5629!@")
        p.driver.find_element_by_id("name").clear()
        p.driver.find_element_by_id("name").send_keys("한글")
        p.driver.find_element_by_id("btnContactUs").click()
        time.sleep(1)
        self.assertEqual(p.driver.find_element_by_id("btnContactUs").is_enabled(), False)
        time.sleep(2)
    # TestRail 결과 입력
    # try :
    #     self.assertEqual(element.is_enabled(),False)
    #     status_id = 1
    # except :
    #     status_id = 5
    #
    # client.send_post(
    #     'add_result_for_case/%s/%s' % (run_id, case_id),
    #     {'status_id': status_id, 'comment': msg,})
    # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))



