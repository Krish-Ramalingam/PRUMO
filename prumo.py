cards = [2]*6 + [3]*6 + [4]*6 + [5]*6 + [6]*6 + [7]*6 + [8]*6 + [9]*6 + [10]*6 + [12]*6 + [14]*6 + [15]*6 + [16]*6 + [18]*6 + [21]*6 + [25]*6 + ['Swap']* 3 + ['Rotate']* 3 + ['Reverse']* 3 + ['Block']* 3 + ['Prime']* 3 + ['Square']* 3 + ['Mod 2']* 3 + ['Mod 3']* 3 + ['Mod 4']* 3 + ['Infinite Descent']* 3 + ['Sieve of Erathosthenes']* 3 + ['Collatz']* 3 + [+2]*3 + [+3]*3 + [+4]*3 + [+5]*3 + [+6]*3 + [+7]*3 + [+8]*3 + [+9]*3

import random
random.shuffle(cards)
cards_i = iter(cards)

def draw(p, n=1):
    with open(f"player_{p}.txt", "a") as file:
        for _ in range(n):
            file.write(str(next(cards_i)) + "\n")
