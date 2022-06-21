magicians = ['alice','david','carolina']
for magician in magicians:
    print(f" {magician.title()}.\n")
#  function for variable in list pulls each item in the list and do action that was linked to it like printing each name in example
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick {magician.title()}.\n")
# \n inserts a blank line after each loop
print("Thank you everyone. That was a great magic show!")
# making numerical list. Using range() function
for value in range(1,6):
    print(value)
# does not include 6, the last number in the range doesnt print
# using range() to make a list of numbers 
numbers = list(range(1,6))
print (numbers)
# list() function converst range of numbers in the set of numbers
even_numbers = list(range(2,11,2))
print(even_numbers)
# using range to create list with even numbers starts with value 2, then adds 2 until it reaches 11
squares =[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)    
# example how to create square list from range (1,11)

# simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)
print(sum(digits))
squares = [value**2 for value in range(1,11)]
print(squares)
# wxample how to create squares different approach


# slicing a list
players = ['ben','john','michael', 'jerry', 'charles']
print(players[0:3])
# starts with the first name in the list
print(players[1:4])
# starts with second name in the list
print(players[:4])
# without starting index python starts at the beginnings of the list
print(players[:2])
#  prints only two starting names
print(players[2:])
# prints every name excludes first two names
print(players[-3:])
# print names of the last three persons
print("Here are the first three playesrs of our team")
for player in players[:3]:
    print(player.title())

# copying a list 
my_foods=['pizza', 'falafel','carrot cake']
friends_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)
# list are independent 
my_foods.append('cannoli')
friends_foods.append('ice cream')
print(my_foods)
print(friends_foods)

# Tuples creates list of items that can't be changed
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
# a tuple looks like a list except using parentheses instead of square brackets
# lets try change tuple
# dimensions[0]=250
# print(dimensions[0]) gives error message
my_t=(3,)
# defines tuple with one element with a comma
# although you cant modify atuple you can assign a new value to a variable
dimensions=(200,50)
print("\nOriginal dimensions are:")
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print("\nModified dimensions are:")
for dimension in dimensions:
    print(dimension)    