from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_DemoClass:
    #Her testten önce çağırılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #Günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur.
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    #Her testten sonra çağırılır.
    def teardown_method(self):
        self.driver.quit()
        print("")
    
    # setup -> test_demoFunc - teardown
    def test_demoFunc(self):
        text ="Hello"
        assert text == "Hello"
    def test_demo2(self):
        assert True

    #@pytest.mark.skip()#Bu testi atla, yapma anlamına gelir.
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])
    def test_invalid_login(self,username,password):
        WebDriverWait(self.driver,30).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,30).until(ec.visibility_of_all_elements_located((By.ID,"password")))    
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        
        WebDriverWait(self.driver,30).until(ec.visibility_of_all_elements_located((By.ID,"login-button")))

        loginBtn = self.driver.find_element(By.ID,"login-button").click()
        WebDriverWait(self.driver,30).until(ec.visibility_of_all_elements_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

