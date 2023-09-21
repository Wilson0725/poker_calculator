import pandas as pd
from ranking import ranking
from range import ranger
from range import hand_trans,trans
from cards import Deck
from itertools import combinations
import os


deck = Deck()
card_dic, card_encode, card_value = deck.deck()
all_the_hands = list(combinations(card_encode,2))

class BillBoard():

    def __init_(self):
        pass
    
    def show(self, all_the_df:pd.DataFrame):
        print(all_the_df)

class PlayerBill(BillBoard):

    def __init__(self,*name):
        super(BillBoard,self).__init__()

        self.name = name

        self.straight_flush = []
        self.four_of_a_kind = []
        self.full_house = []
        self.flash = []
        self.straight = []
        self.three_of_a_kind = []
        self.two_pairs = []
        self.pair = []
        self.high = []
        self.score = 0
        self.avg_score = 0
            
    def updates(self,ranges,table):

        self.table = table
        counter = 0 # counting the hands filted out

        for hand in ranges:

            # filt off cards including tables 
            
            if hand[0] in table:
                counter += 1
                continue

            elif hand[1] in table:
                counter += 1
                continue

            else:
                cards = [x for x in hand] + table

                if ranking(cards) >= 8e12:
                    self.straight_flush.append(hand)

                elif ranking(cards) >= 7e12:
                    self.four_of_a_kind.append(hand)

                elif ranking(cards) >= 6e12:
                    self.full_house.append(hand)

                elif ranking(cards) >= 5e12:
                    self.flash.append(hand)

                elif ranking(cards) >= 4e12:
                    self.straight.append(hand)
                
                elif ranking(cards) >= 3e12:
                    self.three_of_a_kind.append(hand)

                elif ranking(cards) >= 2e12:
                    self.two_pairs.append(hand)

                elif ranking(cards) >= 1e12:
                    self.pair.append(hand)

                else:
                    self.high.append(hand)
                
                self.score += ranking(cards)
        
        self.avg_score = self.score/(len(ranges)-counter)
        
    def show(self): 

        print(f'\n {self.name} \n')

        self.result = {
                'table': trans(self.table),
                'avg_score':self.avg_score/1e12,
                'straight_flush':[hand_trans(x) for x in self.straight_flush],
                'four_of_a_kind':[hand_trans(x) for x in self.four_of_a_kind],
                'full_house':[hand_trans(x) for x in self.full_house],
                'flash':[hand_trans(x) for x in self.flash],
                'straight':[hand_trans(x) for x in self.straight],
                'three_of_a_kind':[hand_trans(x) for x in self.three_of_a_kind],
                'two_pairs':[hand_trans(x) for x in self.two_pairs],
                'pair':[hand_trans(x) for x in self.pair],
                'high_card':[hand_trans(x) for x in self.high]
                }
        
        self.result = pd.DataFrame({key: pd.Series(value) for key, value in self.result.items()})

        print(self.result)

    def save(self):
        
        self.result.to_csv(f'{self.name}_{self.table}.csv')


    
