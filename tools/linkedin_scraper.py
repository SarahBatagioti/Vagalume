from smolagents import tool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@tool
def extrair_perfil_linkedin(linkedin_url: str) -> dict:
    """Raspa dados básicos do perfil LinkedIn de uma pessoa.

    Args:
        linkedin_url: URL pública do perfil da pessoa no LinkedIn.
    
    Returns:
        Um dicionário com nome, título, localização e resumo.
    """
    try:
        # Configurações do navegador headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(linkedin_url)
        time.sleep(5)  # Espera a página carregar

        nome = driver.find_element(By.TAG_NAME, "h1").text
        titulo = driver.find_element(By.CLASS_NAME, "text-body-medium").text
        localizacao = driver.find_element(By.CLASS_NAME, "text-body-small").text

        # A tag <section> com o resumo pode variar - ajuste aqui conforme necessário
        resumo = ""
        try:
            resumo = driver.find_element(By.CLASS_NAME, "summary").text
        except:
            pass

        driver.quit()

        return {
            "nome": nome,
            "titulo": titulo,
            "localizacao": localizacao,
            "resumo": resumo
        }

    except Exception as e:
        return {"erro": str(e)}
