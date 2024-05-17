from funzioni.bidoo_functions import *
import pandas as pd
import pyautogui

username = 'TUO_USERNAME'
password = 'TUA_PASSWORD'

#variabili
xpath_tamplate = '//*[@id="{}"]/div[3]/section[1]/div/section[1]/a'
file_bidoo = 'account_bidoo.csv'

## >main<
print("Benvenuti nel bot di bidoo by HunterStile!")
driver = configurazione_browser()
accesso_bidoo(driver,username,password)
asta = input("Seleziona l'asta(inseire DA come iniziale): ")
xpath = xpath_tamplate.format(asta)
Last_second(driver,xpath)











