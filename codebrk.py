#!/usr/bin/python3

"""
Codebreaker RC2
Inspired by and based upon the game known as UNCLE BERNIE'S CODEBREAKER GAME
"""

# Standard library imports
import sys
from random import choices
from time import sleep

# The AI side of this software
from ai_rc2 import best_guess, response

# Third party imports
# This is a requirement so that we get an emulation of original game
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


def output(prnt):
    """simulate the text display speed of vintage computers"""
    for char in prnt:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.035)


def cls():
    """clears the screen and places the cursor at position 0,0"""
    print(TERM.home + TERM.clear, end="")


def menu():
    """display the menu and return the chosen option"""
    menu_text = """
    *** UNCLE BERNIE'S CODEBREAKER GAME ***

     0 ROOKIE
     1 MASTER
     2 GENIUS
     H HELP

    ENTER YOUR CHOICE: """
    options = ("0", "1", "2", "H", ESCAPE_KEY)  # ESCAPE_KEY to exit
    output(menu_text)
    inp = ""
    with TERM.cbreak():  # so that we don't need to hit enter to terminate input
        while inp not in options:
            inp = TERM.inkey().upper()
            if inp == ESCAPE_KEY:
                output("\n\tEsc key detected.\n\tGame exit.\n")
                sys.exit()
        print(inp)
    return inp


def inst():
    """the help section"""
    message = """
    INSTRUCTIONS:

    BREAK THE FOUR LETTER SECRET CODE BEFORE
    THE COMPUTER FINDS YOUR OWN SECRET CODE!
    EACH GUESS FOR THE SECRET CODE ANSWERS:
    '*' FOR EACH LETTER IN THE CORRECT POSITION
    '+' FOR EACH LETTER IN THE WRONG POSITION
    '-' FOR EACH LETTER NOT HAVING ANY MATCH
    ESC KEY VOIDS/RESTARTS USER INPUT GROUPS
    """
    output(message)
    # =======<END>======= #


def display_scores():
    """display the score records"""
    scrs = []
    display = """
    SCORE (YOU:ME) IS """
    for key in SCORES:
        scrs.append(f"{SCORES[key]:02d}")
    display += ":".join(scrs)
    output(f"{display}\n")
    # =======<END>======= #


def get_hguess(level):
    """
    get human code guess and return a string object
    takes one augment: level
    level must contain 0 1 or 2 as a string object
    """

    # y is the column and x is the row
    # format the term.move() as y, x
    # don't forget the end='' option, as in: print(term.move(x, y), end='')
    if level not in ("0", "1", "2"):
        print(get_hguess.__doc__)
        return False
    ltrs = ["A", "B", "C", "D", "E", "F"]
    if level == "1":
        ltrs.append("G")
    elif level == "2":
        ltrs.append("G")
        ltrs.append("H")
    with TERM.cbreak():  # so that we don't need to hit enter to terminate input
        char_list = []
        while len(char_list) != 4:
            y, x = TERM.get_location()
            ltr = TERM.inkey().upper()
            if ltr in ltrs:
                print(TERM.move(y, x), end="")
                char_list.append(ltr)
                print(char_list[-1], end="")
            elif ltr == ESCAPE_KEY and char_list:
                for deleate in range(len(char_list)):
                    print(TERM.move_left(), end="")
                    output(" ")
                    print(TERM.move_left(), end="")
                char_list.clear()
    return "".join(char_list)


def ai_analyse(ltrs, resp, s_sp, p_mx):
    """analyse the human player feedback
    return a new search_space and positions matrix
    usage:
        ltrs = the AI best guess
        resp = the human feedback
        s_sp = the search space
        p_mx = the positions matrix
    """

    def remove(array):
        """
        maintain the positions matrix
        takes one arguments (array)
        array: any letters to be removed
        uses the array index as the positional argument
        """
        for index, ltr in enumerate(array):
            if ltr in p_mx[index]:
                p_mx[index].remove(ltr)
        # END #

    wro_ltr = resp.count("-")
    if wro_ltr == 4:
        rem_set = set(ltrs)
        for ltr in rem_set:
            remove(4 * ltr)
            s_sp.remove(ltr)
    elif "*" not in resp:
        remove(ltrs)
    return s_sp, p_mx


