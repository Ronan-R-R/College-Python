from colorama import Fore, Back, Style, init

init()

print(Style.BRIGHT + Fore.CYAN + "Cyan" + Style.RESET_ALL)
print(Style.DIM + Back.BLUE + "Blue" + Style.RESET_ALL)
print(Fore.RED + "Red" + Fore.RESET)
print(Back.GREEN + "Green" + Back.RESET)