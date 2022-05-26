import colorama
import requests
import os
import random
import time
LICENCE = colorama.Fore.BLUE + """
Copyright (c) 2022 https://github.com/GGTNT
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
VERSION =  "1.0"
print(LICENCE + colorama.Fore.YELLOW + "Version : " + VERSION)
time.sleep(5)
while True:
    nitro = ""
    dico = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(16):
        nitro = f"{nitro}{random.choice(dico)}"
    r = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true")
    if r.ok:
        os.system("cls")
        print(colorama.Fore.GREEN + f"[v] https://discord.com/gifts/{nitro}")
        with open("code.txt","a+") as f:
            f.write(f"https://discord.com/gifts/{nitro}")
            f.close()
        exit()
    else:
        print(colorama.Fore.RED + f'[i] https://discord.com/gifts/{nitro}')