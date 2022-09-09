from follow_bot import spotify
import threading, os, time
from colorama import Fore, init

cmd = 'mode 50,30'
os.system(cmd)

print(f"{Fore.RED}                     __\n                _   /  |\n              | \  \/_/\n               \_\| / __              \n                  \/_/__\           .--='/~\ \n           ____,__/__,_____,______)/   /[~]]]\n            -,-----,--\--,-----,---,\'-' [[~]]\n        Spotify Bot__/\_            '--=.\]/\n                  /_/ |\\\n                       \/\n\n")
print(f"\n           {Fore.YELLOW}[ + ]{Fore.YELLOW} Spotify Auto | [{Fore.GREEN}Online{Fore.RESET}{Fore.YELLOW}]{Fore.YELLOW}")
print(f"           {Fore.YELLOW}[ + ]{Fore.YELLOW} Proxy status | [{Fore.GREEN}Online{Fore.RESET}{Fore.YELLOW}]{Fore.YELLOW}")
print(f"\n    {Fore.RED}All services are running smoothly! 9k/day{Fore.RED}")

lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
spotify_profile = str(input("Spotify Link or Username: "))
threads = int(input("\nThreads: "))


def load_proxies():
    if not os.path.exists("proxies.txt"):
        print("\nFile proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nNo proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print("\n[1] Proxies\n[2] Proxyless")
option = int(input("\n> "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print(f"{Fore.RESET}[{Fore.GREEN}SUCCESS{Fore.RESET}] " + "Followed ({})".format(counter))
    else:
        time.sleep(1)

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0
