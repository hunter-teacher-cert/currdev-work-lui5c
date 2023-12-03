"""
Assignment 4 Starter Code
For each exercise, pass `end=' '` to your `print` statements, like this:

print("hello", end="")

This makes your output easier to inspect.
"""

# Exercise 1
# Write a for loop that prints each number from 1 to 10. 
print("\nExercise 1")
for i in range(1, 11):
  print(i, end=" ")


# Exercise 2
# Write a for loop that prints each number from 1 to 100.
print("\nExercise 2")
for i in range(1, 101):
  print(i, end=" ")


# Exercise 3
# Write a for loop that prints each odd number from 1 to 99. 
print("\nExercise 3")
for i in range(1, 100, 2):
  print(i, end=" ")


# Exercise 4
# Write a for loop that prints the first 10 perfect squares (1, 4, 9, 16, etc. -- perfect squares have square roots that are whole numbers.)
print("\nExercise 4")
for i in range(1, 11):
  print(i**2, end=" ")


# Exercise 5
# Change only line A so that this program counts from 0 to 99. 
print("\nExercise 5")
for i in range(10):
    for j in range(10):
        print(i*10 + j, end=' ') ### line A


# Exercise 6
# Write a program that asks the user for an integer and then uses a for loop to print the first 5 multiples of that integer.
print("\nExercise 6")
num = int(input("type an integer: "))
for i in range(2, 7):
  print(num*i, end=" ")


# Extension Exercises
# 1. Write a program that sums up all of the 
#    numbers from 1 to a given number, using
#    a for loop. 
# 
# 2. Write a program that uses a for loop to 
#    determine how many digits are in an integer. 
#
# 3. Write a program that uses for loops 
#    or while loops to determine if a 
#    number is prime. 
# 
# print("Extension Exercises:")

# Extension 1
num = 10
sum = 0
for i in range(1, num+1):
  sum += i

# Extension 2
num = 1000
for i in range(10):
  if num - 10**i < 0:
    break

# Extension 3
num = 51
prime = True
for i in range(num // 2):
  if num % i == 0:
    prime = False
    break

