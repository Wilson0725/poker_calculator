# %% import

from itertools import combinations
from cards import Deck
from ranking import ranking
from pre_ranking import pre_ranking 
# %%
### def

deck = Deck()
card_dic, card_encode, card_value = deck.deck()
all_the_hands = list(combinations(card_encode,2))

def trans(cards:list):
    cards.sort()

    result = []
    for c in cards:
        result.append(card_dic[c])
    
    return result
        

def hand_trans(hands):
    card0 = card_dic[min(hands)]
    card1 = card_dic[max(hands)]
    
    return [card0, card1]

def ranger(lower_limit:int,uper_limit:int =40000): # 40000 = no upper limit
    return [x for x in all_the_hands if lower_limit <= pre_ranking(x) <= uper_limit]

# %% 

'common range setting' 
### Open

# UTG
class UTG_range():
    def __init__(self):
        
        # open
        self.pairs = ranger(30707) # 7+ pairs 
        self.Axs = ranger(21402,21413) # A2s - AKs
        self.Kxs = ranger(21305,21312) # K5s- KQs
        self.Qxs = ranger(21209,21211) # Q9s- QJs
        self.Jxs = ranger(21110,21110) # JTs
        self.Txs = ranger(21009,21009) # T9s
        self.Axo = ranger(11410,11413) 
        self.Kxo = ranger(11311,11312)
        self.Qxo = ranger(11211,11211)

        self.open = self.pairs+self.Axs+self.Kxs+self.Qxs+self.Jxs+self.Txs+self.Axo+self.Kxo+self.Qxo 
        self.open_counts = len(self.open)
        self.open_percent = 0.175 

# MP 
class MP_range():
    def __init__(self):

        # open
        self.pairs = ranger(30606) 
        self.Axs = ranger(21402,21413) 
        self.Kxs = ranger(21305,21312) 
        self.Qxs = ranger(21208,21211) 
        self.Jxs = ranger(21109,21110) 
        self.Txs = ranger(21009,21009) 
        self.Axo = ranger(11409,11413) 
        self.Kxo = ranger(11310,11312)
        self.Qxo = ranger(11210,11211)

        self.open = self.pairs+self.Axs+self.Kxs+self.Qxs+self.Jxs+self.Txs+self.Axo+self.Kxo+self.Qxo 
        self.open_counts = len(self.open)
        self.open_percent = 0.213

        # vs utg 
        self.bet3_utg_pairs = ranger(31111)
        self.bet3_utg_bluff = ranger(21404,21405)
        self.bet3_utg_Axs = ranger(21409,21413)
        self.bet3_utg_Kxs = ranger(21310,21312)
        self.bet3_utg_Qxs = ranger(21211,21211)
        self.bet3_utg_Axo = ranger(11412,11413)
        self.bet3_utg_Kxo = ranger(11312,11312)

        self.bet3_utg = self.bet3_utg_pairs+self.bet3_utg_bluff+self.bet3_utg_Axs+self.bet3_utg_Kxs+self.bet3_utg_Qxs+self.bet3_utg_Axo+self.bet3_utg_Kxo
        self.bet3_utg_counts = len(self.bet3_utg)
        self.bet3_utg_percent = 0.079

