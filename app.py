from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.playmixmaster.com/account')
sleep(5)

login = driver.find_element(By.XPATH,"//input[@id='usrname']")
password = driver.find_element(By.XPATH,"//input[@id='usrpwd']")

login.send_keys('digite seu login')
sleep(2)
password.send_keys('digite sua senha')
sleep(2)
entrar = driver.find_element(By.XPATH,"//button[@class='btn btn-danger rounded-0 w-100 text-menub']")
sleep(2)
input('')