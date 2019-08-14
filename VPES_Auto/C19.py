import Default_Setting
from selenium.webdriver.support.ui import Select
import unittest, time


# TestRail run_id, Testcase_id, Message 정보
# case_id = 19

class C19(unittest.TestCase):
    def test_C19(self):
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
        p.driver.find_element_by_id("CSCIName").send_keys("Directory")
        p.driver.find_element_by_id("projectCheck").click()
        time.sleep(3)
        p.driver.find_element_by_id("btnState").click()
        time.sleep(2)
        p.driver.find_element_by_id("successBtn").click()
        assert "Selenium" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[2]").text
        assert "Directory" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[3]").text
        time.sleep(3)

# TestRail 결과 입력
    # try :
    #     assert "Selenium" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[2]").text
#         assert "Directory" in p.driver.find_element_by_xpath("//tbody[@id='projectStateList']/tr/td[3]").text
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