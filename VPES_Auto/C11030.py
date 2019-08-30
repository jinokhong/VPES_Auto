import Default_Setting
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time
import os

# TestRail module.run_id, Testcase_id, Message 정보
case_id = 11030

LicensePath = "\KEY-SQA_유효기간_만료_70-85-C2-5E-1E-5E.license"

class C11030(unittest.TestCase):
    def test_C11030(self):
        try:
            module = Default_Setting
            p = Default_Setting.default()
            p.setUp()
            p.test_project_init()
            p.driver.find_element_by_link_text("설정").click()
            p.driver.find_element_by_id("licenseSetting-tab").click()
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
            p.driver.find_element_by_name("uploadfile").send_keys(FullPath)
            time.sleep(2)
            p.driver.find_element_by_id("btn-license").click()
            try:
                element = WebDriverWait(p.driver, 60).until(
                    EC.visibility_of_element_located((By.ID, "modal-content"))
                )
            except TimeoutException:
                print("타임아웃")
            assert "라이센스 파일이 유효하지 않습니다." in p.driver.find_element_by_id("modal-content").text
            time.sleep(2)
            self.assertEqual(p.driver.find_element_by_id("endDayError").text, "사용기간 만료")
            self.assertEqual(p.driver.find_element_by_id("endDayError").value_of_css_property('color'), "rgba(255, 0, 0, 1)")
            status_id = 1
        except :
            status_id = 5

# Test Rail 결과 메세지 입력
        if status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (module.run_id, case_id, module.passMsg))
            module.client.send_post(
                'add_result_for_case/%s/%s' % (module.run_id, case_id),
                {'status_id': status_id, 'comment': module.passMsg })

        elif status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (module.run_id, case_id, module.failMsg))
            module.client.send_post(
                'add_result_for_case/%s/%s' % (module.run_id, case_id),
                {'status_id': status_id, 'comment': module.failMsg })


if __name__ == "__main__":
    unittest.main()