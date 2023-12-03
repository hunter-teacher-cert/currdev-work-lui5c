"""
For this lab, you'll be implementing all of the exercises that we did for while loops, except using for loops. 

Definite Loops

Definite loops run a specific amount of times.

Exercise 1:
Write a for loop that prints the numbers 0-4, inclusive. 
"""

# # Uncomment these lines by highlighting all of them and pressing Ctrl + /

# print("Exercise 1:")
for i in range(5):
  print(i, end=" ")
print()
"""
Exercise 2:

Write a while loop that prints out the numbers 0-10, inclusive.
"""

# put exercise 2 here. 

print("Exercise 2:")
for i in range(11):
  print(i, end=" ")
print()


"""
Exercise 3:

Write a for loop that prints the following output:
a
aa
aaa
aaaa
aaaaa
aaaaaa
"""
# write exercise 3 here.

print("Exercise 3:")
for i in range(1, 7):
  print("a"*i)

"""
Exercise 4:

Write a for loop that prints every even number from 0 to 100. 
"""

# write exercise 4 here.
print("Exercise 4:")
for i in range(0, 101, 2):
  print(i, end=" ")
print()

"""
Exercise 5:
Write a for loop that prints the first 20 powers of 2.
(1, 2, 4, 8, 16, 32, 64, 128, etc...)
"""

# write exercise 5 here. 
print("Exercise 5:")
for i in range(20):
  print(2**i, end=" ")
print()

"""
Exercise 6:
Write a short program that takes a number from the user, and counts down from that number. 
"""

# write exercise 6 here. 
print("Exercise 6:")
number = int(input("What number are we counting down from?"))
for i in range(number, -1, -1):
  print(i)



"""
Independent practice:

Using the modulo operator (%) and while and if, 
write a program that prints out all of the 
factors of a number. Here is a useful (!) snippet
of code that prints a factor if it is a factor of
a number.

if number % factor == 0:
  print(factor)

Your program should:
1. Ask the user for a number.
2. Create a variable called factor
3. Have a while loop that uses factor and number in the conditional
4. Have an if statement in the for loop
5. Have a print statement in the if block
"""

# write your independent practice program below. 
num = int(input("type a number: "))
print("the factors of", num, "are: ")
for i in range(1, num+1):
  if num % i == 0:
    print(i, end=" ")
print()


"""
Optional challenges:

1. Write a program that asks the user for a number, n, 
and prints the first n numbers of the Fibonacci sequence.

2. Write a program that makes a zigzag pattern
in the terminal, like this:
_____
____
___
__
_

_
__
___
____
_____
____
___
etc.
Hint: You will need 1 while loop and 2 for loops for this.

3. Write another version of your lab #1 with while loops to only give the user 6 tries to guess the number. Keep track of the user's win/loss percentage, instead of a high score. 
"""

# write your optional challenge programs below. 

# Exercise 1:

a = int(input("which term should I stop at?"))
nminus1 = 1
n = 1
temp = 0
if a == 1 or a == 2: print(nminus1)
else:
  for i in range(a-1):
    temp = n
    n = n + nminus1
    nminus1 = temp
    print(n)


# Exercise 2:
for i in range(3):
  for i in range(6):
    print("-"*i)
  for i in range(6):
    print("-"*(6-i))

# Exercise 3: verified upon turning in.