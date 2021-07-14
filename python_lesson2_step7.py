from selenium import webdriver
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
def cal(x):
    return math.log(abs(12*math.sin(x)))
try:
    browser = webdriver.Chrome() 
    browser.get(link)#изменение ссылки     
    browser.implicitly_wait(12)
    b=WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    but=browser.find_element_by_id('book')
    but.click()   
    
    y = str(browser.find_element_by_id("input_value").text)    
    x = cal(int(y))   
    input=browser.find_element_by_id("answer")
    input.send_keys(str(x))

   # button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #inp=browser.find_element_by_id("robotCheckbox")
    #inp.click()
    #inh=browser.find_element_by_id("robotsRule")
    #inh.click()
    #button.click()
    #select = Select(browser.find_element_by_tag_name("select"))
   # select.select_by_value(str(int(x)+int(y)))     
    
    button = browser.find_element(By.XPATH,'//button[text()="Submit"]')
    button.click()
    time.sleep(10)
       
finally:
    time.sleep(10)    
    browser.quit()
