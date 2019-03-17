from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

LoginUrl = ('https://www.facebook.com/')

UserName= ('your account')
UserPass= ('your password')

options = webdriver.FirefoxOptions()

Browser = webdriver.Firefox(executable_path=r'E:\geckodriver.exe', options=options)

Browser.get(LoginUrl)
Browser.find_element_by_id('email').send_keys(UserName)
Browser.find_element_by_id('pass').send_keys(UserPass)
Browser.find_element_by_id('pass').send_keys(Keys.ENTER)
sleep(5)

Browser.get(r'https://www.facebook.com/ETtoday/')
Browser.implicitly_wait(10)
webdriver.ActionChains(Browser).send_keys(Keys.ESCAPE).perform()

Browser.save_screenshot('test.png')
Browser.quit()