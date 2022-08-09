import os
os.system('cls||clear')

#----CODE STARTS HERE------
import pickle

game = open('game.dat', 'rb')

if os.path.exists("basket.dat"):
    basket = open("basket.dat", "wb")
else: 
    basket = open("basket.dat", "xb")
    basket = open("basket.dat", "wb")

basket_data = []

while True:
    try:
        participant = pickle.load(game)
        if participant[0] == 'Basket Ball':
            basket_data.append(participant)
    except:
        break

for i in basket_data:
    pickle.dump(i,basket)

# ----------- Uncomment below if you want to check the display in basket.dat -----------

# basket = open("basket.dat", "rb")
# while True:
#         try:
#             participant = pickle.load(basket)
#             print(participant)
#         except EOFError:
#             break

basket.close()
game.close()