# Code by @desvasicek
# © 2022 Des
# MIT License
import subprocess
from colorama import init, Fore, Back, Style
import os, getpass, sys
import requests
path = os.path.dirname(os.path.abspath(__file__))
licensefile = open(f"{path}/LICENSE", mode="r")
creditsfile = open(f"{path}/CREDITS", mode="r")
infofile = open(f"{path}/INFO", mode="r")
init()
done = False
print(f"{Fore.WHITE}{Style.BRIGHT}Welcome to PyShell, a shell entirely built in python.\nSee an issue? Report it on Github https://github.com/desvasicek/PyShell\n{Style.DIM}Type 'credits' for credits, 'license' for the license, or 'info' for more information{Style.RESET_ALL}")
response = requests.get('https://raw.githubusercontent.com/desvasicek/PyShell/master/main.py')
if not open(__file__, mode="r") == response.text:
    print(f"\n{Style.BRIGHT}{Fore.RED}Your version of PyShell is outdated, we reccommend you update it. Type 'info' for more information.{Style.RESET_ALL}\n")
while not done:
    cmd = input(f"{Style.BRIGHT}{Fore.GREEN}{getpass.getuser()}@{os.uname()[1]}{Style.RESET_ALL}:{Style.BRIGHT}{Fore.BLUE}~ ${Style.RESET_ALL} ")
    try:
        if not "NANO" in cmd.upper() and not "CD" in cmd.upper():
            if cmd.upper() == "INFO":
                print(f"{Fore.BLUE}{Style.BRIGHT}{infofile.read()}{Style.RESET_ALL}")
            elif cmd.upper() == "CREDITS":
                print(f"{Style.BRIGHT}{Fore.BLUE}{creditsfile.read()}{Style.RESET_ALL}")
            elif cmd.upper() == "LICENSE":
                print(f"{Style.BRIGHT}{Fore.BLUE}{licensefile.read()}{Style.RESET_ALL}")
            elif cmd.upper == "QUIT":
                done = True
            else:
                p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                for line in iter(p.stdout.readline, b''):
                    print(f"{line.decode('utf8').strip()}")
                p.stdout.close()
                p.wait()
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Sorry, that command is not available. Type 'info' for more information.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}Invalid command.{Style.RESET_ALL}")
        print(f"{Style.NORMAL}{Fore.RED}{e}{Style.RESET_ALL}")
creditsfile.close()
licensefile.close()
quit()
    
