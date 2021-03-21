from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
from selenium.webdriver.remote.file_detector import UselessFileDetector

x=400
y=254

email = (By.ID,"i0116")
next = (By.ID,"idSIButton9")
passw = (By.ID,"i0118")

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.maximize_window()

driver.get("https://login.microsoftonline.com/dec2e631-d656-473c-afff-447008969d2f/oauth2/authorize?client_id=00000003-0000-0ff1-ce00-000000000000&response_mode=form_post&protectedtoken=true&response_type=code%20id_token&resource=00000003-0000-0ff1-ce00-000000000000&scope=openid&nonce=06A7E8476B916E5B799822719B418D164BB2D44BD22D80C1-6069B6B8341E670EF89F50F100919AEE505D098F67BE8C81A6F28AE14DDB2F5D&redirect_uri=https%3A%2F%2Fiiitborg-my.sharepoint.com%2F_forms%2Fdefault.aspx&claims=%7B%22id_token%22%3A%7B%22xms_cc%22%3A%7B%22values%22%3A%5B%22CP1%22%5D%7D%7D%7D&wsucxt=1&cobrandid=11bd8083-87e0-41b5-bb78-0bc43c8a8e8a&client-request-id=f623b69f-f0ae-0000-83c3-75b9b18bdad3")

WebDriverWait(driver,10).until(EC.element_to_be_clickable(email)).send_keys("Srinivasa.Bhargava@iiitb.org")

WebDriverWait(driver,10).until(EC.element_to_be_clickable(next)).click()

WebDriverWait(driver,10).until(EC.element_to_be_clickable(passw)).send_keys("Z-G%855h=iDEGXe")

WebDriverWait(driver,10).until(EC.element_to_be_clickable(next)).click()

WebDriverWait(driver,10).until(EC.element_to_be_clickable(next)).click()

manda = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/button')

action = ActionChains(driver)

action.move_to_element(manda).click().perform()

time.sleep(2)
pyautogui.click(x,y)
