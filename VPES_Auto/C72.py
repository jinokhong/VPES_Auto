import Default_Setting
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time
import os
# TestRail run_id, Testcase_id, Message 정보
# case_id = 72

fPath = "\SN_SCM 없음.xml"

class C72(unittest.TestCase):
    def test_C72(self):
        module = Default_Setting
        p = Default_Setting.default()
        p.setUp()
        p.test_project_init()
        p.driver.find_element_by_id("projectCreate").click()
        time.sleep(2)
        p.driver.find_element_by_id("scmType").click()
        Select(p.driver.find_element_by_id("scmType")).select_by_visible_text("DIRECTORY") # 드롭타운 선택
        p.driver.find_element_by_id("scmType").click()
        p.driver.find_element_by_id("scmUrl").click()
        p.driver.find_element_by_id("scmUrl").clear()
        p.driver.find_element_by_id("scmUrl").send_keys(module.scm_dir)
        p.driver.find_element_by_id("BusinessName").click()
        p.driver.find_element_by_id("BusinessName").clear()
        p.driver.find_element_by_id("BusinessName").send_keys("Selenium")
        p.driver.find_element_by_id("CSCIName").click()
        p.driver.find_element_by_id("CSCIName").clear()
        p.driver.find_element_by_id("CSCIName").send_keys("DIR")
        p.driver.find_element_by_id("projectCheck").click()
        time.sleep(3)
        p.driver.find_element_by_id("btnState").click()
        time.sleep(2)
        p.driver.find_element_by_id("successBtn").click()
        p.driver.find_element_by_class_name("caret").click()
        p.driver.find_element_by_link_text("검증 결과 업로드").click()
        time.sleep(2)
        p.driver.find_element_by_id("toolType").click()
        Select(p.driver.find_element_by_id("toolType")).select_by_visible_text("SNIPER")  # 드롭타운 선택
        p.driver.find_element_by_id("toolType").click()
        time.sleep(3)

        # 현재 파일의 폴더 위치 저장
        pathSave = os.path.dirname(os.path.realpath(__file__))
        # 현재 테스트 케이스의 위치로 이동
        os.chdir(pathSave)
        # 데이터 폴더로 이동
        os.chdir('../VPES_Data')
        # 현재 파일의 폴더 위치 저장
        realpath = os.getcwd()

        # 파일 포함 경로 선언
        FullPath = realpath + fPath
        print(FullPath)
        time.sleep(3)
        p.driver.find_element_by_name("uploadfile").send_keys(FullPath)
        time.sleep(3)
        p.driver.find_element_by_id("btn-xml").click()
        time.sleep(2)
        try: # 성공/실패 알림 팝업 뜰때까지 대기
            element = WebDriverWait(p.driver, 60).until(
                EC.visibility_of_element_located((By.ID, "modal-content"))
            )
        except TimeoutException:
            print("타임아웃")
        assert "업로드하는데 실패했습니다." in p.driver.find_element_by_id("modal-content").text
        time.sleep(2)
        self.assertEqual("- 대상 프로젝트{Selenium_DIR} 소스 형상의 업로드 위치를 확인 해 주십시오.\n    프로젝트 경로 : {VPES_PATH 설정 경로}\miro\n\n- SCM 에 미존재 하는 파일 목록\n    D:\테스트 데이터\Stub_timeout.c", p.driver.find_element_by_xpath("//div[@id='uploadResultList']/span[2]").text)
        time.sleep(2)
        self.assertEqual(p.driver.find_element_by_class_name("btn.btn-danger").is_displayed(), True)



# TestRail 결과 입력
        # try :
        #     self.assertEqual(p.driver.find_element_by_class_name("btn.btn-danger").is_displayed(), True)
        #     status_id = 1
        # except :
        #     status_id = 5
        #
        # client.send_post(
        #     'add_result_for_case/%s/%s' % (run_id, case_id),
        #     {'status_id': status_id, 'comment': msg,})
        # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()