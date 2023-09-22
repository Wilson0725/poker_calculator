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
    grade_encode_dic[grade] = no+1

print(grade_encode_dic)