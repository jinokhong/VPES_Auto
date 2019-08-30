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
client = APIClient('http://211.116.223.42/testrail')
client.user = 'johong@suresofttech.com'
client.password = '12345'

# TestRail module.run_id, Testcase_id, Message 정보
run_id = 372
case_id = 11120
passMsg = 'Test Run Success !!'
failMsg = 'Test Run Fail !!'

class C11120(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_C11120(self):
        try:
            driver = self.driver
            driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
            driver.find_element_by_id("signUp").click()
            self.assertEqual(driver.find_element_by_id("wrongId").text, "")
            self.assertEqual(driver.find_element_by_id("wrongPassword").text, "")
            time.sleep(2)
            status_id = 1
        except :
            status_id = 5

    # Test Rail 결과 메세지 입력
        if status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, passMsg))
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': passMsg })

        elif status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, failMsg))
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': failMsg })

if __name__ == "__main__":
    unittest.main()