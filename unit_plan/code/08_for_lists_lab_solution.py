# Lists + For lab
"""
Ice Cream Combinations
The person using your program runs a frozen yogurt shop. They would like to make a banner sharing how many combinations of frozen yogurt, mix-ins, and toppings are available. They hire you to write a program to find out all of the available combinations. Combinations look like this:

Vanilla
Chocolate with blueberries and chocolate sprinkles
Strawberry with boba
"""

# Task 1: Create 4 empty lists:
# flavors, mixins, toppings, and all_combinations
flavors = []
mixins = []
toppings = []
all_combinations = []


# Task 2: using .append(), populate your first 3 lists.
# Flavors: vanilla, chocolate, strawberry, butter pecan, and mango
# Mix-ins: blueberries, boba, strawberries, granola, oreo
# Toppings: rainbow sprinkles, chocolate sprinkles, caramel syrup, chocolate syrup
flavors.append("vanilla")
flavors.append("chocolate")
flavors.append("strawberry")
flavors.append("butter pecan")
flavors.append("mango")
mixins.append("blueberries")
mixins.append("boba")
mixins.append("strawberries")
mixins.append("granola")
mixins.append("oreo")
toppings.append("rainbow sprinkles")
toppings.append("chocolate sprinkles")
toppings.append("caramel syrup")
toppings.append("chocolate syrup")

# Task 3: Use a for loop to add each flavor to the all_combinations list. 
for f in flavors:
  all_combinations.append(f)


# Task 4: Use two different for loops to add all combinations of 1 flavor and 1 mixin to the all_combinations list. 
for f in flavors:
  for m in mixins:
    all_combinations.append(f"{f} with {m}")


# Task 5: Use three different for loops to add all combinations of 1 of each ingredient to the all_combinations list. 
for f in flavors:
  for m in mixins:
    for t in toppings:
      all_combinations.append(f"{f} with {m}, topped with {t}")

# Task 6: Go back and make sure that the combinations in your list look good when printed. 
# Done


# Task 7: print all combinations with a comma in between them. Print out how many combinations there are.
for c in all_combinations:
  print(c, end=",") if all_combinations.index(c) < len(all_combinations)-1 else print(c)

print(len(all_combinations), "total combinations. ")


# Extension task 1: use list.indexOf(element) and the following pricing lists to add a price to each combination:
flavor_price = [2, 1.8, 2.2, 3, 1.5]
mixin_price = [2, 1, 2, 2, 1]
topping_price = [1, 1, 2, 2]

# Extension task 2: Expand your program to work with user input - use while loops to accomplish the user input. Do not worry about prices with this extension.