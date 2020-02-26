# list_of_random_things = [1, 3.4, 'a string', True]
# print(list_of_random_things[len(list_of_random_things) - 1])
# print(list_of_random_things[2:])
# print('this' in 'this is a string');
# print(5 not in [1, 2, 3, 4, 6])
# list = ["fore", "aft", "starboard", "port"]
# new_str = "".join(list)
# list.append("oip")
# print(list)

# a = [1, 5, 8]
# b = [2, 6, 9, 10]
# c = [100, 200]

# print(max([len(a), len(b), len(c)]))
# print(min([len(a), len(b), len(c)]))

# names = ["Carol", "Albert", "Ben", "Donna"]
# print(" & ".join(sorted(names)))

# a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# b = set(a)
# print(b);
# print(len(a) - len(b))

# a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# b = set(a) # set prints out unique values from a list or Array
# b.add(5)
# b.pop()
# print(b)

# # Dictionaries is like an object
# population = {
#     "Shanghai":	17.8,
#     "Istanbul":	13.3,
#     "Karachi":	13.0,
#     "Mumbai":	12.5
# }
# print(population)

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a == b)
# print(a is b)
# print(a == c)
# print(a is c)

# animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

# phone_balance = 10
# bank_balance = 50

# if phone_balance < 10:
#     phone_balance += 10
#     bank_balance -= 10

# print(phone_balance)
# print(bank_balance)

#Second Example - try changing the value of number

# number = 145
# if number % 2 == 0:
#     print("Number " + str(number) + " is even.")
# else:
#     print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
# age = 35

# Here are the age limits for bus fares
# free_up_to_age = 4
# child_up_to_age = 18
# senior_from_age = 65

# These lines determine the bus fare prices
# concession_ticket = 1.25
# adult_ticket = 2.50

# Here is the logic for bus fare prices
# if age <= free_up_to_age:
#     ticket_price = 0
# elif age <= child_up_to_age:
#     ticket_price = concession_ticket
# elif age >= senior_from_age:
#     ticket_price = concession_ticket
# else:
#     ticket_price = adult_ticket

# message = "Somebody who is {} years old will pay {} to ride the bus.".format(age, ticket_price)
# print(message)
# points = 174

# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#     result = "Oh dear, no prize this time."
# elif points <= 180:
#     result = "Congratulations! You won a wafer-thin mint!"
# else:
#     result = "Congratulations! You won a penguin!"

# print(result)


cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for i in range(len(cities)):
    cities[i] = cities[i].title()

print(cities);

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

# Quiz Solution: Modify Usernames with Range
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)

# Quiz Solution: Tag Counter
# You can use string indexing to find out if each token begins and ends with angle brackets.

tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

# Quiz Solution: Create an HTML List
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

# Solution: Fruit Basket - Tasks 1 & 2
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

print(basket_items.items())

for object, count in basket_items.items():
   if object in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))



# Solution: Fruit Basket - Task 3
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))

# Solution: Factorials with While Loops
# Here is our solution for this one:


# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

# Solution: Factorials with For Loops
# Here is our solution for this one, using a for loop to find the factorial of a number:


# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(1,7):
    product *= num

# print the factorial of number
print(product)

for i in range(1,10): 
    print(i, end =" ") 
print() 

# Solution: Count By
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

# Solution: Nearest Square
limit = 40

num = 0
while (num+1)**2 < limit:
    print(num + 1)
    num += 1
nearest_square = num**2

print(nearest_square)

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))