"""for release candidate two of CODEBREAKER"""

def best_guess(**kwargs):
    """generate and return the AI best guess"""
    if kwargs["first_guess"]:
        return first_guess(kwargs["search_space"])
    ap_codes = []
    search_space = kwargs["search_space"]
    rejected = kwargs["rejected"]
    positions = kwargs["positions"]
    ss = len(search_space)

    for n4 in range(ss):
        L4 = search_space[n4]
        for n3 in range(ss):
            L3 = search_space[n3]
            for n2 in range(ss):
                L2 = search_space[n2]
                for n1 in range(ss):
                    L1 = search_space[n1]
                    code_seq = L4 + L3 + L2 + L1
                    ap_codes.append(code_seq)
    # END OF BUILD #

    accepted = False
    while not accepted:
        # first check that any code_seq conforms to the positions
        for code_seq in ap_codes:
            for index, ltr in enumerate(code_seq):
                if ltr in positions[index]:
                    accepted = True
                else:
                    accepted = False
                    break
            # then check that any given code_seq has not already been tried
            if accepted and code_seq not in rejected:
                for code in rejected:
                    # generate a response for the code_seq, when tested against a rejected code
                    resp = response(code_seq, code)
                    if resp == rejected[code]:
                        pass
                    else:
                        accepted = False
                if accepted:
                    return code_seq
                elif code_seq == ap_codes[-1]:
                    return "CHEAT"


def response(guess, code=""):
    """response feedback v2.0
    returns a response to any given (guess, code)
    if a code is not provided, "----" will be
    returned for any given guess
    """
    guess_lst = list(guess)
    cor_pos = [0, 0, 0, 0]
    correct_ltr = 0
    for index, ltr in enumerate(code):
        if ltr in guess:
            if ltr in guess_lst:
                guess_lst.pop(guess_lst.index(ltr))
            if code[index] == guess[index]:
                cor_pos[index] = 1
    correct_pos = sum(cor_pos)
    wrong_ltr = len(guess_lst)
    correct_ltr = len(code) - correct_pos - wrong_ltr
    output = "*" * correct_pos + "+" * correct_ltr + "-" * wrong_ltr
    return output


def first_guess(ltrs):
    """
    returns a randomly generated first guess in the form of
        AABB
        ABAB
        ABBA
    where A and B are random letters between A and F
    """
    from random import randint

    # ltrs = ["A", "B", "C", "D", "E", "F"]

    # get two, none repeating, integer values between 0 and 5
    # used to index into the ltrs list
    L1 = randint(0, len(ltrs)-1)
    L2 = L1
    while L2 == L1:
        L2 = randint(0, len(ltrs)-1)

    # assign a letter to its placeholder
    x = ltrs[L1]
    y = ltrs[L2]

    # use the placeholders to generate the three preferred patterns,
    # choose one at random and return it
    patterns = {0: [x, x, y, y], 1: [x, y, x, y], 2: [x, y, y, x]}
    pattern = randint(0, 2)
    fg = "".join(patterns[pattern])
    return fg
