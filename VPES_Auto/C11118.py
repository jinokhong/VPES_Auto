from Default_User import *
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
# case_id = 11118

class C11118(unittest.TestCase):
    def test_C11118(self):
        i: default = default() # 프로젝트 초기화
        i.setUp()
        i.test_project_init()
        i.driver.quit()
        p: default_user = default_user() # qscroll을 제외한 사용자 삭제
        p.setUp()
        p.test_user_init()
        p.driver.get("http://211.116.223.190:18080/vpes")  # VPES 서버 진입
        p.driver.find_element_by_id("username").send_keys(usr)  # 로그인
        p.driver.find_element_by_id("pwd").send_keys(pwd)
        p.driver.find_element_by_id("pwd").send_keys(Keys.RETURN)
        p.driver.find_element_by_link_text("전체현황").click()
        p.driver.find_element_by_id("projectCreate").click()
        time.sleep(2)
        p.driver.find_element_by_id("scmType").click()
        Select(p.driver.find_element_by_id("scmType")).select_by_visible_text("GIT")  # SCM 설정 드롭 박스 선택
        p.driver.find_element_by_id("scmType").click()
        p.driver.find_element_by_id("scmUrl").click()
        p.driver.find_element_by_id("scmUrl").clear()
        p.driver.find_element_by_id("scmUrl").send_keys(scm_git)
        p.driver.find_element_by_id("BusinessName").click()
        p.driver.find_element_by_id("BusinessName").clear()
        p.driver.find_element_by_id("BusinessName").send_keys("Test_11118")
        p.driver.find_element_by_id("CSCIName").click()
        p.driver.find_element_by_id("CSCIName").clear()
        p.driver.find_element_by_id("CSCIName").send_keys("GIT")
        p.driver.find_element_by_id("projectCheck").click()
        time.sleep(3)
        p.driver.find_element_by_id("btnState").click()
        time.sleep(2)
        p.driver.find_element_by_id("successBtn").click()
        time.sleep(2)
        p.driver.find_element_by_link_text("로그아웃").click()
        p.driver.find_element_by_id("signUp").click()
        time.sleep(2)
        p.driver.find_element_by_tag_name("b").click()
        time.sleep(2)
        p.driver.find_element_by_xpath("//*[@data-option-array-index='1']").click()
        time.sleep(2)
        assert "Test_11118" in p.driver.find_element_by_xpath("//tbody[@id='my-tbody']/tr/td").text
        assert "GIT" in p.driver.find_element_by_xpath("//tbody[@id='my-tbody']/tr/td[2]").text

    # TestRail 결과 입력
    # try :
    #     assert "Test_11118" in p.driver.find_element_by_xpath("//tbody[@id='my-tbody']/tr/td").text
    #     assert "GIT" in p.driver.find_element_by_xpath("//tbody[@id='my-tbody']/tr/td[2]").text
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

