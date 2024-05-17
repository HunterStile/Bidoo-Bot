from funzioni.bidoo_functions import *
import pandas as pd
import pyautogui



#variabili
xpath_tamplate = '//*[@id="{}"]/div[3]/section[1]/div/section[1]/a'
file_bidoo = 'account_bidoo.csv'


## >main<
print("Benvenuti nel bot di bidoo by HunterStile!")


with open(file_bidoo, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # salta la prima riga con l'intestazione
    for row in csvreader:
        count = count + 1
        print(count,'° riproduzione')
        email = row[0]
        password = row[2]
        driver = configurazione_browser()
        sleep(randint(a,b))
        accesso_bidoo(driver,email,password)
        yop_click(driver,email)
        prendere_puntate(driver)


input("Tutti i busting sono stati eseguiti!")





