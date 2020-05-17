from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)

	book = browser.find_element_by_id("book")
	price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
	book.click()

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)

	answer = browser.find_element_by_id("answer")
	answer.send_keys(y)
	submit = browser.find_element_by_id("solve")
	submit.click()

finally:
	time.sleep(10)
	browser.quit()