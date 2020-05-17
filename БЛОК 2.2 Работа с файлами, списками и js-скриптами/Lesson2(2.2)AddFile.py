from selenium import webdriver
import time
import os

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)

	firstname = browser.find_element_by_name("firstname")
	firstname.send_keys("Test_name")

	lastname = browser.find_element_by_name("lastname")
	lastname.send_keys("Test_last_name")

	email = browser.find_element_by_name("email")
	email.send_keys("test@test.ru")

	element = browser.find_element_by_id("file")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	element.send_keys(file_path)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()