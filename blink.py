# Create By Monnalisa-ID
# Bot Safelinku Version BETA
# DECODE = LEMAH!
# Susah Susah Buat Malah di decode anjg emang!
import time
import sys
import random
import os
from os import system, name
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
import requests
from multiprocessing.pool import ThreadPool
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
hijau = Style.RESET_ALL + Style.BRIGHT + Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.DIM + Fore.WHITE
biru = Style.RESET_ALL + Style.BRIGHT + Fore.BLUE
ungu2 = Style.NORMAL + Fore.MAGENTA
ungu = Style.RESET_ALL + Style.BRIGHT + Fore.MAGENTA
hijau2 = Style.NORMAL + Fore.GREEN
yellow2 = Style.NORMAL + Fore.YELLOW
yellow = Style.RESET_ALL + Style.BRIGHT + Fore.YELLOW
red2 = Style.NORMAL + Fore.RED
red = Style.RESET_ALL + Style.BRIGHT + Fore.RED
cyan = Style.BRIGHT + Fore.CYAN
cyan2 = Style.NORMAL + Fore.CYAN
des = Style.BRIGHT + Fore.GREEN + "『🔥』"
kur1 = Style.BRIGHT + Fore.RED + "["
kur2 = Style.BRIGHT + Fore.RED + "]"

print(f"""{biru}
╔╗ ┌─┐┌┬┐ ╔═╗┌─┐┌─┐┌─┐┬  ┬┌┐┌┬┌─┬ ┬
╠╩╗│ │ │  ╚═╗├─┤├┤ ├┤ │  ││││├┴┐│ │
╚═╝└─┘ ┴  ╚═╝┴ ┴└  └─┘┴─┘┴┘└┘┴ ┴└─┘Cap OT\n{hijau}OT Version : amer arak ciu-ciu kawa-kawa\n""")
time.sleep(3)
print('_' * 60)
print(f"""{cyan2}selamat datang tuanku\n{red}Created By mabok heula ID\n{hijau}Contact Me on : babah botak cap OT\n{red}Ieu mah Versi final|ngajeod we sia mah""")
time.sleep(5)

print("\n")
print('=' * 60)

time.sleep(1)

kw = input(f"{cyan}Asupkeun Link siana (Safelinku)\n{hijau}contohna jiga kieu :https://semawur.com/xxxxxx : ")
time.sleep(1)
os.system('clear')

time.sleep(3)
print("link sia sukses di input bray, dagoan urang kocok heula nepi ka bucat....")

# Baca user-agent dari file ua.txt
with open('ua.txt', 'r') as ua_file:
    user_agents = ua_file.read().splitlines()
    user_agent = random.choice(user_agents)  # Pilih user-agent secara acak

pl = []
prolist = requests.get("https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt").text
prolist1 = requests.get("https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt").text
prolist2 = requests.get("https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt").text
dl = []
for i in prolist.splitlines():
    pl.append(i)

for i in prolist1.splitlines():
    pl.append(i)

for i in prolist2.splitlines():
    pl.append(i)
my_url = kw

def tri(i):
    try:
        if requests.get(my_url, proxies={"https": "https://" + i}, timeout=0.4).status_code == 200:
            print(i)
            tro(i)
    except Exception as e:
        print(f"Error in tri: {e}")

def fres(driver):
    try:
        driver.refresh()
        driver.minimize_window()
    except Exception as e:
        print(f"Error in fres: {e}")

def tro(i):
    try:
        firefox_options = Options()
        firefox_options.add_argument("--proxy-server=" + i)
        firefox_options.add_argument(f"user-agent={user_agent}")
        service = FirefoxService(executable_path='/home/coder/btbtah/geckodriver')
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.get("https://github.com/Monnalisa-ID")
        driver.get(my_url)
        dl.append(driver)
    except Exception as e:
        print(f"Error in tro: {e}")

service = FirefoxService(executable_path='/home/coder/btbtah/geckodriver')
opts = Options()
opts.add_argument(f"user-agent={user_agent}")
try:
    driver = webdriver.Firefox(service=service, options=opts)
    driver.get(my_url)
except Exception as e:
    print(f"Error initializing WebDriver: {e}")

tp = ThreadPool(5000)
tp.map(tri, pl)

tp = ThreadPool(300)
tp.map(fres, dl)

print("Job Done")
