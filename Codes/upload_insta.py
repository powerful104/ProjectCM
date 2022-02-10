from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import os

"""
get_password 함수
매개변수 :

반환값 :
    extra에 위치하는 인스타 비밀번호를 반환
    
기능 :
    업로드에 이용되는 인스타 비밀번호를 반환한다.
"""

def get_password():
    f = open('extra/insta_password.txt','r')
    password = f.readline()
    f.close()
    return password

"""
upload_insta 함수

매개변수 :
    ---업로드 이미지 (이미지를 주려다가, 저장 후 사용한다는 형태로 변환)
    본문 텍스트 문자열

반환값 :
    업로드 상태 플래그 (오류 예외 방지용)

기능 :
    selenium을 활용하여 인스타에 이미지와 본문을 업로드한다.
    업로드 계정은 @color_mixed로 한다.
"""

def upload_insta(main_text):
    
    # 업로드 위해 모바일 폼으로 진행
    chrome_options = Options()
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    mobile_emulation = {"deviceName" : "Galaxy S5"}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    password = get_password()
    
    driver = webdriver.Chrome('extra/chromedriver.exe',options=chrome_options)
    driver.get('https://instagram.com/')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/main/article/div/div/div/div[3]/button[1]")))
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div/div/div/div[3]/button[1]").click()

    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div[1]/div[3]/div/label/input").send_keys('color__mixed')
    driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div[1]/div[4]/div/label/input").send_keys(password)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"loginForm\"]/div[1]/div[6]/button/div")))
    driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div[1]/div[6]/button/div").click()

    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/button").click()

    driver.get('https://www.instagram.com/color__mixed/')

    img = os.path.dirname(os.path.abspath(__file__))[:-6] + "\\extra\\today_img.jpg"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/nav[2]/div/div/div[2]/div/div/div[3]")))
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()

    time.sleep(1)
    pyautogui.write(f'{img}')
    pyautogui.press('enter')
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/div[1]/header/div/div[2]/button")))
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div[1]/header/div/div[2]/button").click()
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/div[2]/section[1]/div[1]/textarea")))
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div[2]/section[1]/div[1]/textarea").send_keys(main_text)
    
    time.sleep(200)
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/div[1]/header/div/div[2]/button")))
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/div[1]/header/div/div[2]/button").click()
    
    time.sleep(10)
    
    driver.quit()