def get_hresp():
    """
    get the human response and return it as a string object
    """
    accept = ("*", "+", "-")
    with TERM.cbreak():  # so that we don't need to hit enter to terminate input
        resp_list = []
        while len(resp_list) != 4:
            y, x = TERM.get_location()
            symb = TERM.inkey().upper()
            if symb in accept:
                print(TERM.move(y, x), end="")
                resp_list.append(symb)
                print(resp_list[-1], end="")
            elif symb == ESCAPE_KEY and resp_list:
                for deleate in range(len(resp_list)):
                    print(TERM.move_left(), end="")
                    output(" ")
                    print(TERM.move_left(), end="")
                resp_list.clear()
    return "".join(sorted(resp_list))


def i_win(code):
    """display the I WIN message. update and display scores"""
    output("    I WIN!\n")
    output(f"    YOU WERE LOOKING FOR {code}\n")
    SCORES["ME"] += 1
    display_scores()
    print()


def u_win():
    """display the YOU WIN message. update and display scores"""
    output("    YOU WIN!\n")
    SCORES["YOU"] += 1
    display_scores()
    print()


def play(lvl, rnds, search_space):
    """main game play"""
    rounds = 0
    ai_guess_log = {}
    # build the positions matrix
    positions = {  # holds all letters at all 4 positions: the starting condition
        0: "",
        1: "",
        2: "",
        3: "",
    }
    for pos in positions:
        positions[pos] = [L for L in search_space]

    display = f"""    LEVEL: 0, ROUNDS: {rnds}, LETTERS: {search_space[0]}...{search_space[-1]}
    """
    output(display)
    display_scores()
    print()
    ai_code = "".join(choices(search_space, k=4))
    first_guess = True
    ai_bg = best_guess(
        first_guess=first_guess,
        search_space=search_space,
        rejected=ai_guess_log,
        positions=positions,
    )
    while True:
        rounds += 1
        first_guess = False
        output(f"    #{rounds:02d} ")
        h_guess = get_hguess(lvl)
        print(TERM.move_right(), end="")
        ai_response = response(h_guess, ai_code)
        output(f"{ai_response}")
        print(TERM.move_right(2), end="")
        if ai_response == "****":
            print()
            u_win()
            break
        output(f"{ai_bg}")
        print(TERM.move_right(), end="")
        h_response = get_hresp()
        if h_response == "****":
            print()
            i_win(ai_code)
            break
        ai_guess_log[ai_bg] = h_response
        search_space, positions = ai_analyse(ai_bg, h_response, search_space, positions)
        if not first_guess:
            ai_bg = best_guess(
                first_guess=first_guess,
                search_space=search_space,
                rejected=ai_guess_log,
                positions=positions,
            )
        if ai_bg == "CHEAT":
            print()
            output("    YOU CHEATED!")
            print()
            i_win(ai_code)
            break

        print()
        if rounds == rnds:
            output("    IT'S A DRAW!\n")
            output(f"    YOU WERE LOOKING FOR {ai_code}\n")
            break
    # =======<END>======= #


# =======<ROOT>======= #
SCORES = {"YOU": 0, "ME": 0}

ESCAPE_KEY = "\x1b"
TERM = Terminal()
cls()
while True:
    OPT = menu()
    if OPT == "H":
        inst()  # it's bad practice to redefine a built-in, such as help()
    elif OPT == "0":
        SEARCH_SPACE = ["A", "B", "C", "D", "E", "F"]
        RNDS = 6
    elif OPT == "1":
        SEARCH_SPACE = ["A", "B", "C", "D", "E", "F", "G"]
        RNDS = 7
    elif OPT == "2":
        SEARCH_SPACE = ["A", "B", "C", "D", "E", "F", "G", "H"]
        RNDS = 8
    if OPT != "H":
        play(OPT, RNDS, SEARCH_SPACE)
