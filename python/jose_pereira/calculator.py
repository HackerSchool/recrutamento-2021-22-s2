import main as c
import os
import time


class Calculator():
    """
    Calculator Class: Represents a calculator.
    """

    def __init__(self):
        self.mainmenu()

    def clearscreen(self):
        """
        Clear the terminal's screen, using the cls command on Windows, or
        the clear command on UNIX systems.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def displaylogo(self):
        """
        Displays the calculator logo.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        logo = \
            f"""{c.Color.BOLD}{c.Color.GREEN}
 _____   ___   _     _____ _   _ _       ___ _____ ___________ 
/  __ \ / _ \ | |   /  __ \ | | | |     / _ \_   _|  _  | ___ \\
| /  \// /_\ \| |   | /  \/ | | | |    / /_\ \| | | | | | |_/ /
| |    |  _  || |   | |   | | | | |    |  _  || | | | | |    / 
| \__/\| | | || |___| \__/\ |_| | |____| | | || | \ \_/ / |\ \ 
 \____/\_| |_/\_____/\____/\___/\_____/\_| |_/\_/  \___/\_| \_|
        {c.Color.END}"""
        print(logo)

    def mainmenu(self):
        """
        Displays the main menu
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.displaylogo()
        print("\n\t\t  1) Solve basic calculations.")
        print("\t\t  2) Multiple args calculation. ")
        print("\t\t  3) Solve one variable equation. ")
        print("\t\t  4) Exit Calculator.")
        self.getoption()

    def getoption(self):
        """
        Gets the user option.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        option = input("\n\t\t  Option: ")
        self.handleoption(option)

    def handleoption(self, option):
        """
        Handles the user option. If it's an invalid option,
        ask user again for a valid option.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # Basic calculation option
        if option == '1':
            self.clearscreen()
            self.docalculation()
        # Multiple args calculation option
        elif option == '2':
            self.clearscreen()
            self.dosupercalculation()
        # One variable equation option
        elif option == '3':
            self.clearscreen()
            self.onevariablesolver()
        elif option == '4':
            # Return to user menu.
            return
        else:
            print("Please type a valid option! ")
            self.getoption()

    def displaycalculationoptions(self):
        """
        Displays the calculator operators.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print(f"\t{c.Color.BOLD}                   Please use:{c.Color.END}")
        print(f"\t  ({c.Color.BOLD}{c.Color.GREEN}+{c.Color.END})"
              f"for adition              ({c.Color.BOLD}{c.Color.GREEN}-"
              f"{c.Color.END}) for subtraction:")
        print(f"\t  ({c.Color.BOLD}{c.Color.GREEN}*{c.Color.END})"
              f"for multiplication       ({c.Color.BOLD}{c.Color.GREEN}/"
              f"{c.Color.END}) for division")
        print(f"\t  ({c.Color.BOLD}{c.Color.GREEN}**{c.Color.END})"
              f"for exponent            ({c.Color.BOLD}{c.Color.GREEN}%"
              f"{c.Color.END}) for rest of")

    def docalculation(self):
        """
        Gets the result of ta basic calculation.
        Parameters
        ----------
        None

        Results
        -------
        None
        """
        self.displaylogo()
        self.displaycalculationoptions()

        # Get expression.
        first_number = int(input("\n\n\t  Enter your first number here -> "))
        operator = input("\n\n\t  Enter your operator here -> ")
        second_number = int(
            input("\n\n\t  Enter your seconhd number here -> "))
        # Eval expression.
        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        elif operator == '/':
            result = first_number / second_number
        elif operator == '**':
            result = first_number ** second_number
        elif operator == '%':
            result = first_number % second_number
        else:
            print(f"\n\t {c.Color.BOLD}{c.Color.RED}"
                  f"Please enter valid operator .{c.Color.END}")

        print(f"\n\t                   {c.Color.GREEN}result: {c.Color.END}"
              f"{result}")
        time.sleep(2.5)
        self.clearscreen()
        self.mainmenu()

    def dosupercalculation(self):
        """
        Resolves a complex expression.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.clearscreen()
        self.displaylogo()
        self.displaycalculationoptions()
        print("\tNOTE: Use one space between numbers and operators.")
        expression = input("\tEnter your expression -> ").split()

        # First do all **
        while '**' in expression:
            i = 0
            for item in expression:
                if item == '**':
                    res = int(expression[i - 1]) ** int(expression[i + 1])
                    del expression[i - 1]
                    del expression[i - 1]
                    expression[i - 1] = res
                    break
                i += 1

        # Then do all * or / or %
        while '*' in expression or '/' in expression or '%' in expression:
            i = 0
            for item in expression:
                if item == '*':
                    res = int(expression[i - 1]) * int(expression[i + 1])
                    del expression[i - 1]
                    del expression[i - 1]
                    expression[i - 1] = res
                    break
                elif item == '/':
                    res = int(expression[i - 1]) / int(expression[i + 1])
                    del expression[i - 1]
                    del expression[i - 1]
                    expression[i - 1] = res
                    break
                elif item == '%':
                    res = int(expression[i - 1]) % int(expression[i + 1])
                    del expression[i - 1]
                    del expression[i - 1]
                    expression[i - 1] = res
                    break
                i += 1

        # At the end do + or -
        while '+' in expression or '-' in expression:
            i = 0
            for item in expression:
                if item == '+':
                    res = int(expression[i - 1]) + int(expression[i + 1])
                    del expression[i - 1]
                    del expression[i - 1]
                    expression[i - 1] = res
                    break
                elif item == '-':
                    res = int(expression[i - 1]) - int(expression[i + 1])
                    del expression[i - 1]
                    del expression[i - 1]
                    expression[i - 1] = res
                    break
                i += 1
        
        # The result will be the first index of the list
        result = expression[0]
        print(f"\n\t                   {c.Color.GREEN}result: {c.Color.END}"
              f"{result}")
        time.sleep(2.5)
        self.clearscreen()
        self.mainmenu()

    def onevariablesolver(self):
        """
        Resolves a one variable (x) equation.
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.displaylogo()
        print(f"\t{c.Color.BOLD}              Please use: ax + b{c.Color.END}")

        try:
            # Get 'a' and 'b' values
            a = input("\n\n\t  Enter value of 'a' -> ")
            b = input("\n\n\t  Enter value of 'b' -> ")
            # Find x
            x = -int(b) / int(a)
            print(f"\n\t                   {c.Color.GREEN}x = {c.Color.END}"
                  f"{x}")
            time.sleep(2)
            self.clearscreen()
            # Go back to calculator main menu
            self.mainmenu()
        except:
            print(f"\n\t {c.Color.BOLD}{c.Color.RED}Please enter valid 'a' and"
                  f"'b' values.{c.Color.END}")
            time.sleep(1.5)
            self.clearscreen()
            self.onevariablesolver()
