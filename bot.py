from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import random

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
            # Espera até que o elemento <a> com href '/amazon/followers/' esteja presente
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/amazon/followers/')]"))
            )
            # driver.execute_script('arguments[0].click();', button)
            button.click();
            sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

        
    def follow_all(self):
        driver = self.driver
        
        try:
            button_list = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]"))
            )

            seguidor = 0
            teste = 0

            while teste < 10:
                for element in button_list:
                    try:
                        driver.execute_script('arguments[0].click();', element)
                        # Aguarda um tempo aleatório entre 5 e 10 segundos
                        sleep(random.uniform(5, 10))
                        seguidor += 1
                        print(f"Seguidor número: {seguidor}")
                    except Exception as e:
                        print(f"Não foi possível seguir a pessoa: {e}")
                teste += 1
                # Atualiza a lista de botões após cada iteração
                button_list = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]"))
                )
        except Exception as e:
            print(f"An error occurred: {e}")
        
 
Bot = InstagramBot('otavioalv_1', 'galego00');
Bot.login();
Bot.find_profile('amazon')
Bot.button_follower()
Bot.follow_all()

        
        
        
    