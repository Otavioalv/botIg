from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class InstagramBot:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        
    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        
        sleep(5)
        
        username_element = driver.find_element(By.NAME, 'username');
        username_element.clear()
        sleep(2)
        username_element.send_keys(self.username)
        sleep(2)
        
        password_element = driver.find_element(By.NAME, 'password')
        password_element.clear()
        sleep(2)
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        sleep(5)
        
    def find_profile(self, username):
        driver = self.driver
        url = 'https://www.instagram.com/' + username + "/followers/"
        driver.get(url)
        sleep(5)
        
    def button_follower(self):
        driver = self.driver
        try:
            button_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'x78zum5') and contains(@class, 'x1q0g3np') and contains(@class, 'xieb3on')]"))
            )
            print(button_list)
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def button_followers(self):
        driver = self.driver
        # x78zum5 x1q0g3np xieb3on
        button_list = driver.find_element(By.XPATH, "//ul[contains(@class, 'x78zum5') and contains(@class, 'x1q0g3np') and contains(@class, 'xieb3on')]")
        print(button_list)
        
    def follow_all(self):
        driver = self.driver
        
        # _acan _acap _acas _aj1- _ap30
        button_list = driver.find_elements(By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30)]")

        seguidor = 0
        teste = 0
            
        while teste < 10:
            for element in button_list: 
                driver.execute_script('arguments[0].click();', element)
                seguidor += 1
                
                print(seguidor)
                sleep(7)
            teste+=1
        
 
Bot = InstagramBot('otavioalv_1', 'galego00');
Bot.login();
Bot.find_profile('amazon')
Bot.button_followers()

        
        
        
        