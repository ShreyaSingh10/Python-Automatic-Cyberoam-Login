#from selenium module import webdriver
from selenium import webdriver

#from selenium module import Keys
from selenium.webdriver.common.keys import Keys

user = "imh1000014" #enter your user id
pwd = ""  #enter your password

#we are initialising Chrome by making an object of it
driver = webdriver.Chrome(executable_path= r'.\\driver\\chromedriver.exe')

#The "driver.get method" will explore to a page given by the URL.WebDriver will hold up until the page has completely been loaded (that is, the "onload" occasion has let go), before returning control to your test or script.
driver.get("https://172.16.1.1:8090/httpclient.html?u={proto}{url}")

#In this line, we are finding the element of the textbox where the "email" has to be written.
elem = driver.find_element_by_name("username")

#Now we are sending the values to the email section
elem.send_keys(user)

#same for password
elem = driver.find_element_by_name("password")

elem.send_keys(pwd)

#elem.send_keys(Keys.RETURN) is used to press enter after the values are inserted
elem.send_keys(Keys.RETURN)

#closes
#driver.close()