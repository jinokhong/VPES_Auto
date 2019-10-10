import Default_User
from selenium.common.exceptions import NoSuchElementException
import unittest, time


# 1.6 기준 이슈 있음(이름 입력하지 않아도 회원가입 버튼 활성화됨)

# TestRail module.run_id, Testcase_id, Message 정보
case_id = 11124

class C11124(unittest.TestCase):
    def test_C11124(self):
        try:
            module = Default_User
            p = Default_User.default_user()
            p.setUp()
            p.test_user_init()
            p.driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
            p.driver.find_element_by_id("signUp").click()
            p.driver.find_element_by_id("id").clear()
            p.driver.find_element_by_id("id").send_keys("Test")
            p.driver.find_element_by_id("password").clear()
            p.driver.find_element_by_id("password").send_keys("wowkw5629!@")
            p.driver.find_element_by_id("surePassword").clear()
            p.driver.find_element_by_id("surePassword").send_keys("wowkw5629!@")
            time.sleep(1)
            self.assertEqual(p.driver.find_element_by_id("btnContactUs").is_enabled(), False)
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