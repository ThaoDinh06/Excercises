# dic: key - value
# import random function
# random.choice(dic.keys())
# end-use gona guess
# whether match or not
# if it's match, it will print meaning of word to screen, vice versa

from gettext import ngettext
import random
Dictionary = {"man": ["đàn ông"], 
            "woman": ["đàn bà", "phụ nữ"],
            "house": ["nhà", "ngôi nhà", "căn nhà"], 
            "sun": ["mặt trời"],
            "moon": ["mặt trăng"], 
            "earth": ["trái đất", "quả đất", "địa cầu"],
            "mountain": ["núi", "ngọn núi"], 
            "river": ["sông", "con sông"],
            "tree": ["cây cối", "cây"],
            "good": ["tốt", "ngon", "giỏi", "hay"]
            }

randomKey = random.choice(list(Dictionary.keys()))
print('The word "' + randomKey + '" means: ')
word = input("Your answer is: ")

for i in Dictionary.get(randomKey):
    if word == i:
        print("You're right.")
        break
else:
    print("You're wrong. The word '" + randomKey + "' means " + str(Dictionary.get(randomKey)))

