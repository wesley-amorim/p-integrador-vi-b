from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

#Função para verificar se o site está disponivel
def verificar_disponibilidade_site(url):
    try:
        response = requests.get(url, timeout=7) #tempo de espera pela resposta de 8 segundos
        if response.status_code == 200:
            print("O site está disponivel.")
            return True
        else:
            print(f"Falha:  {response.status_code}.") # resposta variável
            return False
    except requests.exceptions.RequestException as e:
        print(f"O site está indisponível. Erro: {e}")
        return False
    
#Função que monitora as credenciais
def monitorar_wordpress(url, username, password):
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        assert "WordPress" in driver.title, "Site Incorreto!"

        #Credenciais
        driver.find_element(By.ID, "user_login").send_keys(username)
        driver.find_element(By.ID, "user_pass").send_keys(password)
        driver.find_element(By.ID, "wp-submit").click()

        time.sleep(5)

        #Verificar se tudo deu certo com login
        if "Painel" in driver.title or "Dashboard" in driver.page_source:
            print("Login realizado com sucesso!")
        else:
            print("Falha ao acessar o site com as credenciais fornecidas.")

        driver.quit()
    except Exception as e:
        print(f"Erro durante o monitoramento: {e}")