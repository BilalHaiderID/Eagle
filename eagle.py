#!/bin/python3
#author:@bilalhaiderid
#_________[ IMPORTING MODULES ]_________>>
import os,sys,re,json,time,wget
from mailtm import Email
from faker import Faker
from bs4 import BeautifulSoup
import random,requests,subprocess
from concurrent.futures import ThreadPoolExecutor
#_________[ BASIC COLOURS ]_________>>
coloff = "\033[0m"         # NoColour
red = "\033[1;31m"         # Red
green = "\033[1;32m"       # Green
white = "\033[1;37m"       # Blue
blue = "\033[1;34m"        # White
#_________[ SCRIPT SETTINGS ]_________>>
try:
    script_data = open('.data/settings.json','r')
except:
    print(f"[{green}+{coloff}] Downloading Script Setting File")
    try:
        wget.download("https://raw.githubusercontent.com/BilalHaiderID/Eagle/main/.data/settings.json",out=".data")
    except Exception as e:
        exit(e)
    finally:
        print(f"\n[{green}+{coloff}] Downloading Done Successfully")

script_data = open('.data/settings.json','r').read()
script_data = json.loads(script_data)
if script_data['colour'] == 'green':maincol = green
elif str(script_data['colour']) == 'red':maincol = red
elif str(script_data['colour']) == 'white':maincol = white
elif str(script_data['colour']) == 'blue':maincol = blue
elif str(script_data['colour']) == '':maincol = coloff
#_________[ MAILTM ]_________>>
def mailTm_listener(message):
    print(f"[{maincol}+{coloff}] Subject: " + message['subject'])
    print(f"[{green}+{coloff}] Content: " + message['text'] if message['text'] else message['html'])
def mailTM():
    logo()
    username = input(f"[{maincol}+{coloff}] Input Username [Random] : ")
    password = input(f"[{maincol}+{coloff}] Input Password [Random] : ")
    domain = input(f"[{maincol}+{coloff}] Input Domain [exelica.com] : ")
    mail = Email()
    if username in ['',' ']:username=None
    if password in ['',' ']:password=None
    if domain in ['',' ']:domain=None
    mail.register(username=username,password=password,domain=domain)
    print(f"\n[{maincol}+{coloff}] Email Adress: " + str(mail.address))
    print(f"[{maincol}+{coloff}] Waiting for new emails...")
    print(f"{coloff}----------------------------------------------------")
    mail.start(mailTm_listener)
#_________[ TOKEN PER ]_________>>
def req_info_token(cookie,token):
    session = requests.Session()
    try:
        url    = 'https://developers.facebook.com/tools/debug/accesstoken/?access_token=%s&version=v15.0'%(token)
        req = BeautifulSoup(session.get(url,cookies={'cookie':cookie}).content,'html.parser')
        crf = req.find('a',href='/docs/reference/login/#permissions').text
        print(f"[{maincol}+{coloff}] Permissions : {maincol}{crf}{coloff}")
    except Exception as e:
        print(f"{e}")
#_________[ TOKEN GENERATE ]_________>>
def generate_token():
    logo()
    cookie = input(f'[{maincol}->{coloff}] Input Cookie : ')
    session = requests.Session()
    try:
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = session.get(url,cookies={'cookie':cookie})
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = session.get(nek,cookies={'cookie':cookie})
        token = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        # print(f"{coloff}{'EAAB':-^54}")
        print(f"{coloff}----------------------------------------------------")
        print(f"[{maincol}+{coloff}] EAAB Token : {maincol}{token}{coloff}")
        req_info_token(cookie,token)
    except Exception as e:
        print(f'{e}')
    try:
        url = 'https://business.facebook.com/business_locations'
        req = session.get(url,cookies={'cookie':cookie})
        token = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        print(f"{coloff}----------------------------------------------------")
        print(f"[{maincol}+{coloff}] EAAG Token : {maincol}{token}{coloff}")
        req_info_token(cookie,token)
    except Exception as e:
        print(f'{e}')
    try:
        url = 'https://www.facebook.com/events_manager2/overview'
        req = session.get(url,cookies={'cookie':cookie})
        token = re.search('{"accessToken":"(EAAd\w+)',req.text).group(1)
        print(f"{coloff}----------------------------------------------------")
        print(f"[{maincol}+{coloff}] EAAD Token : {maincol}{token}{coloff}")
        req_info_token(cookie,token)
    except Exception as e:
        print(f'{e}')
#_________[ FAKE INFO ]_________>>
def fake_info():
    logo()
    fake = Faker()
    address = str(fake.address()).replace('\n','')
    print(f'[{maincol}+{coloff}] Name : {fake.name()}')
    print(f"[{maincol}+{coloff}] Address : {address}")
    print(f'[{maincol}+{coloff}] Email : {fake.email()}')
    print(f'[{maincol}+{coloff}] City : {fake.city()}')
    print(f'[{maincol}+{coloff}] Country : {fake.country()}')
    print(f'[{maincol}+{coloff}] Country Code : {fake.country_code()}')
    print(f'[{maincol}+{coloff}] Date OF Birth : {fake.date_of_birth()}')
    print(f'[{maincol}+{coloff}] Domain Name : {fake.domain_name()}')
    print(f'[{maincol}+{coloff}] Image URL : {fake.image_url()}')
    print(f'[{maincol}+{coloff}] IPv4 : {fake.ipv4()}')
    print(f'[{maincol}+{coloff}] IPv6 : {fake.ipv6()}')
    print(f'[{maincol}+{coloff}] Phone Number : {fake.phone_number()}')
    print(f'[{maincol}+{coloff}] Password : {fake.password()}')
    print(f'[{maincol}+{coloff}] Timezone : {fake.timezone()}')
    print(f'[{maincol}+{coloff}] Zipcode : {fake.zipcode()}')
#_________[ LOGO ]_________>>
def logo(time_sleep=0.5):
    time.sleep(time_sleep)
    os.system("clear")
    time.sleep(time_sleep)
    print(f"""{coloff}
   ___________              .__          
   \_   _____/____     ____ |  |   ____  
    |    __)_\__  \   / ___\|  | _/ __ \ 
    |        \/ __ \_/ /_/  >  |_\  ___/ 
   /_______  (____  /\___  /|____/\___  >
           \/     \//_____/           \/  {maincol} {script_data['version']} {coloff}""")
    print(f"{coloff}----------------------------------------------------")
    print(f"{maincol} No Technology thats connected to internet is{coloff}")
    print(f"{maincol}                  Unhackable{coloff}")
    print(f"{coloff}----------------------------------------------------")
#_________[ MAIN MENU ]_________>>
def main():
    logo()
    print("[{}01{}] ".format(maincol,coloff))
    print("[{}02{}] ".format(maincol,coloff))
    print("[{}03{}] ".format(maincol,coloff))
    print("[{}04{}] ".format(maincol,coloff))
    print("[{}05{}] ".format(maincol,coloff))
    print("[{}06{}] ".format(maincol,coloff))
    print("[{}07{}] ".format(maincol,coloff))
    print("[{}08{}] ".format(maincol,coloff))
    print("[{}09{}] ".format(maincol,coloff))
    print("[{}10{}] ".format(maincol,coloff))
    print("[{}11{}] ".format(maincol,coloff))
    print("[{}12{}] ".format(maincol,coloff))
    print(f"{coloff}----------------------------------------------------")
    maininp = input(f"[{green}->{coloff}] Select in option : ")


if __name__=='__main__':pass
    # generate_token()
    # mailTM()
    # fake_info()