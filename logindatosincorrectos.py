import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

linkPagina = 'https://magento.softwaretestingboard.com/'
emailDePrueba = 'testinguadeprueba@gmail.com'
contraDePrueba = 'TestingPrueba1234falla'

driver.get(linkPagina)

# Buscamos el boton SignIn mediante su CLASS_NAME

navSignIn = driver.find_element(By.CLASS_NAME, "authorization-link")
navSignIn.click()

inputEmail = driver.find_element(By.ID, "email")
inputEmail.send_keys(emailDePrueba)

inputPass = driver.find_element(By.ID, "pass")
inputPass.send_keys(contraDePrueba)

btnSignIn = driver.find_element(By.ID, "send2")
btnSignIn.click()

time.sleep(10)

errorMsg = driver.find_element(By.CLASS_NAME, "message-error")

seMuestraMsgError = errorMsg.is_displayed()

print('Resultado: ', str(seMuestraMsgError))