from funzioni.bidoo_functions import *
import pandas as pd
import pyautogui

#variabili
xpath_tamplate = '//*[@id="{}"]/div[3]/section[1]/div/section[1]/a'
file_bidoo = 'account_bidoo.csv'

key = 'NAN'
while key != 'no':
    driver = configurazione_browser()
    creazione_bidoo(driver)
    key = input("Se vuoi continuare a creare premi enter, altrimenti scrivi 'no'")












