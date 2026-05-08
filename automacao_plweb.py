import time
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

from numero import numeropl

# =========================================
# DRIVER ROBUSTO
# =========================================

def iniciar_driver():

    try:
        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        # perfil isolado (evita crash)
        options.add_argument(r"user-data-dir=C:\selenium_whatsapp_profile")

        driver = webdriver.Chrome(options=options)

        return driver

    except WebDriverException as e:
        print("ERRO AO INICIAR CHROME:")
        print(e)
        return None

# =========================================
# MODO TESTE
# =========================================

email_encontrado = {
    "subject": "PL WEB INFORMA - TESTE",
    "body": """
RELATÓRIO DE TESTE

STATUS: NÃO SEI
ATRASO: tanto faz dias
PONTOS POSITIVOS: Não tem
"""
}

# =========================================
# EXECUÇÃO
# =========================================

if email_encontrado:

    mensagem = email_encontrado["body"]

    print("\nEMAIL ENCONTRADO:")
    print(email_encontrado["subject"])

    print("\nCORPO:")
    print(mensagem)

   
    numero = numeropl()

    url = f"https://web.whatsapp.com/send?phone={numero}"

    driver = iniciar_driver()

    if driver is None:
        print("Chrome não iniciou. Abortando automação.")
        exit()

    driver.get(url)

    wait = WebDriverWait(driver, 60)

    caixa = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//footer//div[@contenteditable="true"][@role="textbox"]')
        )
    )

    time.sleep(2)

    pyperclip.copy(mensagem)

    caixa.click()
    caixa.send_keys(Keys.CONTROL, "v")
    time.sleep(1)

    caixa.send_keys(Keys.ENTER)

    print("Mensagem enviada com sucesso")

    time.sleep(3)

    driver.quit()

else:
    print("Nenhum email encontrado.")