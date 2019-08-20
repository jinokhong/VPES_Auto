import Default_Setting
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time
import os
# TestRail module.run_id, Testmodule.case_id, Message 정보
# case_id = 11032

LicensePath = "\KEY-SQA_유효기간_만료_70-85-C2-5E-1E-5E.license"

class C11032(unittest.TestCase):
    def test_C11032(self):
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
        time.sleep(2)
        p.driver.find_element_by_link_text("프로젝트 조회").click()
        try:
            element = WebDriverWait(p.driver, 60).until(
                EC.visibility_of_element_located((By.ID, "licenceValidMsg"))
           )
        except TimeoutException:
            time.sleep(2)
            self.assertEqual(p.driver.find_element_by_id("licenceValidMsg").text, "상세내용 : 라이센스 기간만료!")
            p.driver.find_element_by_class_name("close").click()
            time.sleep(2)
            self.assertEqual("Verification / Validation Process Execution System\n전체현황", p.driver.find_element_by_css_selector("h2").text)
# TestRail 결과 입력
        # try :
        #     p.driver.find_element_by_xpath("//*[@onclick='licenceValid('VALID_DATE_OVER')']").click()
        #     time.sleep(1)
        #     self.assertEqual(p.driver.find_element_by_id("licenceValidMsg").text, "상세내용 : 라이센스 기간만료!")
        #     module.status_id = 1
        # except :
        #     module.status_id = 5
        #
        # module.client.send_post(
        #     'add_result_for_case/%s/%s' % (module.run_id, module.case_id),
        #     {'module.status_id': module.status_id, 'comment': msg,})
        # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (module.run_id, module.case_id, msg))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()