from Default_Setting import *
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

# TestRail run_id, Testcase_id, Message 정보
# case_id = 18

class C18(unittest.TestCase):
    def test_C18(self):
        p: default = default()
        p.setUp()
        p.test_project_init()
        p.driver.find_element_by_id("projectCreate").click()
        time.sleep(2)
        p.driver.find_element_by_id("scmType").click()
        Select(p.driver.find_element_by_id("scmType")).select_by_visible_text("GIT") # 드롭타운 선택
        p.driver.find_element_by_id("scmType").click()
        p.driver.find_element_by_id("scmUrl").click()
        p.driver.find_element_by_id("scmUrl").clear()
        p.driver.find_element_by_id("scmUrl").send_keys(scm_git)
        p.driver.find_element_by_id("BusinessName").click()
        p.driver.find_element_by_id("BusinessName").clear()
        p.driver.find_element_by_id("BusinessName").send_keys("Selenium")
        p.driver.find_element_by_id("CSCIName").click()
        p.driver.find_element_by_id("CSCIName").clear()
        p.driver.find_element_by_id("CSCIName").send_keys("Git")
        p.driver.find_element_by_id("projectCheck").click()
        time.sleep(3)
        p.driver.find_element_by_id("btnState").click()
        time.sleep(2)
        p.driver.find_element_by_id("successBtn").click()
        assert "Selenium" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[2]").text
        assert "Git" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[3]").text
        time.sleep(3)
        p.tearDown()


# TestRail 결과 입력
        # try :
        #     assert "Selenium" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[2]").text
        #     assert "Git" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[3]").text
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
if __name__ == "__main__":
    unittest.main()