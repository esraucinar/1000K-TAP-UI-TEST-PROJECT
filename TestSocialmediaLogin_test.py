from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants import globalConstants as gC
import pytest
from selenium.webdriver.common.action_chains import ActionChains

class TestSocialmediaLogin():
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get(gC.URL)
        self.driver.maximize_window()
    
    def teardown_method(self): 
        self.driver.quit() 
    
    def login(self):
        girisyap_button = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.XPATH, gC.LOGIN)))
        girisyap_button.click()
        sleep(15)
        emailLogin= WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH,gC.EMAIL)))
        emailLogin.click()
        sleep(2)
        emailLogin.send_keys(gC.EMAIL_ADDRESS)
        sleep(5)
        password = WebDriverWait(self.driver,35).until(ec.visibility_of_element_located((By.XPATH,gC.PASSWORD_FIELD)))
        password.click()
        password.send_keys(gC.PASSWORD)
        sleep(2)
        loginButton = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH,gC.LOGIN_BUTTON)))
        loginButton.click()
        return 

#Profile Management- Profile Photo
    def test_profile_photo(self):
        self.login()
        sleep(15)
        profilephoto = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.LINK_TEXT,gC.PROFILE)))
        profilephoto.click()
        sleep(5)
        organize = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,gC.ORGANIZE)))
        organize.click()
        organize_profile = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,gC.ORGANIZE_PROFILE)))
        organize_profile.click()
        profile_avatar = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,gC.AVATAR)))
        profile_avatar.click()
        sleep(3)
        print("Current URL after click:", self.driver.current_url)


  
