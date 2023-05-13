from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager # İlgili driver otomatik olarak indirilip handle ediliyor.

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com.tr/")
#driver.maximize_window()
searchTextBox = driver.find_element(By.NAME,"q")
searchTextBox.send_keys("kodlama.io")
sleep(2)
searchButton = driver.find_element(By.CLASS_NAME,"gNO89b")
searchButton.click()
sleep(3)
webSiteClick = driver.find_element(By.CLASS_NAME,"byrV5b")
webSiteClick.click()
sleep(3)
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio şitesinde şu anda {len(listOfCourses)} adet kurs var.")



driver.find_element(By.XPATH,"/html").screenshot("C:\\Users\\omerd\\Desktop\\test.png")


sleep(30)

driver.close

