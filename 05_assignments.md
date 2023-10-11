# Assignment 5
Develop two assignments that are different types for your unit plan.
Describe the assignment, including student facing instructions in a markdown file.

My unit plan is an introductory curriculum for Python using Python with Turtle. 


## Assignment 1 - Lists Practice
### Description
The purpose of this homework assignment is to practice working with lists, which were first introduced on Monday. Write up your responses on a loose leaf sheet of paper. 
### Assignment
1. Write a line of python that creates a variable a and sets it equal to a list holding the first 5 numbers of the school’s phone number. 
2. Write a line of Python that creates a variable b and sets it equal to a list with one integer, one string, and one float.
3. In one sentence, explain why program A prints “Boop!”
4. Modify line 1 of Program A so that it prints “Beep!”

**Program A**
```python
my_list = [1, 0, 1, 0, 4, 5]
if my_list[0] < my_list[2]:
  print(“Beep!”)
else:
  print(“Boop!”)
```


5. What is the output of line A in program B?
6. What is the output of line B in program B?
7. What is the output of line C in program B?

**Program B**
```python
my_list = [1, 3, 4]
my_list.append(0)
my_list.append(3)
print(my_list)    # **** line A ****
my_list = my_list + my_list
print(my_list)    # **** line B ****
print(my_list[0]) # **** line C ****
```


8. For each line of program C, write what would happen if you entered it into Python’s REPL.
**Program C**
```python
a = [1, 2, 3]
print(a[0])
print(a[-1])
a[0] > a[2]
a[4]
a.append(a[0])
a.append(a[0])
a
len(a)
a.pop(0)
a
a.remove(3)
a
```



## Assignment 2 - For loops
### Description
The purpose of this assignment is for you to further practice the for loops that we practiced in class today.   
For each exercise, write your code under the appropriate comment.  
For each exercise, pass `end=' '` to your `print` statements, like this:  
```python
print("hello", end="")
```
This makes your output easier to inspect.
### Assignment
1. Write a for loop that prints each number from 1 to 10. 
2. Write a for loop that prints each number from 1 to 100.
3. Write a for loop that prints each odd number from 1 to 99. 
4. Write a for loop that prints the first 10 perfect squares (1, 4, 9, 16, etc. -- perfect squares have square roots that are whole numbers.)
5. Change the 0 on line A so that this program to count from 0 to 99. 
```python
for i in range(10):
    for j in range(10):
        print(0, end='') ### line A
```
6. Write a program that asks the user for an integer and then uses a for loop to the first 5 multiples of that integer.

```python
# Assignment 2 Starter Code

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
# Change the 0 on line A so that this program to count from 0 to 99. 
print("\nExercise 5")

for i in range(10):
    for j in range(10):
        print(0, end='') ### line A


# Exercise 6
# Write a program that asks the user for an integer and then uses a for loop to the first 5 multiples of that integer.
print("\nExercise 6")


```