# CO
class CO_range():
    def __init__(self):

        # open
        self.pairs = ranger(30202) 
        self.Axs = ranger(21402,21413) 
        self.Kxs = ranger(21303,21312) 
        self.Qxs = ranger(21205,21211) 
        self.Jxs = ranger(21107,21110) 
        self.Txs = ranger(21008,21009)
        self.Nxs = ranger(20908,20908)
        self.Axo = ranger(11408,11413) 
        self.Kxo = ranger(11309,11312)
        self.Qxo = ranger(11210,11211)
        self.Jxo = ranger(11110,11110)

        self.open = self.pairs+self.Axs+self.Kxs+self.Qxs+self.Jxs+self.Txs+self.Nxs+self.Axo+self.Kxo+self.Qxo+self.Jxo
        self.open_counts = len(self.open)
        self.open_range = 0.285

        # vs utg 
        self.bet3_utg_pairs = ranger(31010)
        self.bet3_utg_bluff = ranger(21404,21405)
        self.bet3_utg_Axs = ranger(21409,21413)
        self.bet3_utg_Kxs = ranger(21310,21312)
        self.bet3_utg_Qxs = ranger(21211,21211)
        self.bet3_utg_Axo = ranger(11412,11413)
        self.bet3_utg_Kxo = ranger(11312,11312)

        self.bet3_utg = self.bet3_utg_pairs+self.bet3_utg_bluff+self.bet3_utg_Axs+self.bet3_utg_Kxs+self.bet3_utg_Qxs+self.bet3_utg_Axo+self.bet3_utg_Kxo
        self.bet3_utg_counts = len(self.bet3_utg)
        self.bet3_utg_percent = 0.083

        # vs mp
        self.bet3_mp_pairs = ranger(31010)
        self.bet3_mp_bluff = ranger(21404,21405)
        self.bet3_mp_Axs = ranger(21408,21413)
        self.bet3_mp_Kxs = ranger(21310,21312)
        self.bet3_mp_Qxs = ranger(21211,21211)
        self.bet3_mp_Axo = ranger(11411,11413)
        self.bet3_mp_Kxo = ranger(11312,11312)

        self.bet3_mp = self.bet3_mp_pairs+self.bet3_mp_bluff+self.bet3_mp_Axs+self.bet3_mp_Kxs+self.bet3_mp_Qxs+self.bet3_mp_Axo+self.bet3_mp_Kxo
        self.bet3_mp_counts = len(self.bet3_mp)
        self.bet3_mp_percent = 0.095

# BTN
class BTN_range():
    def __init__(self):

        # open
        self.pairs = ranger(30202) 
        self.Axs = ranger(21402,21413) 
        self.Kxs = ranger(21302,21312) 
        self.Qxs = ranger(21202,21211) 
        self.Jxs = ranger(21104,21110) 
        self.Txs = ranger(21006,21009)
        self.Nxs = ranger(20906,20908)
        self.Exs = ranger(20806,20808)
        self.Svxs = ranger(20705,20706)
        self.Sxs = ranger(20605,20605)
        self.Fxs = ranger(20504,20504)
        self.Axo = ranger(11403,11413) 
        self.Kxo = ranger(11308,11312)
        self.Qxo = ranger(11209,11211)
        self.Jxo = ranger(11109,11110)
        self.Txo = ranger(11009,11009)

        self.open = self.pairs+self.Axs+self.Kxs+self.Qxs+self.Jxs+self.Txs+self.Nxs+self.Exs+self.Svxs+self.Sxs+self.Fxs+self.Axo+self.Kxo+self.Qxo+self.Jxo+self.Txo
        self.open_counts = len(self.open)
        self.open_range = 0.418

        # vs utg 
        self.bet3_utg_pairs = ranger(31010)
        self.bet3_utg_bluff = ranger(21404,21405)
        self.bet3_utg_Axs = ranger(21409,21413)
        self.bet3_utg_Kxs = ranger(21310,21312)
        self.bet3_utg_Qxs = ranger(21211,21211)
        self.bet3_utg_Axo = ranger(11412,11413)
        self.bet3_utg_Kxo = ranger(11312,11312)

        self.bet3_utg = self.bet3_utg_pairs+self.bet3_utg_bluff+self.bet3_utg_Axs+self.bet3_utg_Kxs+self.bet3_utg_Qxs+self.bet3_utg_Axo+self.bet3_utg_Kxo
        self.bet3_utg_counts = len(self.bet3_utg)
        self.bet3_utg_percent = 0.056
        
        # vs mp
        self.bet3_mp_pairs = ranger(31010)
        self.bet3_mp_bluff = ranger(21404,21405)
        self.bet3_mp_Axs = ranger(21408,21413)
        self.bet3_mp_Kxs = ranger(21310,21312)
        self.bet3_mp_Qxs = ranger(21211,21211)
        self.bet3_mp_Axo = ranger(11411,11413)
        self.bet3_mp_Kxo = ranger(11312,11312)

        self.bet3_mp = self.bet3_mp_pairs+self.bet3_mp_bluff+self.bet3_mp_Axs+self.bet3_mp_Kxs+self.bet3_mp_Qxs+self.bet3_mp_Axo+self.bet3_mp_Kxo
        self.bet3_mp_counts = len(self.bet3_mp)
        self.bet3_mp_percent = 0.095

        # vs co
        self.bet3_co_pairs = ranger(31010)
        self.bet3_co_bluff = ranger(21404,21405)
        self.bet3_co_Axs = ranger(21409,21413)
        self.bet3_co_Kxs = ranger(21309,21312)
        self.bet3_co_Qxs = ranger(21210,21211)
        self.bet3_co_Jxs = ranger(21110,21110)
        self.bet3_co_Axo = ranger(11410,11413)
        self.bet3_co_Kxo = ranger(11311,11312)
        self.bet3_co_Qxo = ranger(11211,11211)

        self.bet3_co = self.bet3_co_pairs+self.bet3_co_bluff+self.bet3_co_Axs+self.bet3_co_Kxs+self.bet3_co_Qxs+self.bet3_co_Jxs+self.bet3_co_Axo+self.bet3_co_Kxo+self.bet3_co_Qxo
        self.bet3_co_counts = len(self.bet3_co)
        self.bet3_co_percent = 0.128

        # vs utg_call
        self.call_utg_pairs = ranger(30404,30909)
        
        self.call_utg = self.call_utg_pairs+ranger(20908,20908)+ranger(20807,20807)+ranger(20706,20706)+ranger(20605,20605)+ranger(20504,20504)
        self.call_utg_counts = len(self.call_utg)
        self.call_utg_percent = 0.042

        # vs mp_call
        self.call_mp_pairs = ranger(30505,30909)
        
        self.call_mp = self.call_mp_pairs+ranger(20908,20908)+ranger(20807,20807)+ranger(20706,20706)
        self.call_mp_counts = len(self.call_mp)
        self.call_mp_percent = 0.032

        # vs co_call
        self.call_co_pairs = ranger(30707,30909)
        
        self.call_co = self.call_co_pairs+ranger(20908,20908)+ranger(20807,20807)+ranger(20706,20706)
        self.call_co_counts = len(self.call_co)
        self.call_co_percent = 0.023        

