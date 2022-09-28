import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

###########1 задание######################
#my_account = driver.find_element_by_link_text("My Account")
#my_account.click()
#email_address = driver.find_element_by_id("reg_email")
#email_address.send_keys("ivan@mail.com")
#password = driver.find_element_by_id("reg_password")
#password.send_keys("!Ivan1984!")
#register = driver.find_element_by_xpath("//input[@value='Register']")
#register.click()
#driver.quit()

################2 задание#####################
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("ivan@mail.com")
password = driver.find_element_by_id("password")
password.send_keys("!Ivan1984!")
login = driver.find_element_by_xpath("//input[@value='Login']")
login.click()
some_element= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout>a"), "Logout"))
driver.quit()