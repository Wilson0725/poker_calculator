#%% 
### import 

# external 
import pandas as pd 
import numpy as np
from itertools import combinations

# internal 
import range_
import cards
import ranking
import billboard as bbd
from pre_ranking import pre_ranking 

# %% 
### __init__

if __name__ == "__main__":

    deck = cards.Deck()
    card_dic, card_encode, card_value = deck.deck()
    all_the_hands = list(combinations(card_encode,2))

    table = [22,12,10]

    utg = range_.UTG_range()
    bb = range_.BB_range()

    player1 = bbd.PlayerBill('John')
    player2 = bbd.PlayerBill('Ken')

    player1.updates(utg.open,table)
    player2.updates(bb.call_utg,table)

    player1.show()
    player2.show()

    table = [22,12,10,15]

    player1.updates(utg.open,table)
    player2.updates(bb.call_utg,table)

    player1.show()
    player2.show()
