from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	num1_element = browser.find_element_by_id("num1")
	num1 = num1_element.text
	num2_element = browser.find_element_by_id("num2")
	num2 = num2_element.text
	summa = str(int(num1) + int(num2))

	from selenium.webdriver.support.ui import Select
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(summa)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()