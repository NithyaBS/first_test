from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# create a new chrome session
driver = webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\chromedriver.exe")
driver.get("https://www.blogger.com")
#driver.save_screenshot("C:\\Users\\admin\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\haiamazon.png")
driver.maximize_window()
driver.implicitly_wait(15)
print("The title of the page is :")
print(driver.title)
print("The URL is :")
print(driver.current_url)
a= driver.find_element_by_link_text("SIGN IN").send_keys(Keys.ENTER)
input = driver.find_element_by_id('identifierId')
input.send_keys("nithya123bs@gmail.com")
driver.refresh()
print("SUCESSFULLY RUNNING")
driver.close()
