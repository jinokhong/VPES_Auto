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
# passMsg = 'Test Run Success !!'
# failMsg = 'Test Run Fail !!'

class C11125(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_C11125(self):
        driver = self.driver
        driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
        driver.find_element_by_id("signUp").click()
        list = ["`","~","!","@","#","$","%","^","&","*","(",")","-","=","_","+","[","]","{","}",";","'",":",'"',",",".","?","<",">","/"]

        try :
            for num in list: # list를 받아와서 첫번째부터 한글자씩 num으로 넘겨준다
                driver.find_element_by_id("id").clear()
                driver.find_element_by_id("id").send_keys(num)
                time.sleep(10)
                elem = driver.find_element_by_id("wrongId")
                print(elem.value_of_css_property('color'))
                self.assertEqual(elem.value_of_css_property('color'), "rgba(255, 0, 0, 1)")
                self.assertEqual(driver.find_element_by_id("wrongId").text, "아이디에 한글 또는 특수문자가 포함되어 있습니다.")
        except NoSuchElementException:  # 엘리먼트 없으면 id입력창에 테스트 성공 입력
            driver.find_element_by_id("id").clear()
            driver.find_element_by_id("id").send_keys("테스트 성공")
        time.sleep(2)
        
    # TestRail 결과 입력
    # try :
    #     self.assertEqual(driver.find_element_by_id("id").text, "테스트 성공")
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

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()