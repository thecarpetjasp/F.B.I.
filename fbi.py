#!/usr/bin/env python3
import json
import requests
import os
import colorama
from colorama import Fore, Style

#######################################################################################
#Please enter your API keys below. Make sure to insert inbetween the "Quotation Marks".
#######################################################################################
global API_KEY_ADDRESS, API_KEY_EMAIL, API_KEY_PHONE
API_KEY_ADDRESS = ("")
API_KEY_EMAIL = ("")
API_KEY_PHONE = ("")

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

os.system("cls||clear")

def main():
    while True:
        print (Fore.YELLOW + "█████", end="")
        print ("██╗██████╗  ", end="")
        print ("  ██╗\n██╔════╝██╔", end="")
        print ("══██╗   ██║\n█████╗  ███", end="")
        print ("███╔╝   ██║\n██╔══╝  ██╔══██", end="")
        print ("╗   ██║\n██║", Fore.WHITE + "█", sep="", end="")
        print ("█╗" + Fore.YELLOW + "  ████", sep="", end="")
        print ("██╔╝" + Fore.WHITE + "█", sep="", end="")
        print ("█╗" + Fore.YELLOW + "█", sep="", end="")
        print ("█║",Fore.WHITE + "██╗", sep ="")
        print ("╚═╝" + Fore.WHITE + "╚═", end="")
        print ("╝" + Fore.YELLOW + "  ╚══", end="")
        print ("═══╝" + Fore.WHITE + " ", end="")
        print ("╚═╝" + Fore.YELLOW + "╚═╝", Fore.WHITE + "╚═╝", sep="", end=" ")
        print (Fore.WHITE + "by", Fore.YELLOW + color.BOLD + "Jack Carter", color.END)
        print (Fore.YELLOW + "Find", Fore.WHITE + ".", sep="", end="    ")
        print (Fore.YELLOW + "Big", Fore.WHITE + ".", sep="", end="     ")
        print (Fore.YELLOW + "Info", Fore.WHITE + ".", sep="", end="")
        print ("\n \n \n")
        print (Fore.WHITE + color.BOLD + "[", Fore.YELLOW + "1", Fore.WHITE + "]", sep="", end=" ")
        print (Fore.WHITE + color.BOLD + "Reverse Search Address\n ", color.END)
        print (Fore.WHITE + color.BOLD + "[", Fore.YELLOW + "2", Fore.WHITE + "]", sep="", end=" ")
        print (Fore.WHITE + color.BOLD + "Reverse Search Email Address\n ", color.END)
        print (Fore.WHITE + color.BOLD + "[", Fore.YELLOW + "3", Fore.WHITE + "]", sep="", end=" ")
        print (Fore.WHITE + color.BOLD + "Reverse Search Phone Number\n \n \n", color.END)
        direct_choice = input(Fore.WHITE + "Please choose by " + Fore.YELLOW + color.BOLD + "number " + Fore.WHITE + color.END + "or type " + Fore.YELLOW + color.BOLD + "exit " + Fore.WHITE + color.END + "to close: " + Fore.YELLOW + color.BOLD) 
        if direct_choice == ("1"):
            os.system("cls||clear")
            address_line_1 = input(Style.RESET_ALL + '*HIT ENTER TO LEAVE BLANK*\n' + Fore.YELLOW + '---------------------------\n' + Fore.WHITE + color.BOLD + 'Address Line 1: ' + color.END + Fore.YELLOW)
            new_line_1 = (address_line_1.replace(" ", "+"))
            print (Fore.WHITE + color.BOLD)
            address_line_2 = input('Address Line 2: ' + color.END + Fore.YELLOW)
            new_line_2 = (address_line_2.replace(" ", "+"))
            print (Fore.WHITE + color.BOLD)
            city = input('City: ' + color.END + Fore.YELLOW)
            new_city = (city.replace(" ", "+"))
            print (Fore.WHITE + color.BOLD)
            state_code = input('State code: ' + color.END + Fore.YELLOW)
            print (Fore.WHITE + color.BOLD)
            post_code = input('Postal Code: ' + color.BOLD + Fore.YELLOW)
            new_post_code = (post_code.replace(" ", ""))
            print (Fore.WHITE + color.BOLD)
            country_code = input('Country code ' + color.END + '(Eg: ' + Fore.YELLOW +  'US' + Fore.WHITE + ',' + Fore.YELLOW + ' UK' + Fore.WHITE + ' etc.): ' + Fore.YELLOW)
            print ("")
            url = ('https://api.ekata.com/3.0/location?api_key=' + API_KEY_ADDRESS + '&street_line_1=' + new_line_1 + '&street_line_2=' + new_line_2 + '&city=' + new_city + '&state_code=' + state_code + '&postal_code=' + new_post_code + '&country_code=' + country_code)
            response = requests.get(url)
            todos = json.loads(response.text)
            print ("")
            print (Fore.YELLOW + color.BOLD + "***************************************************************************")
            print (Fore.WHITE + color.BOLD + json.dumps(todos, indent=1))
            print (Fore.YELLOW + color.BOLD + "***************************************************************************" + color.END)
            print ("")
            print ("")
            print ("")
            back_close = input(Fore.WHITE + 'Type ' + Fore.YELLOW + color.BOLD + 'back ' + Fore.WHITE + color.END + 'to return to directory. Otherwise, hit any key to close the script: ' + Fore.YELLOW + color.BOLD)
            if back_close == ("back"):
                os.system("cls||clear")
                main ()
            else:
                os.system("cls||clear")
                print (color.END + Fore.YELLOW + "█████", end="")
                print ("██╗██████╗  ", end="")
                print ("  ██╗\n██╔════╝██╔", end="")
                print ("══██╗   ██║\n█████╗  ███", end="")
                print ("███╔╝   ██║\n██╔══╝  ██╔══██", end="")
                print ("╗   ██║\n██║", Fore.WHITE + "█", sep="", end="")
                print ("█╗" + Fore.YELLOW + "  ████", sep="", end="")
                print ("██╔╝" + Fore.WHITE + "█", sep="", end="")
                print ("█╗" + Fore.YELLOW + "█", sep="", end="")
                print ("█║", Fore.WHITE + "██╗", sep ="")
                print ("╚═╝" + Fore.WHITE + "╚═", end="")
                print ("╝" + Fore.YELLOW + "  ╚══", end="")
                print ("═══╝" + Fore.WHITE + " ", end="")
                print ("╚═╝" + Fore.YELLOW + "╚═╝", Fore.WHITE + "╚═╝", sep="", end=" ")
                print (Fore.WHITE + "by", Fore.YELLOW + color.BOLD + "Jack Carter", color.END)
                print (Fore.YELLOW + "Find", Fore.WHITE + ".", sep="", end="    ")
                print (Fore.YELLOW + "Big", Fore.WHITE + ".", sep="", end="     ")
                print (Fore.YELLOW + "Info", Fore.WHITE + ".", sep="", end="")
                print ("\n")
                break
            return
        elif direct_choice == ("2"):
            os.system("cls||clear")
            email_address = input(Fore.WHITE + color.BOLD + 'Email Address: ' + color.END + Fore.YELLOW)
            new_email = (email_address.replace("@", "%40"))
            url = ('https://api.ekata.com/4.1/email?api_key=' + API_KEY_EMAIL + '&email_address=' + new_email)
            response = requests.get(url)
            todos = json.loads(response.text)
            print ("")
            print (Fore.YELLOW + color.BOLD + "***************************************************************************")
            print (Fore.WHITE + color.BOLD + json.dumps(todos, indent=1))
            print (Fore.YELLOW + color.BOLD + "***************************************************************************" + color.END)
            print ("")
            print ("")
            print ("")
            back_close = input(Fore.WHITE + 'Type ' + Fore.YELLOW + color.BOLD + 'back ' + Fore.WHITE + color.END + 'to return to directory. Otherwise, hit any key to close the script: ' + Fore.YELLOW + color.BOLD)
            if back_close == ("back"):
                os.system("cls||clear")
                main ()
            else:
                os.system("cls||clear")
                print (color.END + Fore.YELLOW + "█████", end="")
                print ("██╗██████╗  ", end="")
                print ("  ██╗\n██╔════╝██╔", end="")
                print ("══██╗   ██║\n█████╗  ███", end="")
                print ("███╔╝   ██║\n██╔══╝  ██╔══██", end="")
                print ("╗   ██║\n██║", Fore.WHITE + "█", sep="", end="")
                print ("█╗" + Fore.YELLOW + "  ████", sep="", end="")
                print ("██╔╝" + Fore.WHITE + "█", sep="", end="")
                print ("█╗" + Fore.YELLOW + "█", sep="", end="")
                print ("█║", Fore.WHITE + "██╗", sep ="")
                print ("╚═╝" + Fore.WHITE + "╚═", end="")
                print ("╝" + Fore.YELLOW + "  ╚══", end="")
                print ("═══╝" + Fore.WHITE + " ", end="")
                print ("╚═╝" + Fore.YELLOW + "╚═╝", Fore.WHITE + "╚═╝", sep="", end=" ")
                print (Fore.WHITE + "by", Fore.YELLOW + color.BOLD + "Jack Carter", color.END)
                print (Fore.YELLOW + "Find", Fore.WHITE + ".", sep="", end="    ")
                print (Fore.YELLOW + "Big", Fore.WHITE + ".", sep="", end="     ")
                print (Fore.YELLOW + "Info", Fore.WHITE + ".", sep="", end="")
                print ("\n")
                break
            return
        elif direct_choice == ("3"):
            os.system("cls||clear")
            phone_area = input(Fore.WHITE + color.BOLD + 'Area code \n(Eg: ' + Fore.YELLOW + color.BOLD + '+44 ' + Fore.WHITE + color.BOLD + 'etc. Must include even for landline): ' + color.END + Fore.YELLOW)
            print ("")
            phone_num = input(Fore.WHITE + color.BOLD + 'Phone number: ' + color.END + Fore.YELLOW)
            phone_number = (phone_area + phone_num)
            url = ('https://api.ekata.com/3.1/phone?api_key=' + API_KEY_PHONE + '&phone=' + phone_number)
            response = requests.get(url)
            todos = json.loads(response.text)
            print ("")
            print (Fore.YELLOW + color.BOLD + "***************************************************************************")
            print (Fore.WHITE + color.BOLD + json.dumps(todos, indent=1))
            print (Fore.YELLOW + color.BOLD + "***************************************************************************" + color.END)
            print ("")
            print ("")
            print ("")
            back_close = input(Fore.WHITE + 'Type ' + Fore.YELLOW + color.BOLD + 'back ' + Fore.WHITE + color.END + 'to return to directory. Otherwise, hit any key to close the script: ' + Fore.YELLOW + color.BOLD)
            if back_close == ("back"):
                os.system("cls||clear")
                main ()
            else:
                os.system("cls||clear")
                print (color.END + Fore.YELLOW + "█████", end="")
                print ("██╗██████╗  ", end="")
                print ("  ██╗\n██╔════╝██╔", end="")
                print ("══██╗   ██║\n█████╗  ███", end="")
                print ("███╔╝   ██║\n██╔══╝  ██╔══██", end="")
                print ("╗   ██║\n██║", Fore.WHITE + "█", sep="", end="")
                print ("█╗" + Fore.YELLOW + "  ████", sep="", end="")
                print ("██╔╝" + Fore.WHITE + "█", sep="", end="")
                print ("█╗" + Fore.YELLOW + "█", sep="", end="")
                print ("█║", Fore.WHITE + "██╗", sep ="")
                print ("╚═╝" + Fore.WHITE + "╚═", end="")
                print ("╝" + Fore.YELLOW + "  ╚══", end="")
                print ("═══╝" + Fore.WHITE + " ", end="")
                print ("╚═╝" + Fore.YELLOW + "╚═╝", Fore.WHITE + "╚═╝", sep="", end=" ")
                print (Fore.WHITE + "by", Fore.YELLOW + color.BOLD + "Jack Carter", color.END)
                print (Fore.YELLOW + "Find", Fore.WHITE + ".", sep="", end="    ")
                print (Fore.YELLOW + "Big", Fore.WHITE + ".", sep="", end="     ")
                print (Fore.YELLOW + "Info", Fore.WHITE + ".", sep="", end="")
                print ("\n")
                break
            return
        elif direct_choice == ("exit"):
            os.system("cls||clear")
            print (color.END + Fore.YELLOW + "█████", end="")
            print ("██╗██████╗  ", end="")
            print ("  ██╗\n██╔════╝██╔", end="")
            print ("══██╗   ██║\n█████╗  ███", end="")
            print ("███╔╝   ██║\n██╔══╝  ██╔══██", end="")
            print ("╗   ██║\n██║", Fore.WHITE + "█", sep="", end="")
            print ("█╗" + Fore.YELLOW + "  ████", sep="", end="")
            print ("██╔╝" + Fore.WHITE + "█", sep="", end="")
            print ("█╗" + Fore.YELLOW + "█", sep="", end="")
            print ("█║", Fore.WHITE + "██╗", sep ="")
            print ("╚═╝" + Fore.WHITE + "╚═", end="")
            print ("╝" + Fore.YELLOW + "  ╚══", end="")
            print ("═══╝" + Fore.WHITE + " ", end="")
            print ("╚═╝" + Fore.YELLOW + "╚═╝", Fore.WHITE + "╚═╝", sep="", end=" ")
            print (Fore.WHITE + "by", Fore.YELLOW + color.BOLD + "Jack Carter", color.END)
            print (Fore.YELLOW + "Find", Fore.WHITE + ".", sep="", end="    ")
            print (Fore.YELLOW + "Big", Fore.WHITE + ".", sep="", end="     ")
            print (Fore.YELLOW + "Info", Fore.WHITE + ".", sep="", end="")
            print ("\n")
            break
        else:
            print (color.END)
            os.system("cls||clear")
if __name__ == "__main__":
    main ()
