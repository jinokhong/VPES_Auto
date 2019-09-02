from testrail import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os

# TestRail 접속 정보
client = APIClient('http://211.116.223.42/testrail')
client.user = 'johong@suresofttech.com'
client.password = '12345'
passMsg = 'Test Run Success !!'
failMsg = 'Test Run Fail !!'
run_id = 391

usr = "qscroll"
pwd = "sure"
scm_git = "http://qatest@192.168.0.136:7990/scm/qat/server191.git"
scm_svn = "https://qa-server/VPES_Source"
scm_dir = "miro"

LicensePath = "\KEY-SQA_정상_70-85-C2-5E-1E-5E.license"

class default(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(90)
        self.driver.maximize_window()

    def test_project_init(self):
        driver = self.driver
        driver.get("http://211.116.223.190:18080/vpes") # VPES 서버 진입
        driver.find_element_by_id("username").send_keys(usr) # 로그인
        driver.find_element_by_id("pwd").send_keys(pwd)
        driver.find_element_by_id("pwd").send_keys(Keys.RETURN)
        driver.find_element_by_link_text("설정").click()
        driver.find_element_by_id("licenseSetting-tab").click()
        time.sleep(2)
        # 현재 파일의 폴더 위치 저장
        pathSave = os.path.dirname(os.path.realpath(__file__))
        # 현재 테스트 케이스의 위치로 이동
        os.chdir(pathSave)
        # 데이터 폴더로 이동
        os.chdir("VPES_License")
        # 현재 파일의 폴더 위치 저장
        realpath = os.getcwd()

        # 파일 포함 경로 선언
        FullPath = realpath + LicensePath
        print(FullPath)
        time.sleep(2)
        driver.find_element_by_name("uploadfile").send_keys(FullPath)
        time.sleep(2)
        driver.find_element_by_id("btn-license").click()
        try:
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "modal-content"))
            )
        except TimeoutException:
            print("타임아웃")
        assert "업로드 되었습니다." in driver.find_element_by_id("modal-content").text
        time.sleep(2)
        driver.find_element_by_link_text("전체현황").click()
        time.sleep(2)

        try:
            while 1 :
                # 프로젝트 반복 삭제
                driver.find_element_by_class_name("caret").click()
                driver.find_element_by_link_text("삭제").click()
                time.sleep(1)
                driver.find_element_by_id("deleteY").click()
                time.sleep(4)


        except NoSuchElementException: # 엘리먼트 없으면 VPES 메인 페이지로 이동 클릭
            driver.find_element_by_xpath("//*[@id='leftWrap']/h1/a/img").click()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()