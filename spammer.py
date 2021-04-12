#coding: utf-8
import selenium
import random
import time
import os
import getpass
from selenium import webdriver
from colorama import Fore, Back, Style
from colorama import init
init()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

#menu + sistema de login
os.system("@echo off")
os.system("cls")
os.system('color 6')
os.system("title COMMENT SPAMMER")
print(' ')
print(r'    ____   U  ___ u  __  __    __  __  U _____ u _   _     _____')         
print(r" U / ___|   \/ _ \/U|  \/  |uU|  \/  |u\| ___ |/| \ | |   |_   _|")        
print(r' \| | u     | | | |\| |\/| |/\| |\/| |/ |  _|  <|  \| |>    | | ')         
print(r'  | |/__.-,_| |_| | | |  | |  | |  | |  | |___ U| |\  |u   /| |\'')         
print(r'   \____|\_)-\___/  |_|  |_|  |_|  |_|  |_____| |_| \_|   u |_|U')         
print(r'  _// \\      \\   <<,-,,-.  <<,-,,-.   <<   >> ||   \\,-._// \\_ ')
print(r' (__)(__)    (__)   (./  \.)  (./  \.) (__) (__)(_")  (_/(__) (__)   ')    
print(r'       ____     ____       _      __  __    __  __  U _____ u   ____')     
print(r'      / __ | uU|  _ \ uU  / \  uU|  \/  |uU|  \/  |u\| ___ |/U |  _ \ u')  
print(r'     <\___ \/ \| |_) |/ \/ _ \/ \| |\/| |/\| |\/| |/ |  _|"   \| |_) |/')  
print(r'      u___) |  |  __/   / ___ \  | |  | |  | |  | |  | |___    |  _ < ')   
print(r'      |____/>> |_|     /_/   \_\ |_|  |_|  |_|  |_|  |_____|   |_| \_\  ') 
print(r'       )(  (__)||>>_    \\    >><<,-,,-.  <<,-,,-.   <<   >>   //   \\_ ') 
print(r'      (__)    (__)__)  (__)  (__)(./  \.)  (./  \.) (__) (__) (__)  (__) ')
print(' ')
print('                                                                             author: pedrokp // kp#3343')
print(' ')
login = str(input(' [+] Coloque seu usuario do instagram: '))
senha = getpass.getpass(' [+] Coloque a sua senha do instagram: ')
print(' ')
print(Fore.RED + ' [!] Caso queira parar o script, aperte CTRL+C')
print(Style.RESET_ALL)
print(Fore.RED + ' [!] Qualquer duvida entre em contato comigo pelo discord (kp#3343)')
print(Style.RESET_ALL)
#função de randomizar as mensagens
def my_shuffle(array):
    random.shuffle(array)
    print (Fore.YELLOW + ' >> ' + array[0])
    print(Style.RESET_ALL)
    return array[0]

#acesso ao instagram
driver.get('https://www.instagram.com/')
try:
    driver.implicitly_wait(5) # seconds
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
except:
    print(Fore.RED + ' [!] Algo deu errado, não foi possível acessar sua conta')
    print(Style.RESET_ALL)
    os.system("pause")
finally:
    print(Fore.RED + ' [!] Logado na conta com sucesso')
    print(Style.RESET_ALL)
    print(' ')
    try:
        driver.implicitly_wait(5) # seconds
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        driver.implicitly_wait(5) # seconds
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        perfil_alvo = str(input(Fore.YELLOW + ' [+] Coloque o perfil que contem o post desejado: '))
        driver.implicitly_wait(5) # seconds
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(perfil_alvo)
        driver.implicitly_wait(5) # seconds
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
        post_xpath = str(input(Fore.YELLOW + ' [+] Coloque o XPath do post que deseja comentar: '))
        print(Style.RESET_ALL)
        driver.implicitly_wait(5) # seconds
        driver.find_element_by_xpath(post_xpath).click()
        time.sleep(1)
        driver.refresh()
        print(Fore.RED + ' [!] Post acessado com sucesso')
        print(Style.RESET_ALL)
        messages = [item for item in input(Fore.YELLOW + ' [+] Coloque as mensagens que serao randomizadas (separe-as por virgulas): ').split(', ')]
        print(' ')
        print(Fore.MAGENTA + ' [*] Log dos comentarios: ')
        print(' ')
        print(' ')
        #spammer
        for i in range(10000):
            time.sleep(4)
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()
            print(Fore.MAGENTA + ' [*] Comentario enviado:      ' + Fore.YELLOW + '# ' + str(i+1))
            print(Style.RESET_ALL)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(my_shuffle(messages))
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
            driver.refresh()
            time.sleep(40)
        print(' ')
        print(Fore.RED + ' [!] Script concluido')
        print(Style.RESET_ALL)
        print(' ')
        print(' ')
        time.sleep(4)
        exit()
    except:
        print(Fore.RED + ' [!] Algo inesperado aconteceu, caso os erros persistam me adicione no discord (kp#3343)')
        print(Fore.RED + ' [!] Fechando aplicativo em 3 segundos...')
        print(Style.RESET_ALL)
        time.sleep(3)
        exit()
        
