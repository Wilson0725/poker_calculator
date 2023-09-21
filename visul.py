# %%
### import 
import matplotlib.pyplot as plt 
import pandas as pd
from ranking import ranking
from range_ import ranger
from range_ import hand_trans,trans
from cards import Deck
from itertools import combinations
import os
import range_
import cards
import math

# %%
### 
        
def create_cards(a_range, table):
    counter = 0 # counting the hands filted out
    combination = []

    for hand in a_range:

        # filt off cards including tables 
        if hand[0] in table:
            counter += 1
            continue 

        elif hand[1] in table:
            counter += 1
            continue

        else:
            cards = [x for x in hand] + table
        
        combination.append(cards)

    return combination

def plot(combos1,combos2=None,combos3=None,combos4=None,combos5=None,combos6=None):
    
    y1 = [math.log(ranking(combo),1e12) for combo in combos1]
    y1.sort()
    x1 = range(len(y1))

    y2 = [math.log(ranking(combo),1e12) for combo in combos2]
    y2.sort()
    x2 =range(len(y2))

    
    plt.plot([x/len(x1) for x in x1],y1,label='combos1')
    plt.plot([x/len(x2) for x in x2],y2,label='combos2')
    plt.legend()
    plt.show()

# %%
###

if __name__ == '__main__':

    deck = cards.Deck()
    card_dic, card_encode, card_value = deck.deck()
    all_the_hands = list(combinations(card_encode,2))

    table = deck.encode_shuffle()[0:3]
    print(trans(table))
    utg = range_.UTG_range()
    bb = range_.BB_range()

    combos1 = create_cards(utg.open,table)
    combos2 = create_cards(bb.call_utg,table)

    plot(combos1,combos2)
    

    
    