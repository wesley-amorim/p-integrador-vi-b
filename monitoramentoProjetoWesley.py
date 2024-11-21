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