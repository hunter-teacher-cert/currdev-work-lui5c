# Class 06 - intro to lists

### Learning Objective[s]

* Students will be able to use lists to store collections of data in Python.  
* Students will be able to use the documentation/reference sheet for lists to write their own practice exercises for lists.   
* Students will be able to differentiate between the list methods that return a value and the list methods that 
only mutate a list. 

### Standards

* **9-12.CT.4** - Implement a program using a combination of student-defined and third-party functions to organize the computation.

* **9-12.CT.8** - Develop a program that effectively uses control structures in order to create a computer program for practical intent, personal expression, or to address a societal issue.

* **9-12.CT.9** - Systematically test and refine programs using a range of test cases, based on anticipating common errors and user behavior.

* **9-12.CT.10** - Collaboratively design and develop a program or computational artifact for a specific audience and create documentation outlining implementation features to inform collaborators and users.


### Materials & Resources

These are the questions that will be posted on Google Classroom for students to work on independently, in their own file titled `lists.py`.

0. (kind of long) - Using the resources [here](https://www.w3schools.com/python/python_ref_list.asp), demonstrate your understanding of each list method by implementing each method once with a sample list. 

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

9. Extension: write a program that creates a grocery list for a user. The program should use a while loop to add items to the grocery list until the user types `done`, and then the list should be printed for the user. 

## Handouts

## In-Class Exercises

## Assignments

No homework :)
