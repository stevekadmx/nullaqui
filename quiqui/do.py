from colorama import Fore, Back, Style

def cprint(text, color):
    """
    Prints text in a specified color.

    Args:
        text (str): The text to print.
        color (str): The color to print the text in.
    """
    if color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    elif color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'yellow':
        print(Fore.YELLOW + text + Style.RESET_ALL)
    elif color == 'blue':
        print(Fore.BLUE + text + Style.RESET_ALL)
    elif color == 'magenta':
        print(Fore.MAGENTA + text + Style.RESET_ALL)
    elif color == 'cyan':
        print(Fore.CYAN + text + Style.RESET_ALL)
    elif color == 'white':
        print(Fore.WHITE + text + Style.RESET_ALL)
    elif color == 'black':
        print(Fore.BLACK + text + Style.RESET_ALL)


cprint(f"not found (By.CLASS_NAME): '{name}'", 'yellow')
