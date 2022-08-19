import os
os.system('cls||clear')
# The cover price of a book is $24.95, but bookstores get a 40 percent discount. Shipping costs $3 for the ﬁrst copy and 
# 75 cents for each additional copy. Calculate the total wholesale costs for the given number of books.
#----CODE STARTS HERE------

# book = 24.95
# copy = float(input())
# shipping = ((copy - 1) * 0.75) + 3
# book *= copy
# discount = book * 0.4
# book -= discount
# print(book + shipping)

# Constant variable for book price, first copy shipping price, and the discount
BOOK = 24.95
SHIP = 3
DISCOUNT = BOOK * 0.4

# input for how many copies
copy = int(input())

# discounted price of all the books ordered
discounted = BOOK - DISCOUNT

# additional shipping price
shipping = (copy - 1) * 0.75 + SHIP

# total price of books depends on how many copies
total_books = discounted * copy

# total price of books plus the shipping fees
total_price = total_books + shipping

# to print the total price
print(total_price)