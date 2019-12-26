import time
from selenium import webdriver
from bs4 import BeautifulSoup    
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
import requests

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
#driver = webdriver.Chrome(options=options,executable_path='write the path of chrome driver example is shown below ')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome(options=options,executable_path='C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/chromedriver.exe')  # Optional argument, if not specified will search path.
#driver.get('paste the login url of the website')
#print("opening https://xyz.com/Identity/Account/Login?ReturnUrl=%2F")
driver.get('https://xyz.com/Identity/Account/Login?ReturnUrl=%2F')
print("waiting 5 seconds")
time.sleep(5) # Let the user actually see something!
#username = driver.find_element_by_id('click inspect element on username entering textbox and find for id attribute paste 
# as shown in below')
username = driver.find_element_by_id('Input_Email')
print("entering email")
#send your email id as keys 
username.send_keys('user@xyz.com')
#simliar for password
password = driver.find_element_by_id('Input_Password')
print("entering password")
password.send_keys('xyz@123')
#click on submit button to login
print("clicking on submit")
driver.find_elements_by_tag_name('button')[0].click()
print("navigating to xyz page")
driver.get('https://xyz.com/home/downloads')
#clicking on selected row in a table automatically 
print("selecting row")
td_list = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector("#DataTables_Table_0 tr td"))
for td in td_list:
    try:
        if(td.text == "text in that row "):
            td.click()
        print("row is clicked")
    except exceptions.StaleElementReferenceException as e:
        pass
time.sleep(5)
td_list1 = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_tag_name("a"))
for t in td_list1:
    try:
        if(t.text == "text in that row "):
            t.click()
    except exceptions.StaleElementReferenceException as e:
        pass
print("row is clicked")
#to download 
soup = BeautifulSoup(driver.page_source)
for x in soup.findAll('a',attrs={'type':'submit'}):
    Downloadlink="https://xyz.com" + x.get('href')    
    myfile = requests.get(Downloadlink)
    #custmozise your saveing location..
    open('C:/Users/CS-10/Desktop/New/20191912.txt', 'wb').write(myfile.content)
    print("document downloaded")