# SB
class SB_range():
    def __init__(self):

        # open
        self.pairs = ranger(30202) 
        self.Axs = ranger(21402,21413) 
        self.Kxs = ranger(21302,21312) 
        self.Qxs = ranger(21202,21211) 
        self.Jxs = ranger(21104,21110) 
        self.Txs = ranger(21006,21009)
        self.Nxs = ranger(20906,20908)
        self.Exs = ranger(20806,20808)
        self.Svxs = ranger(20705,20706)
        self.Sxs = ranger(20605,20605)
        self.Fxs = ranger(20504,20504)
        self.Axo = ranger(11403,11413) 
        self.Kxo = ranger(11308,11312)
        self.Qxo = ranger(11209,11211)
        self.Jxo = ranger(11109,11110)
        self.Txo = ranger(11009,11009)

        self.open = self.pairs+self.Axs+self.Kxs+self.Qxs+self.Jxs+self.Txs+self.Nxs+self.Exs+self.Svxs+self.Sxs+self.Fxs+self.Axo+self.Kxo+self.Qxo+self.Jxo+self.Txo
        self.open_counts = len(self.open)
        self.open_range = 0.418

        # vs utg 
        self.bet3_utg_pairs = ranger(31010)
        self.bet3_utg_bluff = ranger(21404,21405)
        self.bet3_utg_Axs = ranger(21409,21413)
        self.bet3_utg_Kxs = ranger(21310,21312)
        self.bet3_utg_Qxs = ranger(21211,21211)
        self.bet3_utg_Axo = ranger(11412,11413)
        self.bet3_utg_Kxo = []

        self.bet3_utg = self.bet3_utg_pairs+self.bet3_utg_bluff+self.bet3_utg_Axs+self.bet3_utg_Kxs+self.bet3_utg_Qxs+self.bet3_utg_Axo+self.bet3_utg_Kxo
        self.bet3_utg_counts = len(self.bet3_mp)
        self.bet3_utg_percent = 0.074

        # vs mp
        self.bet3_mp_pairs = ranger(31010)
        self.bet3_mp_bluff = ranger(21404,21405)
        self.bet3_mp_Axs = ranger(21409,21413)
        self.bet3_mp_Kxs = ranger(21310,21312)
        self.bet3_mp_Qxs = ranger(21211,21211)
        self.bet3_mp_Axo = ranger(11411,11413)
        self.bet3_mp_Kxo = ranger(11312,11312)

        self.bet3_mp = self.bet3_mp_pairs+self.bet3_mp_bluff+self.bet3_mp_Axs+self.bet3_mp_Kxs+self.bet3_mp_Qxs+self.bet3_mp_Axo+self.bet3_mp_Kxo
        self.bet3_mp_counts = len(self.bet3_mp)
        self.bet3_mp_percent = 0.092

        # vs co
        self.bet3_co = []
        self.bet3_co_counts = 0
        self.bet3_co_percent = 0

        # vs btn
        self.bet3_btn_pairs = ranger(30707)
        self.bet3_btn_Axs = ranger(21403,21413)
        self.bet3_btn_Kxs = ranger(21309,21312)
        self.bet3_btn_Qxs = ranger(21209,21211)
        self.bet3_btn_Jxs = ranger(21110,21110)
        self.bet3_btn_Axo = ranger(11410,11413)
        self.bet3_btn_Kxo = ranger(11311,11312)

        self.bet3_btn = self.bet3_btn_pairs+self.bet3_btn_Axs+self.bet3_btn_Kxs+self.bet3_btn_Qxs+self.bet3_btn_Jxs+self.bet3_btn_Axo+self.bet3_btn_Kxo
        self.bet3_btn_counts = len(self.bet3_btn)
        self.bet3_btn_percent = 15.1


