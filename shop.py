import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
############1 задание########################
#my_account = driver.find_element_by_link_text("My Account")
#my_account.click()
#username = driver.find_element_by_id("username")
#username.send_keys("ivan@mail.com")
#password = driver.find_element_by_id("password")
#password.send_keys("!Ivan1984!")
#login = driver.find_element_by_xpath("//input[@value='Login']")
#login.click()
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#HTML_5_Forms = driver.find_element_by_partial_link_text("Forms")
#HTML_5_Forms.click()
#some_element= WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-title"), "HTML5 Forms"))
#driver.quit()

################2 задание##################
#my_account = driver.find_element_by_link_text("My Account")
#my_account.click()
#username = driver.find_element_by_id("username")
#username.send_keys("ivan@mail.com")
#password = driver.find_element_by_id("password")
#password.send_keys("!Ivan1984!")
#login = driver.find_element_by_xpath("//input[@value='Login']")
#login.click()
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#HTML = driver.find_element_by_link_text("HTML")
#HTML.click()
#items_count = driver.find_elements_by_class_name("product-type-simple")
#if len(items_count) == 3:
#    print("3 товара")
#else:
# print("Ошибка. Количество товаров: " + str(len(items_count)))
#driver.quit()

###############3 задание###############
#my_account = driver.find_element_by_link_text("My Account")
#my_account.click()
#username = driver.find_element_by_id("username")
#username.send_keys("ivan@mail.com")
#password = driver.find_element_by_id("password")
#password.send_keys("!Ivan1984!")
#login = driver.find_element_by_xpath("//input[@value='Login']")
#login.click()
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#selector = driver.find_element_by_xpath("//option[@value='menu_order']")
#selector_text = selector.text
#assert selector_text == "Default sorting"
#from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
#element = driver.find_element_by_class_name("orderby") # "element" это просто название переменной, можно задать и другое
#select = Select(element)
#select.select_by_visible_text("Sort by price: high to low")
#selector_new = driver.find_element_by_xpath("//option[@value='price-desc']")
#selector_new_text = selector_new.text
#assert selector_new_text == "Sort by price: high to low"
#driver.quit()

##############4 задание###############
#my_account = driver.find_element_by_link_text("My Account")
#my_account.click()
#username = driver.find_element_by_id("username")
#username.send_keys("ivan@mail.com")
#password = driver.find_element_by_id("password")
#password.send_keys("!Ivan1984!")
#login = driver.find_element_by_xpath("//input[@value='Login']")
#login.click()
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#login = driver.find_element_by_xpath("//img[@alt='Android Quick Start Guide']")
#login.click()
#book_old_price = driver.find_element_by_css_selector(".price > del > span")
#book_old_price_text = book_old_price.text
#book_new_price = driver.find_element_by_css_selector(".price > ins > span")
#book_new_price_text = book_new_price.text
#assert book_old_price_text == "₹600.00"
#assert book_new_price_text == "₹450.00"
#book_cover = WebDriverWait (driver, 10) .until(
#    EC.element_to_be_clickable ((By.CSS_SELECTOR, ".images")))
#book_cover.click()
#book_cover_close = WebDriverWait (driver, 10) .until(
#    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
#book_cover_close.click()
#driver.quit()

###########5 задание##############
#driver.implicitly_wait(5)
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#add_to_basket = driver.find_element_by_xpath("//a[@data-product_id='182']")
#add_to_basket.click()
#basket = driver.find_element_by_xpath("//a[@title='View your shopping cart']")
#basket.click()
#some_element= WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>td>.amount"), "180.00"))
#some_element= WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total>td>strong>span"), "183.60"))
#driver.quit()

##########6 задание##########
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#driver.execute_script("window.scrollBy(0, 300);")
#webapp_develpmend = driver.find_element_by_xpath("//a[@data-product_id='182']")
#webapp_develpmend.click()
#time.sleep(3)
#js_data= driver.find_element_by_xpath("//a[@data-product_id='180']")
#js_data.click()
#basket = driver.find_element_by_xpath("//a[@title='View your shopping cart']")
#basket.click()
#time.sleep(3)
#delete= driver.find_element_by_xpath("//a[@data-product_id='182']")
#delete.click()
#time.sleep(3)
#undo = driver.find_element_by_css_selector(".woocommerce-message>a")
#undo.click()
#Quantity = driver.find_element_by_xpath("//input[@name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
#Quantity.click()
#Quantity.clear()
#Quantity.send_keys("3")
#update_basket = driver.find_element_by_xpath("//input[@value='Update Basket']")
#update_basket.click()
#quantity1 = driver.find_element_by_xpath("//input[@name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
#quantity1_text = quantity1.get_attribute("value")
#assert quantity1_text == "3"
#time.sleep(3)
#apply_coupon = driver.find_element_by_xpath("//input[@name='apply_coupon']")
#apply_coupon.click()
#some_element= WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
#driver.quit()

############7 задание################
#driver.implicitly_wait(5)
#shop = driver.find_element_by_link_text("Shop")
#shop.click()
#driver.execute_script("window.scrollBy(0, 300);")
#webapp_develpmend = driver.find_element_by_xpath("//a[@data-product_id='182']")
#webapp_develpmend.click()
#basket = driver.find_element_by_xpath("//a[@title='View your shopping cart']")
#basket.click()
#proceed_to_checkout = driver.find_element_by_class_name("wc-forward")
#proceed_to_checkout.click()
#First_Name = driver.find_element_by_id("billing_first_name")
#First_Name.send_keys("Ivan")
#Last_Name = driver.find_element_by_id("billing_last_name")
#Last_Name.send_keys("Petrov")
#Email_Address = driver.find_element_by_id("billing_email")
#Email_Address.send_keys("ivan@mail.com")
#Phone = driver.find_element_by_id("billing_phone")
#Phone.send_keys("89991112233")
#select = driver.find_element_by_id("s2id_billing_country")
#select.click()
#text = driver.find_element_by_id("s2id_autogen1_search")
#text.send_keys("Russia")
#russia = driver.find_element_by_class_name("select2-result-label")
#russia.click()
#Address = driver.find_element_by_id("billing_address_1")
#Address.send_keys("Leninski")
#Address = driver.find_element_by_id("billing_address_2")
#Address.send_keys("35")
#Town_City = driver.find_element_by_id("billing_city")
#Town_City.send_keys("Moscow")
#State_County = driver.find_element_by_id("billing_state")
#State_County.send_keys("Russia")
#Postcode_ZIP = driver.find_element_by_id("billing_postcode")
#Postcode_ZIP.send_keys("12345")
#driver.execute_script("window.scrollBy(0, 600);")
#option = driver.find_element_by_css_selector("[value='cheque']")
#option.click()
#driver.implicitly_wait(5)
#place_order = driver.find_element_by_id("place_order")
#place_order.click()
#some_element= WebDriverWait(driver, 10).until(
#    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
#driver.quit()