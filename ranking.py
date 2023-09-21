import cards
from itertools import combinations

# ranking, output = grade, of_what, with what, return max(C75)
def ranking(cards:list):
    
    # cards >= 5, for pre-ranking
    if len(cards) >= 5:
        combos = list(combinations(cards,5)) # all combos of C75
    else:
        combos = [cards]

    rank = [0,0,0] # grade, of_what, with what
    
    if len(cards) >= 5:
        list_of_13 = [13]*5 # for getting of the value from encoded card 
    
    # for pre-ranking 
    else:
        list_of_13 = [13]*len(cards)

    grade_list = ['High card',
                'One pair',
                'Two pairs',
                'Three of a kind',
                'Straight',
                'Flush',
                'Full house',
                'Four of a kind',
                'Straight flush']
    
#   # grade encoding 
    grade_encode_dic = {}
    for (no,grade) in enumerate(grade_list):
        grade_encode_dic[grade] = no
    
#   # C75
    rank_record = []

    i = 0 # counter 
    for sample in combos:
        sample = list(sample)

        ### only vaule 
        values = [(a+1) % b for a, b in zip(sample, list_of_13)] # value without suit
        values = [14 if a == 1 else a for a in values] # 1 =A =14
        values = [13 if a == 0 else a for a in values] # 0 =k =13
        values.sort()

        longest_value = max(values, key=values.count) # 1-A 

        ### only suit 
        suits = [(x-1)//13 for x in sample] # S=0, H=1, D=2, C=3
        longest_suit = max(suits, key=suits.count) # 0,1,2,3

        ### def the MIN_STRAIGHT 
        MIN_STRAIGHT = [1,2,3,4,13] # 2,3,4,5,A
        min_straight = False

        ### find a flush  
        flush = False
        if suits.count(longest_suit) == 5:
            flush = True
            of_what = max(values)
        
        ### find a straight 
        straight = False
        if MIN_STRAIGHT == values:
            min_straight = True
            straight = True
            of_what = 1

        elif (max(values)-min(values)) == 4:
            if len(set(values)) <=4:
                pass
            else: 
                assert len(set(values)) ==5,'wrong len(set(values))'
                straight = True
                of_what = max(values)

#g8     ### find a straight flush 
        if flush and straight: 
            straight_flash = True 
            if min_straight == True:
                of_what = 1
                with_what = [0]
            else:
                of_what = max(values)
                with_what = [0]

            rank = [grade_encode_dic['Straight flush'], of_what, with_what]

#g7     ### find a four of a kind
        elif values.count(longest_value) == 4:
            four_of_a_kind = True
            of_what = longest_value
            with_what = [x for x in values if x != longest_value]

            rank = [grade_encode_dic['Four of a kind'], of_what, with_what]

#g6     ### find a full house 
        elif values.count(longest_value) == 3: 
            rest_of_values = [x for x in values if x != longest_value]
            assert len(rest_of_values) == 2, 'wrong algo fo rest of values'

            if rest_of_values[0] == rest_of_values[1]:
                full_house = True
                of_what = longest_value
                with_what = rest_of_values
                
                rank = [grade_encode_dic['Full house'], of_what, with_what]

#g3     ### find a three of a kind
            else:
                three_of_a_kind = True
                of_what = longest_value    
                with_what = rest_of_values
                
                rank = [grade_encode_dic['Three of a kind'], of_what, with_what]

#g5     ### find a flush
        elif flush:
            of_what = max(values)
            with_what =[0]
            
            rank = [grade_encode_dic['Flush'], of_what, with_what]

#g4     ### find a straight 
        elif straight:
            if MIN_STRAIGHT:
                of_what = 1
                with_what =[0]
            else:
                of_what = max(values)
                with_what =[0]

            rank = [grade_encode_dic['Straight'], of_what, with_what]

#g2     ### find two pairs 
        elif values.count(longest_value) == 2: # if two pairs will first find the smaller pair 
            rest_of_values = [x for x in values if x != longest_value] # may has the bigger one 
            if rest_of_values == []:
                rest_of_longest_value = 1 # no 1 in this system, pass the next if (for pre-ranking)
            else:
                rest_of_longest_value = max(rest_of_values, key=rest_of_values.count)

            if rest_of_values.count(rest_of_longest_value) == 2: # find the second(bigger) pair
                two_pairs = True
                of_what = rest_of_longest_value # bigger one is in the rest
                with_what = [longest_value*10, [x for x in rest_of_values if x != rest_of_longest_value][0]] # smaller pair *10 

                rank = [grade_encode_dic['Two pairs'], of_what, with_what]

#g1     ### find a pair 
            else: # only one pair
                of_what = longest_value
                with_what = rest_of_values

                rank = [grade_encode_dic['One pair'], of_what, with_what]

#g0     ### high card
        else:
            high_card = True
            of_what = 0
            with_what = values

            rank = [grade_encode_dic['High card'], 0, with_what]

        rank_record.append(rank)
        i += 1

#   ### encode rank
    rank_encode_record = []
    
    for rank in rank_record:
        rank_encode = 0
        rank_encode += rank[0]*1e12 # grade* 1e12
        rank_encode += rank[1]*1e10 # of_what* 1e10

        rank[2].sort()
        counter = 0
        for what in rank[2]: # small one to big 
            #print(rank_encode)
            rank_encode += what*(10**(2*counter))
            #print(rank_encode)
            counter +=1

        rank_encode_record.append(rank_encode)

    #print(rank_encode_record)
        
    return max(rank_encode_record)

#%%
### test 

if __name__ == "__main__":
    deck = cards.Deck()

    card_dic, card_encode, card_str = deck.deck()
    shuffled_encode = deck.encode_shuffle()
    
    cards_encode_list = shuffled_encode[0:7]
    cards_list = [card_dic[x] for x in cards_encode_list]

    A = ranking(cards_encode_list)
    B = ranking(cards_encode_list[0:2])
    
    print(f'\n Cards:\n  {cards_list}\n')
    
    try:
        print(f'\nA-Codes:\n {A} \n')
        print(f'\nB-Codes:\n {B} \n')
    except: 
        print('wrong rules')