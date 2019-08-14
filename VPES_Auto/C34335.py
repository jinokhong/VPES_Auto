import Default_Setting
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time
import os

# TestRail run_id, Testcase_id, Message 정보
# case_id = 34335

fPath = "\SN_GIT_POP.xml"

class C34335(unittest.TestCase):
    def test_C34335(self):
        module = Default_Setting
        p = Default_Setting.default()
        p.setUp()
        p.test_project_init()
        p.driver.find_element_by_id("projectCreate").click()
        time.sleep(2)
        p.driver.find_element_by_id("scmType").click()
        Select(p.driver.find_element_by_id("scmType")).select_by_visible_text("GIT") # 드롭타운 선택
        p.driver.find_element_by_id("scmType").click()
        p.driver.find_element_by_id("scmUrl").click()
        p.driver.find_element_by_id("scmUrl").clear()
        p.driver.find_element_by_id("scmUrl").send_keys(module.scm_git)
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
        # 상위 폴더로 이동
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
        try:
            element = WebDriverWait(p.driver, 60).until(
                EC.visibility_of_element_located((By.ID, "modal-content"))
            )
        except TimeoutException:
            print("타임아웃")
        assert "업로드 되었습니다." in p.driver.find_element_by_id("modal-content").text
        time.sleep(2)
        self.assertEqual(p.driver.find_element_by_class_name("btn.btn-success").is_displayed(),True)
        # p.tearDown()


# TestRail 결과 입력
        # try :
        #     self.assertEqual(p.driver.find_element_by_class_name("btn.btn-success").is_displayed(),True)
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