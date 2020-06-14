from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,NoAlertPresentException, UnexpectedAlertPresentException, ElementNotInteractableException
from user_credentials import Email, Passowrd
import time
from datetime import datetime
import random
#from apscheduler.schedulers.blocking import BlockingScheduler


#Declare time module
sleeptime = time

#gtidevops = '/html/body/rdp-client-top-view/div/div[1]/rdp-all-resources-pane/div/div[2]/rd-resource-list/div/div[2]/div[14]'
#df_btn = '/html/body/rdp-client-top-view/div/div[1]/rdp-all-resources-pane/div/div[2]/rd-resource-list/div/div[2]/div'

#define variable
wvd_url = "https://rdweb.wvd.microsoft.com/webclient"
webdriver_path = "D:\\webdriver\\chromedriver.exe"
first_page_btn = '/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input'
remote_app_btn = '/html/body/rdp-client-top-view/div/div[1]/rdp-all-resources-pane/div/div[2]/rd-resource-list/div/div[2]/div[14]'
allow_btn_xpath = '/html/body/div[1]/div/div/form/div[2]/button[1]'
remote_app_login_btn_xpath = '/html/body/rdp-client-top-view/div/div[1]/session-view/div/div[2]/div[2]/div[2]/div/div/form/div[2]/button[1]'
user_cred_box_xpath = '/html/body/rdp-client-top-view/div/div[1]/session-view/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/label[1]/input'
passd_cred_box_xpath = '/html/body/rdp-client-top-view/div/div[1]/session-view/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/label[2]/input'


def loginUserEmailAndPassowrd(email,password,driver):
    sleeptime.sleep(10)
    #Find email input box element by id and type into email data
    #Use "Enter" KEY to next page
    email_textbox =  driver.find_element_by_id("i0116")
    email_textbox.send_keys(email, Keys.ENTER)

    #Find email input box element by id and type into password data
    password_textbox = driver.find_element_by_id("i0118")
    password_textbox.send_keys(password)

def checkLoginUserCredential(email,password,driver):
    print("User: "+email.split("@",1)[0]+" start at "+str(datetime.now()))
    sleeptime.sleep(10)
    #driver.find_element_by_css_selector('#idSIButton9').click()
    #Define login button XPath locator
    locator = (By.XPATH, first_page_btn)
    #Use "WebDriverWait" find login button XPath and set time limit
   
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print(email+" has TimeoutException")
        print("page refresh...")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        sleeptime.sleep(20)
        loginUserEmailAndPassowrd(email,password,driver)
        print("return to checkLogin method")
        checkLoginUserCredential(email,password,driver)
    except NoSuchElementException:
        print(email+" has NoSuchElementException")
        print("page refresh...")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        sleeptime.sleep(20)
        loginUserEmailAndPassowrd(email,password,driver)
        print("return to checkLogin method")
        checkLoginUserCredential(email,password,driver)

    sleeptime.sleep(10)
    #When finding the XPath will click the login button
    driver.find_element_by_xpath(first_page_btn).click()

    #Log a message when user login successfully
    print("User: "+email+" logined")

def clickAppIconAction(email,password,driver):
    sleeptime.sleep(10)
    #Declare app icon XPath location 
    remote_app_icon = (By.XPATH, remote_app_btn)
    
    #Use "WebDriverWait" find app icon XPath and set time limit
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(remote_app_icon))
    except TimeoutException:
        print(email+" has TimeoutException")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        print("page refresh...")
        sleeptime.sleep(20)
        print("return to appIconAction method")
        clickAppIconAction(email,password,driver)
    except NoSuchElementException:
        print(email+" has NoSuchElementException")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        print("page refresh...")
        sleeptime.sleep(20)
        print("return to appIconAction method")
        clickAppIconAction(email,password,driver)

    sleeptime.sleep(10)
    #When finding the XPath will click the app icon
    driver.find_element_by_xpath(remote_app_btn).click()

    #Log a message when user click app icon successfully
    print("User: "+email.split("@",1)[0]+": click remote machine icon")

    #Declare allow button XPath location
    sleeptime.sleep(10)
    allow_btn = (By.XPATH, allow_btn_xpath)

    #Use "WebDriverWait" find allow button XPath and set time limit
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(allow_btn))
    except TimeoutException:
        print(email+" has TimeoutException")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        print("page refresh...")
        sleeptime.sleep(20)
        print("return to appIconAction method")
        clickAppIconAction(email,password,driver)
    except NoSuchElementException:
        print(email+" has NoSuchElementException")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        print("page refresh...")
        sleeptime.sleep(20)
        print("return to appIconAction method")
        clickAppIconAction(email,password,driver)

    sleeptime.sleep(10)
    #When finding the XPath will click the allow button
    driver.find_element_by_xpath(allow_btn_xpath).click() 

    #Log a message when user click allow button successfully
    print("User: "+email.split("@",1)[0]+" click allow button")
    
