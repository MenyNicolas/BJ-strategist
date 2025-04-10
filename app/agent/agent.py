import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
import random

import agent.utils_agent as utils_agent

########################################################
# Fonctions utiles pour l'IA
########################################################

def valeur_carte(carte):
    if carte in ['J', 'Q', 'K']:
        return 10
    else:
        return carte
    
def valeur_main(main):
    return sum(valeur_carte(carte) for carte in main)

########################################################


def agent_BJ(id_action, action_stack, main_joueur, main_dealer, running_count, sabot):

    true_count = int(running_count / (len(sabot) / 52))

    # gestion de la mise initiale
    if(id_action == 0):
        return 10

    # gestion de l'assurance
    if(id_action == 1):
        if true_count > 2:
            return 'A'
        else:
            return 'N'
        
    # gestion du surrender
    if(id_action == 2):
        return utils_agent.surrender(main_joueur, main_dealer, true_count)
    
    # gestion des splits
    if(id_action == 3):
        return utils_agent.model_split(main_joueur, main_dealer, true_count)
    
    # gestion stand hit double
    if(id_action == 4):
        double_possible = len(main_joueur) == 2
        if(valeur_main(main_joueur) == 21):
            return 'S'  
        return random.choice(['H', 'S', 'D'])
    
    return 0