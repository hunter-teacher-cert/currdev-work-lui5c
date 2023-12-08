# Class 03 - intro to definite loops

### Learning Objectives

* Students will be able to write a for loop independently in Python.

* Students will be able to use the loop variable correctly in for loops.

* Students will be able to connect their work with for loops to their understanding of while loops. 

* Students will be able to identify the parts of a for loop that distinguish it from a while loop. 

### Standards

* **9-12.CT.4** - Implement a program using a combination of student-defined and third-party functions to organize the computation.

* **9-12.CT.8** - Develop a program that effectively uses control structures in order to create a computer program for practical intent, personal expression, or to address a societal issue.


### Materials & Resources

The following source code file:

```python
"""
Class 3 Starter Code
For each exercise, pass `end=' '` to your `print` statements, like this:

print("hello", end="")

This makes your output easier to inspect.
"""

# Exercise 1
# Write a for loop that prints each number from 1 to 10. 
print("\nExercise 1")



# Exercise 2
# Write a for loop that prints each number from 1 to 100.
print("\nExercise 2")



# Exercise 3
# Write a for loop that prints each odd number from 1 to 99. 
print("\nExercise 3")



# Exercise 4
# Write a for loop that prints the first 10 perfect squares (1, 4, 9, 16, etc. -- perfect squares have square roots that are whole numbers.)
print("\nExercise 4")



# Exercise 5
# Change only line A so that this program counts from 0 to 99. 
print("\nExercise 5")

for i in range(10):
    for j in range(10):
        print(0, end=' ') ### line A


# Exercise 6
# Write a program that asks the user for an integer and then uses a for loop to print the first 5 multiples of that integer.
print("\nExercise 6")



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
# print("Extension Exercises:")

```

## Handouts

## In-Class Exercises

The following demos will be done:
```python

print("while:")
i = 0
while i < 5:
    print(i)
    i = i + 1

print("for:")
for i in range(5):
    print(i)

for i in range(0, 5, 1):
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(0, 100, 2):
    print(i)

for i in range(100, 0, -2):
    print(i)


for i in range(3):
    print(i)
    for j in range(3):
        print("hip", end=", ")
    print("hooray!")


```

The in-class exercises are contained in the source file that the students receive. 


## Assignments

Problems 5.3.1, 5.3.2, 5.3.3 from 
https://runestone.academy/ns/books/published/CS1-Python-Subgoals/for_loop_range.html?mode=browsing

Write your answer to the problem as a private comment on Google Classroom. 