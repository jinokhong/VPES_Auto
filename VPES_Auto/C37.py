import Default_Setting
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time


# TestRail module.run_id, Testcase_id, Message 정보
case_id = 37

class C37(unittest.TestCase):
    def test_C37(self):
        try:
            module = Default_Setting
            p = Default_Setting.default()
            p.setUp()
            p.test_project_init()
            p.driver.find_element_by_id("projectCreate").click()
            time.sleep(2)
            p.driver.find_element_by_id("StaticTestSubject").click()
            p.driver.find_element_by_id("ReliabilityTest").click()
            p.driver.find_element_by_id("DynamicTestSubject").click()
            time.sleep(1)
            assert "적어도 1개이상의 시험 대상을 선택해주세요." in p.driver.find_element_by_id("modal-content").text
            status_id = 1
        except NoSuchElementException:
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