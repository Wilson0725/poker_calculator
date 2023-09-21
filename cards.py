import random

### class card
# class
class Deck(list):
    def __init__(self): 
        super(Deck,self).__init__()

        self.suit_map = {0: 'S', 1: 'H', 2: 'D', 3: 'C'}
        self.val_map ={}
        self.card_map={}
        self.card_encode = []

        return None

    def deck(self):

        card_code = list(range(1,53))

        for i in range(13):
            if i==8:
                self.val_map[i] = 'T'
            elif i==9:
                self.val_map[i] = 'J'
            elif i==10:
                self.val_map[i] = 'Q'
            elif i==11:
                self.val_map[i] = 'K'
            elif i==12:
                self.val_map[i] = 'A'
            else:
                self.val_map[i] = str(i+2)

        for i in card_code:
            if i==0:
                self.card_map[i] = 'N'
            else:
                self.card_map[i] = self.val_map[(i - 1) % 13] + self.suit_map[(i - 1) // 13]

                self.card_encode = list(self.card_map.keys())
                self.card_str = list(self.card_map.values())

        return self.card_map, list(self.card_map.keys()), list(self.card_map.values())
    
    def encode_shuffle(self):
        random.shuffle(self.card_encode)
        return self.card_encode       

if __name__ == "__main__":
    deck = Deck()

    card_dic, card_encode, card_str = deck.deck()
    print(f'\ncard_dic\n{card_dic}')
    print(f'\ncard_encode\n{card_encode}')
    print(f'\ncard_value\n{card_str}')

    shuffled_encode = deck.encode_shuffle()
    print(f'\nshuffled_encode\n{shuffled_encode}')


        

    