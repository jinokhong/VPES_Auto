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
# case_id = 11029
# passMsg = 'Test Run Success !!'
# failMsg = 'Test Run Fail !!'

usr = "qscroll"
pwd = "sure"

class C11029(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_C11029(self):
        driver = self.driver
        driver.get("http://211.116.223.191:18080/vpes")  # VPES 서버 진입
        driver.find_element_by_id("username").send_keys(usr)  # 로그인
        driver.find_element_by_id("pwd").send_keys(pwd)
        driver.find_element_by_id("pwd").send_keys(Keys.RETURN)
        driver.find_element_by_link_text("설정").click()
        driver.find_element_by_id("licenseSetting-tab").click()
        time.sleep(2)
        self.assertEqual(driver.find_element_by_id("VersionLabel").text, "VPES 버전")
        self.assertEqual(driver.find_element_by_id("MacLabel").text, "서버물리주소")
        self.assertEqual(driver.find_element_by_id("typeLabel").text, "라이센스 종류")
        self.assertEqual(driver.find_element_by_id("StartDayLabel").text, "사용 시작 날짜")
        self.assertEqual(driver.find_element_by_id("endDayLabel").text, "사용 종료 날짜")
        self.assertEqual(driver.find_element_by_id("totalProjectLabel").text, "총 프로젝트 수")
        self.assertEqual(driver.find_element_by_id("MaxProjectLabel").text, "최대 활성 프로젝트 수")

    # TestRail 결과 입력
    # try :
    #     self.assertEqual(driver.find_element_by_id("VersionLabel").text, "VPES 버전")
    #     self.assertEqual(driver.find_element_by_id("MacLabel").text, "서버물리주소")
    #     self.assertEqual(driver.find_element_by_id("typeLabel").text, "라이센스 종류")
    #     self.assertEqual(driver.find_element_by_id("StartDayLabel").text, "사용 시작 날짜")
    #     self.assertEqual(driver.find_element_by_id("endDayLabel").text, "사용 종료 날짜")
    #     self.assertEqual(driver.find_element_by_id("totalProjectLabel").text, "총 프로젝트 수")
    #     self.assertEqual(driver.find_element_by_id("MaxProjectLabel").text, "최대 활성 프로젝트 수")
    #     status_id = 1
    # except :
    #     status_id = 5
    #
    # client.send_post(
    #     'add_result_for_case/%s/%s' % (run_id, case_id),
    #     {'status_id': status_id, 'comment': msg,})
    # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))

    # Test Rail 결과 메세지 입력
    # if status_id == 1:
    #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, passMsg))
    #     client.send_post(
    #         'add_result_for_case/%s/%s' % (run_id, case_id),
    #         {'status_id': status_id, 'comment': passMsg, })
    #
    # elif status_id == 5:
    #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, failMsg))
    #     client.send_post(
    #         'add_result_for_case/%s/%s' % (run_id, case_id),
    #         {'status_id': status_id, 'comment': failMsg, })


