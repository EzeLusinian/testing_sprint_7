import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

linkPagina = 'https://magento.softwaretestingboard.com/'
emailDePrueba = 'roni_cost@example.com'
contraDePrueba = 'roni_cost3@example.com'

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

textoIngresado = driver.find_element(By.CLASS_NAME, "logged-in")

seMuestraMsgWelcome = textoIngresado.is_displayed()

print('Resultado: ', str(seMuestraMsgWelcome))