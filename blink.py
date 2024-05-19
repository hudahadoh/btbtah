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
╚═╝└─┘ ┴  ╚═╝┴ ┴└  └─┘┴─┘┴┘└┘┴ ┴└─┘With Selenium\n{hijau}Bot Version : FINAL\n""")
time.sleep(3)
print('_' * 60)
print(f"""{cyan2}SELAMAT DATANG TUANKU\n{red}Created By Gigoloco ID\n{hijau}Contact Me on : https://github.com/Monnalisa-ID\n{red}This Version Final""")
time.sleep(5)

print("\n")
print('=' * 60)

time.sleep(1)

kw = input(f"{cyan}Enter Link sia Tuanku (Safelinku)\n{hijau}example :https://locoloc.com/xxxxxx : ")
time.sleep(1)
os.system('clear')

time.sleep(3)
print("Link tuanku sukses diinput, ke di kocok heula geus bucat di kabaran ku aing ka tuanku....")

# Baca user-agent dari file ua.txt
with open('ua.txt', 'r') as ua_file:
    user_agents = ua_file.read().splitlines()
    user_agent = random.choice(user_agents)  # Pilih user-agent secara acak

pl = []
prolist = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.txt").text
prolist1 = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.csv").text
prolist2 = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.json").text
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
