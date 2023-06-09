from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("http://automationpractice.pl/index.php")   

women_menu = driver.find_element(By.XPATH, "//*[@id='block_top_menu']//a[@title='Women']").click()
# women_menu.click()

sleep(2)


driver.quit()