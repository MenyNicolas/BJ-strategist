import numpy as np
import pandas as pd

def is_soft(main):
    total = sum(main)
    ace_count = main.count(11)

    adjusted_aces = ace_count
    while total > 21 and adjusted_aces > 0:
        total -= 10
        adjusted_aces -= 1

    return adjusted_aces > 0

def surrender(main_joueur, main_dealer, true_count):
    carte_dealer = main_joueur[0]
    is_hard = not is_soft(main_joueur)
    if carte_dealer in [9, 10, 11]:
        if is_hard and (np.sum(main_joueur) == 16):
            return 1
        elif is_hard and ((np.sum(main_joueur) == 15) and (carte_dealer == 10)):
            return 1
        else:
            return 0
    else:
        return 0
    
def model_split(main_joueur, main_dealer, true_count):
    return 1