def loginUserRemoteApp(email,password,driver):
    sleeptime.sleep(10)
    #Declare remote app login button XPath locaiton
    remote_app_login_btn = (By.XPATH, remote_app_login_btn_xpath)
    
    #Use "WebDriverWait" find login button XPath and set time limit
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(remote_app_login_btn))
    except TimeoutException:
        print(email+" has TimeoutException")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        print("page refresh...")
        sleeptime.sleep(20)
        #Acccept alert function
        driver.switch_to_alert().accept()
        print("confirm alert") 
        sleeptime.sleep(10)
        clickAppIconAction(email,password,driver)
        print("return to loginRemoteApp method")
        loginUserRemoteApp(email,password,driver)

    except NoSuchElementException:
        print(email+" has TimeoutException")
        #If has error webdriver will be refresh and load again
        driver.refresh()
        print("page refresh...")
        sleeptime.sleep(20)
        #Acccept alert function
        driver.switch_to_alert().accept()
        print("confirm alert")
        sleeptime.sleep(10)
        clickAppIconAction(email,password,driver)
        print("return to loginRemoteApp method")
        loginUserRemoteApp(email,password,driver)

           
    sleeptime.sleep(10)
    #When finding the XPath will type into email and password
    email_textbox =  driver.find_element_by_xpath(user_cred_box_xpath)
    email_textbox.send_keys(email)
    password_textbox = driver.find_element_by_xpath(passd_cred_box_xpath)
    password_textbox.send_keys(password)
    sleeptime.sleep(10)
    #Then click the login button
    driver.find_element_by_xpath(remote_app_login_btn_xpath).click()

    #Log a message when user logined to remote app successfully
    ran = random.randint(60,150)
    print("User: "+email.split("@",1)[0]+" sleep "+ str(ran)+" seconds ")
    sleeptime.sleep(ran)
    #for session host connect to remote desktop
    #sleeptime.sleep(900)
    #Log a message when user logout remote app successfully and close the chrome driver
    #print(email+" logout this seesion")
    #Close webdriver when user finish
    driver.close()
    driver.quit()
        
def openBrowser():
    #declare user email and password from other class
    user_email_list = Email.email_list
    user_password_list = Passowrd.password_list
    #loop user login and connect to wvd 
    for time in range(len(user_email_list)):
        #chrome_option = webdriver.ChromeOptions()
        #chrome_option.add_argument('--headless')
        sleeptime.sleep(10)
        #declare webdriver location and wvd web client url
        driver = webdriver.Chrome(webdriver_path)#, chrome_options=chrome_option)
        driver.get(wvd_url)
        #get user credentials from credentials list
        email = user_email_list[time]
        password = user_password_list[time]
        sleeptime.sleep(10)
        loginUserEmailAndPassowrd(email,password,driver)
        checkLoginUserCredential(email,password,driver)
        clickAppIconAction(email,password,driver)
        loginUserRemoteApp(email,password,driver)
        #print(email+" end at "+str(datetime.now()))
        print("User: "+email.split("@",1)[0]+" end at "+str(datetime.now()))

openBrowser()
#Set schedule for the function
#if __name__ == '__main__':
    #scheduler = BlockingScheduler()
    #scheduler.add_job(openBrowser, 'cron', day_of_week="mon-fri", hour="11", minute="50")  # run on Monday to Friday at 16:30
    #scheduler.start()



    



