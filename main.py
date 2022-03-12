import os
import pyautogui
import time
from dhooks import Webhook
from pystyle import Colors, Colorate
import requests


clear = lambda: os.system('cls')

os.system("title EXORTIX")



def main():

    print(Colorate.Vertical(Colors.purple_to_blue, exortix, 1))


    a = input("\n\n 1- Webhooks Spammer\n 2- Webhooks Delete \n\n Fait un choix -->")

    if a == '1':
        webspammer()    
    if a == '2':
        webdel()    



def webspammer():
    clear()

    print(Colorate.Vertical(Colors.purple_to_blue, websp, 1))

    b = input("\n\n 1- x10Message \n\n 2- x50Message \n\n 3- x100Message \n\n 4- x500Message \n\n 5- x1000Message\n\n\n Fait un choix --> ")

    if b == '1':
        un()
    if b == '2':
        deux() 
    if b == '3':
        trois()
    if b == '4':
        quatre()
    if b == '5':
        cinq()

def un():
    hook = Webhook(input("\n\n Votre Webhooks --> "))
    webmsg = input("\n Le message du webhooks --> ")
    for i in range(10):
        hook.send((webmsg))
        print("[+]Message envoyé")

def deux():
    hook = Webhook(input("\n\n Votre Webhooks --> "))
    webmsg = input("\n Le message du webhooks --> ")
    for i in range(50):
        hook.send((webmsg))
        print("[+]Message envoyé")

def trois():
    hook = Webhook(input("\n\n Votre Webhooks --> "))
    webmsg = input("\n Le message du webhooks --> ")
    for i in range(100):
        hook.send((webmsg))
        print("[+]Message envoyé")

def quatre():
    hook = Webhook(input("\n\n Votre Webhooks --> "))
    webmsg = input("\n Le message du webhooks --> ")
    for i in range(500):
        hook.send((webmsg))
        print("[+]Message envoyé")        

def cinq():
    hook = Webhook(input("\n\n Votre Webhooks --> "))
    webmsg = input("\n Le message du webhooks --> ")
    for i in range(1000):
        hook.send((webmsg))
        print("[+] Message envoyé")

def webdel():
    clear()
    print(Colorate.Vertical(Colors.purple_to_blue, websp, 1))
    webhook = input("\n \n Webhook -->")
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(Colors.green("\n [+] Webhook Delete\n"))
        input(" [+] Press Enter")
    elif check.status_code == 200:
        print(Colors.red("\n [-] Error"))
        input(" [+] Press Enter")

        
websp = ('''                     /$$      /$$ /$$$$$$$$ /$$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$
                    | $$  /$ | $$| $$_____/| $$__  $$| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/
                    | $$ /$$$| $$| $$      | $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$ /$$/ 
                    | $$/$$ $$ $$| $$$$$   | $$$$$$$ | $$$$$$$$| $$  | $$| $$  | $$| $$$$$/  
                    | $$$$_  $$$$| $$__/   | $$__  $$| $$__  $$| $$  | $$| $$  | $$| $$  $$  
                    | $$$/ \  $$$| $$      | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$\  $$ 
                    | $$/   \  $$| $$$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$
                    |__/     \__/|________/|_______/ |__/  |__/ \______/  \______/ |__/  \__/''')

exortix = ('''                   /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$ /$$   /$$
                  | $$_____/| $$  / $$ /$$__  $$| $$__  $$|__  $$__/|_  $$_/| $$  / $$
                  | $$      |  $$/ $$/| $$  \ $$| $$  \ $$   | $$     | $$  |  $$/ $$/
                  | $$$$$    \  $$$$/ | $$  | $$| $$$$$$$/   | $$     | $$   \  $$$$/ 
                  | $$__/     >$$  $$ | $$  | $$| $$__  $$   | $$     | $$    >$$  $$ 
                  | $$       /$$/\  $$| $$  | $$| $$  \ $$   | $$     | $$   /$$/\  $$
                  | $$$$$$$$| $$  \ $$|  $$$$$$/| $$  | $$   | $$    /$$$$$$| $$  \ $$
                  |________/|__/  |__/ \______/ |__/  |__/   |__/   |______/|__/  |__/''')

        

if __name__ == "__main__":
    while True:
        clear()
        main()