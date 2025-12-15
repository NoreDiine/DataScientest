from selenium import webdriver
from selenium.webdriver.common.by import By
# Importations pour les Attentes Explicites
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
from datetime import datetime

TEMPS_MAX_ATTENTE = 10

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qacart-todo.herokuapp.com/")
wait = WebDriverWait(driver, TEMPS_MAX_ATTENTE)

EMAIL = "noreddine.l.m@gmail.com"
PASSWORD = "123456789"
try:

    emailInputSelector = (By.ID, "email")
    passwordInputSelector = (By.ID, "password")
    loginBtnSelector = (By.ID, "submit")

    time.sleep(2)

    emailInputBtn = wait.until(EC.element_to_be_clickable(emailInputSelector))
    emailInputBtn.send_keys(EMAIL)
    
    time.sleep(2)

    passwordInputBtn = wait.until(EC.element_to_be_clickable(passwordInputSelector))
    passwordInputBtn.send_keys(PASSWORD)

    loginBtn = wait.until(EC.element_to_be_clickable(loginBtnSelector))
    print(loginBtn)
    print("Bouton de recherche localisé.")


    # 3. INTERACTION : CLIQUER SUR LE BOUTON
    time.sleep(2)

    loginBtn.click()
    print("Clic effectué avec succès!")


    time.sleep(2)

    addTodoBtnSelector = (By.CSS_SELECTOR,'svg[data-testid="add"]')
    addTodoBtn = wait.until(EC.element_to_be_clickable(addTodoBtnSelector))
    addTodoBtn.click()
    
    addTodoInputSelector = (By.CSS_SELECTOR,'input[data-testid="new-todo"]')
    addTodoInput = wait.until(EC.element_to_be_clickable(addTodoInputSelector))
    addTodoInput.send_keys(f"NEW TODO Créé le {datetime.now()}")



except Exception as e:
    print(f"Erreur : {e}")


time.sleep(20)
driver.quit()