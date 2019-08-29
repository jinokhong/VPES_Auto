import Default_User
import unittest, time


# TestRail module.run_id, Testmodule.case_id, Message 정보
case_id = 11111

class C11111(unittest.TestCase):
    def test_C11111(self):
        try:
            module = Default_User
            p = Default_User.default_user()
            p.setUp()
            p.test_user_init()
            p.driver.get("http://211.116.223.191:18080/vpes") # VPES 서버 진입
            p.driver.find_element_by_id("signUp").click()
            p.driver.find_element_by_id("id").clear()
            p.driver.find_element_by_id("id").send_keys("Test")
            p.driver.find_element_by_id("password").clear()
            p.driver.find_element_by_id("password").send_keys("wowkw5629!@")
            p.driver.find_element_by_id("name").clear()
            p.driver.find_element_by_id("name").send_keys("Test_Name")
            element = p.driver.find_element_by_id("btnContactUs")
            self.assertEqual(element.is_enabled(),False)
            module.status_id = 1
        except :
            module.status_id = 5

    # Test Rail 결과 메세지 입력
        if module.status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (module.run_id, module.case_id, module.passMsg))
            module.client.send_post(
                'add_result_for_case/%s/%s' % (module.run_id, module.case_id),
                {'module.status_id': module.status_id, 'comment': module.passMsg })

        elif module.status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (module.run_id, module.case_id, module.failMsg))
            module.client.send_post(
                'add_result_for_case/%s/%s' % (module.run_id, module.case_id),
                {'module.status_id': module.status_id, 'comment': module.failMsg })

if __name__ == "__main__":
    unittest.main()
