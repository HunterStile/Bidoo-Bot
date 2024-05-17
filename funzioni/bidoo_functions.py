#librerie
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
from random import randint
from time import sleep
import csv 
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from selenium import webdriver
import string
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
import os
# Ottieni il percorso assoluto della directory corrente (dove si trova il file eseguibile)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Costruisci il percorso assoluto della cartella "Setup"
setup_dir = os.path.join(current_dir, 'Setup')
# Costruisci i percorsi assoluti dei file di testo
path_chrome = os.path.join(setup_dir, 'path_chrome.txt')
path_driver = os.path.join(setup_dir, 'path_driver.txt')

#Variabili
a = 1
b = 2
count = 0
vuoto = 'NAN'
riproduzioni = 2
path = path_driver
chrome_scelto = path_chrome

#ACCESSO
username = ''
password = ''

def Check_robot(driver):
    page_text = check_conferma(driver)
    robot  = "puntata" in page_text
    print(page_text)
    while robot == False:
        print("richiesta robot...")
        page_text = check_conferma(driver)
        robot  = "robot" in page_text
        sleep(randint(3,5))

def torna_indietro():
    sleep(randint(a,b))
    pyautogui.click(41,32)
    sleep(randint(a,b))
def cerca_bottone():
    pyautogui.click(619,380)
    pyautogui.click(619,400)
    pyautogui.click(619,450)
    pyautogui.click(619,500)
    pyautogui.click(619,550)
    pyautogui.click(619,600)
    pyautogui.click(619,650)
    pyautogui.click(619,700)
    pyautogui.click(619,750)
    pyautogui.click(619,800)
    pyautogui.click(619,850)
    pyautogui.click(619,900)

def prendere_puntate(driver):
    pyautogui.click(140,362)
    
    check_conferma(driver)
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,427)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,498)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,581)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,654)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,709)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,788)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,852)
    
    sleep(randint(a,b))
    cerca_bottone()
    torna_indietro()
    pyautogui.click(140,896)
    
    sleep(randint(a,b))
    torna_indietro()
    cerca_bottone()

def yop_click(driver,email):
    yop_link = 'https://yopmail.com/it/'
    driver.get(yop_link)
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p').click()
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'//*[@id="login"]').send_keys(email)
    sleep(randint(a,b)) 
    driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button').click()
    sleep(randint(a,b))
    

def configurazione_browser():
    chrome_driver_path = leggi_txt(path)
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = "C:\\Users\\Luigi\\Desktop\\chrome-win64\\chrome.exe"
    chrome_options.binary_location = leggi_txt(chrome_scelto)
    driver =Chrome(service=Service(chrome_driver_path),options=chrome_options)
    sleep(randint(a,b))
    return driver


def leggi_txt(nome_file):
    try:
        with open(nome_file, 'r') as file:
            prima_riga = file.readline().strip()  # Legge la prima riga e rimuove eventuali spazi bianchi iniziali/finali
            return prima_riga
    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non è stato trovato.")
        return None
    except Exception as e:
        print(f"Errore durante la lettura del file '{nome_file}': {e}")
        return None

def creazione_bidoo(driver):
    print("Creo account...")
    link = 'https://shopping.bidoo.it/'
    fake = Faker('it_IT')
    nickname = generate_random_string(6)
    password = 'Napoli10!'
    email = generate_random_string(10)
    email +="@yopmail.com"
    driver.get(link)
    sleep(randint(3,4))
    driver.find_element(By.XPATH,'//*[@id="email_signup"]').send_keys(email)
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'//*[@id="holdon"]/div[1]/div/form/div[2]/input').send_keys(nickname)
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'//*[@id="password_signup"]').send_keys(password)
    sleep(randint(a,b))             
    driver.find_element(By.XPATH,'//*[@id="holdon"]/div[1]/div/form/div[4]/div/label/input').click()
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'//*[@id="btnRegister"]').click()
    sleep(randint(a,b))

    # Dati da inserire nel file CSV
    new_rows = [
            [email, nickname, password]
        ]

    # Apri il file CSV in modalità append
    with open('account_bidoo.csv', 'a', newline='') as csvfile:
        # Scrivi i dati nel file CSV
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in new_rows:
            csvwriter.writerow(row)
       
    input()
    driver.close()

def accesso_bidoo(driver,username,password):
    robot = False
    print("Procedo ad accedere...")
    driver.get('https://it.bidoo.com/login_push.php')
    sleep(randint(2,3))
    driver.find_element(By.XPATH,'//*[@id="field_email"]').send_keys(username)
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    sleep(randint(a,b))
    driver.find_element(By.XPATH,'//*[@id="logMeIn"]/div/div/div/div/div/form/div[4]/button').click()
    sleep(randint(a,b))

    page_text = check_conferma(driver)
    robot  = "pulsante" in page_text
    sleep(randint(2,3))
    while robot==True:
       print("richiesta robot...")
       sleep(5)
       page_text = check_conferma(driver)
       creato = "pulsante" in page_text
       if creato == False:
            robot=False

    print("Accesso eseguito correttamente")

def Last_second(driver,xpath):
    conto_zeri = 0
    puntate = 0

    while True:
        print("Bene, procedo a controllare il countdown... ")
        body_text = check_conferma(driver)
        
        # Dividere il testo in righe
        lines = body_text.split('\n')
        # Controllare se ci sono abbastanza righe nel body
        if len(lines) >= 25:
        # Selezionare la 24esima riga e salvarla in una variabile
            linea_19 = lines[19]  # Poiché l'indice delle righe inizia da 0
            print("Contenuto della 19esima riga:", linea_19)
        else:
            print("Il body non ha abbastanza righe per ottenere la 24esima riga."
              )
            sleep(1)
            continue
        
        try:
            numero = int(linea_19)
            print("Conversione riuscita! Il numero è:", numero)
        except ValueError:
            print("La conversione in numero non è riuscita. Assicurati di inserire un valore numerico valido.")
            sleep(60)
            continue
        if numero == 1:
            conto_zeri = conto_zeri + 1
            print("Trovato uno zero...")
            if conto_zeri == 13:
                conto_zeri = 0
                puntate= puntate + 1
                #pyautogui.click(777,658)
                try:
                    element = driver.find_element(By.XPATH, xpath)
                    element.click()
                except NoSuchElementException:
                    input("Elemento non trovato. Potrebbe essere cambiato l'XPath o l'elemento non è presente.")
                except Exception as e:
                    input("Si è verificato un errore")
            
                print("Comprato")
                print(puntate," puntate totali")
                sleep(4)
        else:   
            print("non ancora..")

def generate_random_string(length):
    # definisce i caratteri alfanumerici possibili
    characters = string.ascii_letters + string.digits
    # genera una stringa casuale di lunghezza data
    return ''.join(random.choice(characters) for i in range(length))

def check_conferma(driver):
    try:
        # Aspetta che il corpo della pagina sia presente prima di estrarre il testo
        body_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
        page_text = body_element.text
        
    except Exception as e:
        print(f"Errore durante l'estrazione del testo: {str(e)}")
    return page_text


    



















