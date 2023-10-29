#!/usr/bin/python3

"""A helper utility for the Codebraker game"""

import sys
from time import sleep
from random import shuffle
from ai_rc2 import response


# Third party imports
try:
    from blessed import Terminal
except ImportError as error:
    MSG = """
    This application uses Terminal from the blessed library,
    which could not be found on your system.
    Please see https://pypi.org/project/blessed/ for details.
    sys.exit will now be called, which will display the ImportError message.
    """
    print(MSG)
    sys.exit(f"{error}: ")


def cls():
    """clears the screen and places the cursor at position 0,0"""
    print(TERM.home + TERM.clear, end="")


def inst():
    """the help section"""
    message = """
    Instructions:

    1. Select the game level
    
    2. Either enter your own secret code or press
       R to generate a random four letter code.
    
    3. At the Guess: prompt, enter the four letter
       AI guess.
    
    4. You will then be shown the correct response
       symbols, in the correct order.

    Use those four response symbols, in the game.
    
    Other Guess: prompt options...
        Esc: Clears the input.
         ? : Displays your secret code.
         M : Displays the app menu.
    """
    print(f"    {message}")
    print("    Press any key to continue. ", end="")
    # set the cursor insertion point and display the above print() call
    TERM.get_location()
    #  wait for any key press and don't display it
    with TERM.cbreak():
        TERM.inkey().upper()
        print(" ", end="")
    # =======<END>======= #


def menu():
    """display the menu and return the chosen option"""
    menu_text = """
    Codebreaker Feedback Helper

     0 Rookie
     1 Master
     2 Genius
     H Help
     Esc to Exit
        : """
    options = ("0", "1", "2", "H")  # ESCAPE_KEY to exit
    print(menu_text, end="")
    with TERM.cbreak():  # so that we don't need to hit enter to terminate input
        get = ""
        while not get:
            get = TERM.inkey().upper()
            if get == ESCAPE_KEY:
                sys.exit("Exit")
            if get in options:
                break
            else:
                get = ""
                print(TERM.move_left(), end="")
                print(" ", end="")

    if get == "0":
        print("Rookie")
    elif get == "1":
        print("Master")
    elif get == "2":
        print("Genius")
    elif get == "H":
        print("Help")
    sleep(0.25)
    return get


def read_keys(ary, get_code=""):
    """read and key presses and return any valid string value"""
    with TERM.cbreak():  # so that we don't need to hit enter to terminate input
        char_list = []
        code = ""
        while len(char_list) != 4:
            y, x = TERM.get_location()
            ltr = TERM.inkey().upper()
            if ltr in ary:
                print(TERM.move(y, x), end="")
                char_list.append(ltr)
                print(char_list[-1], end="")
            elif ltr == ESCAPE_KEY and char_list:
                for deleate in range(len(char_list)):
                    print(TERM.move_left(), end="")
                    print(" ", end="")
                    print(TERM.move_left(), end="")
                char_list.clear()
            elif ltr in ("M", "?"):
                char_list.append(ltr)
                break
            elif not char_list and ltr == "R" and get_code:
                print("Generating a four letter secret code...")
                shuffle(ary)
                code = "".join([L for L in ary[0:4]])
                char_list = list(code)
    if code:
        print(f"    {code}")
    else:
        print()
    return "".join(char_list)


def feedback(lvl, ary):
    """generate and display the feedback help"""
    print()
    print(f"    {lvl} level feedback.")
    print("    Using these letters:")
    ltrs = " ".join(ary)
    print(f"    {ltrs}")
    print()
    print("    Enter your four letter secret code")
    print("    or press R to generate a random code")
    print("    ", end="")
    code = read_keys(ary, get_code=True)
    while True:
        ai_guess = ""
        print()
        while not ai_guess:
            print("    Guess:", end=" ")
            ai_guess = read_keys(ary)
        if ai_guess == "M":
            break
        elif ai_guess == "?":
            print(f"    {code}")
        else:
            print(f"    Resp : {response(ai_guess,code)}")
    # END #


# ROOT #
TERM = Terminal()
ESCAPE_KEY = "\x1b"
INP = ""
cls()
while not INP:
    ARRAY = ["A", "B", "C", "D", "E", "F"]
    INP = menu()
    if INP == "H":
        inst()
        INP = ""
    elif INP == "0":
        feedback("Rookie", ARRAY)
    elif INP == "1":
        ARRAY.append("G")
        feedback("Master", ARRAY)
    elif INP == "2":
        ARRAY.append("G")
        ARRAY.append("H")
        feedback("Genius", ARRAY)
    INP = ""
# ROOT END #
