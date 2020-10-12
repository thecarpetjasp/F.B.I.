import os
import colorama
from colorama import Fore, Style
os.system("sudo pip3 install colorama")
os.system("sudo chmod +x fbi.py")
os.system("sudo mv fbi.py /usr/bin/fbi")
os.system("cls||clear")
print ("F.B.I has been successfully installed\nType", Fore.YELLOW + "fbi", Style.RESET_ALL + "anywhere in your terminal to run the script.")
