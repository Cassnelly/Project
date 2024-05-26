#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def printMenu(menu):
    """
    Function to print the options with prefixed numbers.

    Parameters:
        menu (list): List of menu options.

    Returns:
        None
    """
    for i, option in enumerate(menu):
        print(f"{i + 1} {option}")

def acceptCommand(menu_length):
    """
    Function to accept a valid command input from the user.

    Parameters:
        menu_length (int): Length of the menu list.

    Returns:
        int: Valid command input from the user.
    """
    while True:
        try:
            choice = int(input("Enter a number: "))
            if 1 <= choice <= menu_length:
                return choice
            else:
                print("Invalid input. Please enter a number within the range of options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def performCommand(command, menu):
    """
    Function to perform the selected command from the menu.

    Parameters:
        command (int): Selected command number.
        menu (list): List of menu options.

    Returns:
        None
    """
    print(f"Command = {menu[command - 1]}")

def main():
    """
    Main function to orchestrate the command interpreter program.

    Parameters:
        None

    Returns:
        None
    """
    menu = ["Open", "Save", "Compile", "Run", "Quit"]

    while True:
        printMenu(menu)
        choice = acceptCommand(len(menu))
        if choice == len(menu):
            print("Command = Quit")
            print("Have a nice day!")
            break
        else:
            performCommand(choice, menu)

if __name__ == "__main__":
    main()


# In[ ]:




