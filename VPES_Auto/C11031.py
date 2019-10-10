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
import os

# TestRail 접속 정보
client = APIClient('http://211.116.223.42/testrail')
client.user = 'johong@suresofttech.com'
client.password = '12345'

# TestRail module.run_id, Testcase_id, Message 정보
run_id = 512
case_id = 11031
passMsg = 'Test Run Success !!'
failMsg = 'Test Run Fail !!'

LicensePath = "\KEY-SQA_유효기간_만료_70-85-C2-5E-1E-5E.license"

usr = "qscroll"
pwd = "sure"
class C11031(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_C11031(self):
        try:
            driver = self.driver
            driver.get("http://211.116.223.190:18080/vpes")  # VPES 서버 진입
            driver.find_element_by_id("username").send_keys(usr)  # 로그인
            driver.find_element_by_id("pwd").send_keys(pwd)
            driver.find_element_by_id("pwd").send_keys(Keys.RETURN)
            time.sleep(2)
            driver.find_element_by_link_text("설정").click()
            driver.find_element_by_id("licenseSetting-tab").click()
            time.sleep(2)
            # 현재 파일의 폴더 위치 저장
            pathSave = os.path.dirname(os.path.realpath(__file__))
            # 현재 테스트 케이스의 위치로 이동
            os.chdir(pathSave)
            # 데이터 폴더로 이동
            os.chdir("../VPES_License")
            # 현재 파일의 폴더 위치 저장
            realpath = os.getcwd()

            # 파일 포함 경로 선언
            FullPath = realpath + LicensePath
            print(FullPath)
            time.sleep(2)
            driver.find_element_by_name("uploadfile").send_keys(FullPath)
            time.sleep(2)
            driver.find_element_by_id("btn-license").click()
            try:
                element = WebDriverWait(driver, 90).until(
                    EC.visibility_of_element_located((By.ID, "modal-content"))
                )
            except TimeoutException:
                print("타임아웃")
            assert "라이센스 파일이 유효하지 않습니다." in driver.find_element_by_id("modal-content").text
            time.sleep(4)
            self.assertEqual(driver.find_element_by_id("endDayError").text, "상세내용 : 시스템 시간이 다시 설정됐습니다.\n라이선스가 올바르게 동작하려면, 클라이언트 시스템의 날짜 및 시간이 정확해야 하며 이전 시간으로 다시 설정되지 않아야 합니다.\n자세한 정보와 도움말은 support@suresofttech.com에 문의하십시오.")
            self.assertEqual(driver.find_element_by_id("endDayError").value_of_css_property('color'), "rgba(255, 0, 0, 1)")
            time.sleep(2)
            driver.find_element_by_link_text("전체현황").click()
            time.sleep(3)
            driver.find_element_by_css_selector("button.btn.btnProject.btn_Deflut").click()
            time.sleep(2)
            self.assertEqual(driver.find_element_by_id("licenceValidMsg").text, "상세내용 : 라이센스 기간만료!")
            time.sleep(1)
            status_id = 1
        except NoSuchElementException:
            status_id = 5

        # Test Rail 결과 메세지 입력
        if status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, passMsg))
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': passMsg})

        elif status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, failMsg))
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': failMsg})

if __name__ == "__main__":
    unittest.main()