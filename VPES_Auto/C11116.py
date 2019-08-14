import Default_User
import unittest, time


# TestRail run_id, Testcase_id, Message 정보
# case_id = 11116

class C11116(unittest.TestCase):
    def test_C11116(self):
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
        p.driver.find_element_by_id("name").clear()
        p.driver.find_element_by_id("name").send_keys("한글")
        p.driver.find_element_by_id("btnContactUs").click()
        time.sleep(1)
        self.assertEqual(p.driver.find_element_by_id("modal-content").text, "회원가입이 완료되었습니다.")
        time.sleep(2)

    # TestRail 결과 입력
    # try :
    #     self.assertEqual(p.driver.find_element_by_id("modal-content").text, "회원가입이 완료되었습니다.")
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

