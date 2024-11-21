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

#Testar falhas de autenticação
def testar_falha_autenticacao(url, username, password_incorreto):
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        #credenciais incorretas
        driver.find_element(By.ID, "user_login").send_keys(username)
        driver.find_element(By.ID, "user_pass").send_keys(password_incorreto)
        driver.find_element(By.ID, "wp-submit").click()

        time.sleep(5)

        try:
            erro = driver.find_element(By.ID, "login_error").text
            if "erro" in erro.lower():
                print("Mensagem de erro exibida corretamente.")
            else:
                print("enhuma mensagem de erro detectada.")
        except:
            print("Nenhuma mensagem de erro exibida.")

        driver.quit()
    except Exception as e:
        print(f"Erro durante o teste de falha: {e}")



#verificar funcionalidades (( Bloco Principal ))
if __name__ == "__main__":
    url = "http://localhost:8000/wp-login.php"
    username = "WesleyAmorim" #professorSubstituir
    password_correto = "Sokg#$AK329@#Rp@ot$SS)Bv" #professorSubstituir
    password_incorreto = "qualquercoisa" #professorSubstituir

    #Antes de realizar o teste de credenciais, verificar disponibilidade do site
    print("Teste: Verificando disponibilidade do site...")
    if verificar_disponibilidade_site(url):
        #Login com credenciais corretas
        print("Teste: Credenciais corretas")
        monitorar_wordpress(url, username, password_correto)

        #Login com credenciais incorretas
        print("Teste: Falha de autenticação")
        testar_falha_autenticacao(url, username, password_incorreto)
    else:
        print("Site indisponivel. Login não será realizado.")