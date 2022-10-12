from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from colorama import Fore, Style

class Automate:

    def __init__(self, username, password, target):
        self.username = username
        self.password = password
        self.target = target

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        engine = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        try:
            print("Login with: "+self.username)
            engine.get("https://twitter.com/i/flow/login")
            WebDriverWait(engine,30).until(EC.element_to_be_clickable((By.NAME, 'text'))).send_keys(self.username+"\n")
            WebDriverWait(engine,30).until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(self.password)
            WebDriverWait(engine,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"][role="button"]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[data-testid="AppTabBar_Home_Link"][role="link"]')))

            print("Processing the report.....(The speed depends on your internet connection)")
            engine.get("https://www.twitter.com/"+self.target)
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="userActions"][role="button"]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[5]'))).click()
            engine.switch_to.frame(WebDriverWait(engine,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/iframe'))))
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/form/button[6]/div'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.ID, 'hateful-btn'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.ID, 'group-victim-btn'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'skip-btn'))).click()
            engine.switch_to.default_content()

            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div'))).click()
            engine.close()
            print("Target account ("+self.target+") has been reported => "+ Fore.GREEN +"[OK]" + Style.RESET_ALL)
            print("Waiting few seconds to avoid rate limits....")
            print("#####################")
            time.sleep(4)
        except Exception:
            engine.close()
            print(Fore.RED +"An error has occured, probably you have incorrect username/password, your Insta account not been verified, or your IP has blocked"+ Style.RESET_ALL)
            print("#####################")