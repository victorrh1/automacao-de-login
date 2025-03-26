#LOGICA UTILIZADA:
#Link do site
#https://web.playmixmaster.com/account
#Identificar elementos de campo de login
#//input[@id='usrname']
#Identificar elementos de campo senha
#//input[@id='usrpwd']
#Identificar elementos do botão de login
#//button[@class='btn btn-danger rounded-0 w-100 text-menub']

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.playmixmaster.com/account')
sleep(5)

#precisei colocar o pagedown para que a automação identificasse o botão de entrar
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.PAGE_DOWN)
sleep(2)

login = driver.find_element(By.XPATH,"//input[@id='usrname']")
password = driver.find_element(By.XPATH,"//input[@id='usrpwd']")

login.send_keys('digite seu usuario')
sleep(2)
password.send_keys('digite sua senha')
sleep(2)
entrar = driver.find_element(By.XPATH,"//button[@class='btn btn-danger rounded-0 w-100 text-menub']")
sleep(1)
entrar.click()
input('')