import requests
import time
import os
import random
import threading
from queue import Queue
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from rgbprint import gradient_print
from pystyle import *

"""
Copyright © 2024 Koraedn. All rights reserved.

BioFlooder is a proprietary software developed by Koraedn. The use, distribution, and modification of this software without explicit permission from the author are strictly prohibited. Unauthorized copying, reverse engineering, or distribution of this software, via any medium, is illegal and punishable under copyright law.

This software and associated documentation files are provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

For licensing inquiries, please contact Koraedn at 'koraedn' on Discord.

"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_screen():
    clear_screen()
    loading = r"""
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""          
             [>] Press Any Key To Continue
"""
    Anime.Fade(Center.Center(loading), Colors.green_to_white, Colorate.Horizontal, interval=0.0035, enter=True)

def print_menu():
    menu = r"""
                         __    _                         ┌───────────┬──────────────────────────────────┬──────────────┐
                    _wr""        "-q__                   │BioFlooder │ Coded By Koraedn. Daddy Koraeddy │ gg/gG5uRrt6VR│
                 _dP                 9m_                 ├───────────┴──────────────────────────────────┴──────────────┤
               _#P                     9#_               │Bioflooder is a tool designed for educational purposes only  │
              d#@                       9#m              │created by Daddy Koraeddy. It allows users to flood links    │
             d##                         ###             │with proxies and includes an antibot feature to enhance      │
            J###                         ###L            │functionality. However, please note that Daddy Koraeddy is   │
            {###K                       J###K            │not responsible for any silly or unintended damages that may │
            ]####K      ___aaa___      J####F            │occur from its use. Users are encouraged to employ this tool │
        __gmM######_  w#P""   ""9#m  _d#####Mmw__        │responsibly and within the bounds of applicable laws and     │
     _g##############mZ_         __g##############m_     │guidelines.       Aka Abyzms!!!                              │
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_   ├─────────────────────────────────────────────────────────────┤
  a###""          ,Z"#####@" '######"\g          ""M##m  │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
 J#@"             0L  "*##     ##@"  J#              *#K │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
 #"               `#    "_gmwgm_~    dF               `#_│Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
7F                 "#_   ]#####F   _dK                 JE│Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
]                    *m__ ##### __g@"                   F│Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
                       "PJ#####LP"                       │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
 `                       0######_                      ' │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
                       _0########_                       │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
     .               _d#####^#####m__              ,     │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
      "*w_________am#####P"   ~9#####mw_________w*"      │Koraeddy Daddy!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!│
          ""9@#####@M""           ""P@#####@M""          └─────────────────────────────────────────────────────────────┘
"""
    sys.stdout.write("\033[H\033[J")
    gradient_print(menu, start_color="light_green", end_color="green")

def load_proxy_t4u_thread_nuitka_file(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]
    return proxies

def nml_proxy_t4u_thread_nuitka_file(proxy):
    if not proxy.startswith(('http://', 'https://')):
        return [f'http://{proxy}', f'https://{proxy}']
    return [proxy]

def check_proxy(proxy):
    proxy_dict = {
        "http": proxy,
        "https": proxy
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxy_dict, timeout=2)
        if response.status_code == 200:
            return (proxy, True)
    except (requests.RequestException, requests.exceptions.SSLError):
        return (proxy, False)
    return (proxy, False)

def validate_proxy_t4u_thread_nuitka_file(proxies, max_workers=100):
    print_menu()
    valid_proxy_t4u_thread_nuitka_file = []
    total = len(proxies)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for proxy in proxies:
            for normalized_proxy in nml_proxy_t4u_thread_nuitka_file(proxy):
                futures.append(executor.submit(check_proxy, normalized_proxy))
        for i, future in enumerate(as_completed(futures), 1):
            proxy, is_valid = future.result()
            if is_valid and proxy not in valid_proxy_t4u_thread_nuitka_file:
                valid_proxy_t4u_thread_nuitka_file.append(proxy)
            valid_count = len(valid_proxy_t4u_thread_nuitka_file)
            sys.stdout.write(f"\rValid: {valid_count} | Scanned: {i}/{total * 2}")
            sys.stdout.flush()
    print()
    with open("VALIDS.txt", "w") as file:
        for proxy in valid_proxy_t4u_thread_nuitka_file:
            file.write(f"{proxy}\n")
    print(f"\nValid proxies saved inside of 'VALIDS.txt'")
    return valid_proxy_t4u_thread_nuitka_file

def visit_site(url, proxies, targeted_visit_size_t4u_nuitka, max_visits_per_second=1000):
    print_menu()
    user_agents = [
        "1 (1) 1 (1) 1",
    ]
    visited_count = 0
    failed_count = 0
    visit_queue = Queue()
    lock = threading.Lock()

    def visit(proxy):
        nonlocal visited_count, failed_count
        while True:
            try:
                proxy_dict = {
                    "http": proxy,
                    "https": proxy
                }
                headers = {
                    "User-Agent": random.choice(user_agents)
                }
                response = requests.get(url, proxies=proxy_dict, headers=headers, timeout=5)
                with lock:
                    if response.status_code == 200:
                        visited_count += 1
                        visit_queue.put(visited_count)
                    else:
                        failed_count += 1
            except Exception:
                with lock:
                    failed_count += 1

    def update_counter():
        while visited_count < targeted_visit_size_t4u_nuitka:
            time.sleep(0.1)
            visit_size_t4u_nuitka = visit_queue.qsize()
            sys.stdout.write(f"\rVisits: {visit_size_t4u_nuitka} | Failed: {failed_count}")
            sys.stdout.flush()

    print_menu()
    print(f"Flooding {url} until estimated {targeted_visit_size_t4u_nuitka} visits...")
    counter_t4u_thread_nuitka = threading.Thread(target=update_counter)
    counter_t4u_thread_nuitka.start()
    with ThreadPoolExecutor(max_workers=max_visits_per_second) as executor:
        futures = [executor.submit(visit, proxy) for proxy in proxies]
        for future in as_completed(futures):
            pass
    counter_t4u_thread_nuitka.join()
    print(f"\n[>] Estimated Visits: {visited_count}")
    print(f"Failed: {failed_count}")
    center.print("BioFlooder")

def main():
    os.system('BioFlooder | Koraedn')
    loading_screen()
    print_menu()
    proxy_t4u_thread_nuitka_file = input("[>] Proxies text file: ").strip().strip('"')
    if not os.path.isfile(proxy_t4u_thread_nuitka_file):
        print("Not a file path.")
        return

    proxies = load_proxy_t4u_thread_nuitka_file(proxy_t4u_thread_nuitka_file)
    if not proxies:
        print("0 proxies found.")
        return

    print_menu()
    use_all_proxies = input("[>] Use all proxies (y/n)? ").strip().lower() == 'y'

    if use_all_proxies:
        valid_proxy_t4u_thread_nuitka_file = proxies
    else:
        valid_proxy_t4u_thread_nuitka_file = validate_proxy_t4u_thread_nuitka_file(proxies)

    print(f"Proxies found: {len(valid_proxy_t4u_thread_nuitka_file)}")
    if not valid_proxy_t4u_thread_nuitka_file:
        print("No valid proxies found.")
        return

    print_menu()
    url = input("[>] URL: ").strip()
    targeted_visit_size_t4u_nuitka = int(input("[>] Attempted Flood Count: ").strip())
    visit_site(url, valid_proxy_t4u_thread_nuitka_file, targeted_visit_size_t4u_nuitka)

if __name__ == "__main__":
    main()