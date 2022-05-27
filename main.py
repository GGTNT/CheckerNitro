import colorama
import requests
import os
import random
import time
import psutil
from discord_webhook import DiscordWebhook
os.system("title Nitro Generator https://github.com/GGTNT")
LICENCE = colorama.Fore.BLUE + """
Copyright (c) 2022 https://github.com/GGTNT
"""
VERSION =  "1.3"
def slowType(text: str, speed: float, newLine=True):
    for i in text:  
        
        print(i, end="", flush=True)
        time.sleep(speed)  
    if newLine:  
        print()  
slowType(LICENCE + colorama.Fore.YELLOW + "Version : " + VERSION,0.01)
slowType(colorama.Fore.WHITE+"Voulez vous utilisez un webhook (Y/N) : ",0.01,newLine=False)
url_web_y = input()
if url_web_y == "Y" or url_web_y == "y":
    slowType("Entrer l'url du webhook : ",0.01,newLine=False)
    url_web = input()
    webhook = DiscordWebhook(url=url_web, rate_limit_retry=True,
                         content='Le générateur vient de démarer, vous recevrez un message ici quand un code nitro **VALIDE** sera trouver.')
    try:
        response = webhook.execute()
    except requests.exceptions.MissingSchema:
        print(colorama.Fore.RED+"Url invalide"+colorama.Fore.RESET)
        print("Le programme va se fermer...")
        time.sleep(3)
        exit()
else:
    pass
slowType(colorama.Fore.WHITE+"Veuillez chosir les cpu (default=0.01) : ",0.01,newLine=False)
try:
    cpu = float(input())
except ValueError:
    pass
    cpu = 0.01
code_tester = 0
while True:
    psutil.cpu_percent(interval=cpu)
    code_tester = code_tester + 1
    os.system(f"title Nitro Generator https://github.com/GGTNT                                       code tester : {code_tester}, cpu : {cpu}")
    nitro = ""
    dico = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(16):
        nitro = f"{nitro}{random.choice(dico)}"
    r = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true")
    if r.ok:
        os.system("cls")
        print(colorama.Fore.GREEN + f"[v] https://discord.com/gifts/{nitro}")
        webhook = DiscordWebhook(url=url_web, rate_limit_retry=True,
                     content=f'Nitro trouver : {nitro}')
        response = webhook.execute()
        with open("code.txt","a+") as f:
            f.write(f"https://discord.com/gifts/{nitro}")
            f.close()
        exit()
    else:
        print(colorama.Fore.RED + f'[i] https://discord.com/gifts/{nitro}')