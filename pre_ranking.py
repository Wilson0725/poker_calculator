# %%  
### import 

# external 
import random

# internal 
from cards import Deck


# %% 
### def pairs, suity and odds

# pairs
def pre_ranking(hands:list):

    card1 = min(hands)
    card2 = max(hands)

    ### only vaule 
    values = [(a+1) % b for a, b in zip(hands, [13,13])] # value without suit
    values = [14 if a == 1 else a for a in values] # 1 =A =14
    values = [13 if a == 0 else a for a in values] # 0 =k =13
    values.sort()

    value1 = values[0]
    value2 = values[1]

#g3    
    if value1%13 == value2%13:
        assert ((card2-card1)%13 == 0),(card1, card2,'wrong pair-rules')

        return 3e4 + value2*(10**2)+ value1*(10**0)
#g2    
    elif (card1-1)//13 == (card2-1)//13:
        assert card2-card1 <= 12,('wrong suity-rules')
        
        return 2e4+ value2*(10**2)+ value1*(10**0)        
        
#g1    
    else:
        return 1e4+ value2*(10**2)+ value1*(10**0)        

# %% 
### test 

if __name__ =='__main__':
    deck = Deck()

    card_dic, card_encode, card_str = deck.deck()

    hands1 = random.sample(card_encode,2)
    
    print(f'{card_dic[hands1[0]],card_dic[hands1[1]]}={hands1}={pre_ranking(hands1)}')
    
    

