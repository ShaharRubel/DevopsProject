from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5001/users/get_user_data/1")

try:
    driver.find_element("id", "user")
    print(driver.find_element("id", "user").text)
except:
    print("Element not found")