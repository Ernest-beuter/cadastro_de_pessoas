import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)
    usuario = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    usuario.send_keys("tomsmth")
    senha = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    senha.send_keys("SuperSecretPassword!")
    botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
    botao.click()

    print("lmao")
    time.sleep(1)
    print("lol")

    mensagem = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text

    assert "You logged into a secure area!" in mensagem
    assert driver.current_url.endswith("/secure")
    print("ct01 t")
    print(mensagem)

    logout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
    logout.click()
    print(driver.title)
    time.sleep(12)
finally:
    driver.quit()