# BB
class BB_range():
    def __init__(self):

        # vs utg 
        self.bet3_utg_pairs = ranger(31212)
        self.bet3_utg_bluff = ranger(21404,21405)
        self.bet3_utg_Axs = ranger(21410,21413)
        self.bet3_utg_Kxs = ranger(2131111,21312)
        self.bet3_utg_Qxs = []
        self.bet3_utg_Axo = ranger(11413,11413)
        self.bet3_utg_Kxo = ranger(11312,11312)

        self.bet3_utg = self.bet3_utg_pairs+self.bet3_utg_bluff+self.bet3_utg_Axs+self.bet3_utg_Kxs+self.bet3_utg_Qxs+self.bet3_utg_Axo+self.bet3_utg_Kxo
        self.bet3_utg_counts = len(self.bet3_utg)
        self.bet3_utg_percent = 0.056

        # vs mp
        self.bet3_mp_pairs = ranger(31111)
        self.bet3_mp_bluff_1 = ranger(21402,21406)
        self.bet3_mp_bluff_2 = ranger(21302,21306)
        self.bet3_mp_Axs = ranger(21412,21413)
        self.bet3_mp_Axo = ranger(11413,11413)
        self.bet3_mp_Kxo = ranger(11312,11312)

        self.bet3_mp = self.bet3_mp_pairs+self.bet3_mp_Axs+self.bet3_mp_Axo+self.bet3_mp_Kxo+self.bet3_mp_bluff_1+self.bet3_mp_bluff_2
        self.bet3_mp_counts = len(self.bet3_mp)
        self.bet3_mp_percent = 0.072        

        # vs co
        self.bet3_co_pairs = ranger(31111)
        self.bet3_co_bluff_1 = ranger(21402,21406)
        self.bet3_co_bluff_2 = ranger(21302,21306)
        self.bet3_co_Axs = ranger(21412,21413)
        self.bet3_co_Axo = ranger(11411,11413)
        self.bet3_co_Kxo = ranger(11312,11312)

        self.bet3_co = self.bet3_co_pairs+self.bet3_co_bluff_1+self.bet3_co_bluff_2+self.bet3_co_Axs+self.bet3_co_Axo+self.bet3_co_Kxo
        self.bet3_co_counts = len(self.bet3_co)
        self.bet3_co_percent = 0.091

        # vs btn
        self.bet3_btn_pairs = ranger(30909)
        self.bet3_btn_bluff = ranger(21404,21405)
        self.bet3_btn_Axs = ranger(21410,21413)
        self.bet3_btn_Kxs = ranger(21309,21313)
        self.bet3_btn_Qxs = ranger(21209,21211)
        self.bet3_btn_Jxs = ranger(21108,21110)
        self.bet3_btn_Txs = ranger(21008,21009)
        self.bet3_btn_Nxs = ranger(20908,20908)
        self.bet3_btn_Axo = ranger(11410,11413)
        self.bet3_btn_Kxo = ranger(11311,11312)     

        self.bet3_btn = self.bet3_btn_pairs+self.bet3_btn_bluff+self.bet3_btn_Axs+self.bet3_btn_Kxs+self.bet3_btn_Qxs+self.bet3_btn_Jxs+self.bet3_btn_Txs+self.bet3_btn_Nxs+self.bet3_btn_Axo+self.bet3_btn_Kxo
        self.bet3_btn_counts = len(self.bet3_btn)
        self.bet3_btn_percent = 0.139

        # vs sb
        self.bet3_sb = ranger(31010)+ranger(21404,21405)+ranger(21410,21413)+ranger(21310,21312)+ranger(21211,21211)+ranger(21002,21005)+ranger(11402,11407)+ranger(11412,11413)+ranger(11305,11307)+ranger(11208,11208)
        self.bet3_sb_counts = len(self.bet3_sb)
        self.bet3_sb_percent = 0.174

        # vs utg_call
        self.call_utg = ranger(30202,31111)+ranger(21402,21403)+ranger(21406,21409)+ranger(21303,21310)+ranger(21207,21211)+ranger(21108,21110)+ranger(21007,21009)+ranger(20906,20908)+ranger(20806,20807)+ranger(20705,20706)+ranger(20604,20605)+ranger(20503,20504)+ranger(20403,20403)+ranger(11410,11412)
        self.call_utg_counts = len(self.call_utg)
        self.call_utg_percent = 0.184

        # vs mp_call
        self.call_mp = ranger(30202,31010)+ranger(21407,21411)+ranger(21307,21312)+ranger(21206,21211)+ranger(21108,21110)+ranger(21007,21009)+ranger(20906,20908)+ranger(20805,20807)+ranger(20705,20706)+ranger(20604,20605)+ranger(20503,20504)+ranger(20403,20403)+ranger(11410,11412)+ranger(11311,11311)+ranger(11211,11211)
        self.call_mp_counts = len(self.call_mp)
        self.call_mp_percent = 0.195 

        # vs co_call
        self.call_co = ranger(30202,31010)+ranger(21407,21411)+ranger(21307,21312)+ranger(21205,21211)+ranger(21106,21110)+ranger(21007,21009)+ranger(20906,20908)+ranger(20806,20807)+ranger(20705,20706)+ranger(20604,20605)+ranger(20503,20504)+ranger(20403,20403)+ranger(11409,11410)+ranger(11310,11311)+ranger(11210,11211)+ranger(11110,11110)
        self.call_co_counts = len(self.call_co)
        self.call_co_percent = 0.219     

        # vs btn_call
        self.call_btn = ranger(30202,30808)+ranger(21402,21403)+ranger(21406,21409)+ranger(21302,21308)+ranger(21202,21208)+ranger(21104,21107)+ranger(21006,21007)+ranger(20906,20907)+ranger(20805,20807)+ranger(20704,20706)+ranger(20604,20605)+ranger(20503,20504)+ranger(20403,20403)+ranger(11405,11409)+ranger(11309,11310)+ranger(11210,11211)+ranger(11109,11110)+ranger(11009,11009)
        self.call_btn_counts = len(self.call_btn)
        self.call_btn_percent = 0.258

        # vs bb_call
        self.call_bb = ranger(30202,30909)+ranger(21402,21403)+ranger(21406,21409)+ranger(21302,21309)+ranger(21202,21210)+ranger(21102,21110)+ranger(21006,21009)+ranger(20905,20908)+ranger(20804,20807)+ranger(20704,20706)+ranger(20603,20605)+ranger(20502,20504)+ranger(20402,20403)+ranger(20302,20302)+ranger(11408,11411)+ranger(11308,11312)+ranger(11209,11211)+ranger(11109,11110)+ranger(11008,11009)
        self.call_bb_counts = len(self.call_bb)
        self.call_bb_percent = 0.350

#%% 
### test

if __name__ =='__main__':
    
    ### deck
    deck = Deck()
    card_dic, card_encode, card_str = deck.deck()
    all_the_hands = list(combinations(card_encode,2))
    
    utg = UTG_range()
    mp = MP_range()
    bb =BB_range()
    print(len(utg.open)/len(all_the_hands))
    print(bb.call_bb_counts/len(all_the_hands))
    print(bb.bet3_btn)
