import Default_User
import unittest, time


# 1.6 기준 이슈 있음(이름 입력하지 않아도 회원가입 버튼 활성화됨)

# TestRail module.run_id, Testmodule.case_id, Message 정보
# case_id = 11124

class C11124(unittest.TestCase):
    def test_C11124(self):
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
        element = p.driver.find_element_by_id("btnContactUs")
        self.assertEqual(element.is_enabled(),False)
        time.sleep(2)

    # TestRail 결과 입력
    # try :
    #     self.assertEqual(element.is_enabled(),False)
    #     module.status_id = 1
    # except :
    #     module.status_id = 5
    #
    # module.client.send_post(
    #     'add_result_for_case/%s/%s' % (module.run_id, module.case_id),
    #     {'module.status_id': module.status_id, 'comment': msg,})
    # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (module.run_id, module.case_id, msg))

    # Test Rail 결과 메세지 입력
    # if module.status_id == 1:
    #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (module.run_id, module.case_id, module.passMsg))
    #     module.client.send_post(
    #         'add_result_for_case/%s/%s' % (module.run_id, module.case_id),
    #         {'module.status_id': module.status_id, 'comment': module.passMsg })
    #
    # elif module.status_id == 5:
    #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (module.run_id, module.case_id, module.failMsg))
    #     module.client.send_post(
    #         'add_result_for_case/%s/%s' % (module.run_id, module.case_id),
    #         {'module.status_id': module.status_id, 'comment': module.failMsg })

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()