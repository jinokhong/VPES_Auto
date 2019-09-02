import Default_Setting
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time


# TestRail module.run_id, Testcase_id, Message 정보
case_id = 47029


class C47029(unittest.TestCase):
    def test_C47029(self):
        try:
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
            p.driver.find_element_by_id("scmUrl").send_keys("http://qatest@192.168.0.136:7990/scm/qat/server191.git1")
            time.sleep(2)
            assert "사용자 정보 또는 유효하지 않은 Url입니다." in p.driver.find_element_by_id("URLstate").text
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

#if __name__ == "__main__":
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(C17(methodName='test_C17'))


