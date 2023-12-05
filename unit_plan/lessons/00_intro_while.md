# Class 00 - intro to while loops

### Learning Objective[s]

* Students will be able to explain in words what a while loop is and how it is similar to an if statement in Python.
* Students will be able to write simple while loops independently. 

### Standards

* **9-12.CT.4** - Implement a program using a combination of student-defined and third-party functions to organize the computation.

* **9-12.CT.8** - Develop a program that effectively uses control structures in order to create a computer program for practical intent, personal expression, or to address a societal issue.

* **9-12.CT.9** - Systematically test and refine programs using a range of test cases, based on anticipating common errors and user behavior.

* **9-12.CT.10** - Collaboratively design and develop a program or computational artifact for a specific audience and create documentation outlining implementation features to inform collaborators and users.

### Materials & Resources

```python
"""
Review: Conditionals are used after 'if' statements. 

They check if something is true or if something equals something.

You can use:
- and
- not
- or
- ()
- ==
- !=

examples:

name = "Luis"

if name != "Luis":
  print("Hello.")
else:
  print("Hello, Luis.")

Exercise 0: Modify the following code so that the sentences printed out are true. 
"""

age = 3

if age < 4: # change this line
  print("People aged", age, "and higher are allowed to drive.")


if age < 4: # change this line
  print("People aged", age, "and higher are allowed to buy cigarettes.")


if age < 4: # change this line
  print("People that are", age, "years old are considered teenagers.")


"""
Indefinite Loops

Indefinite Loops are like if statements, except that the conditional at the top is RE-RUN AT THE END OF THE BLOCK.

Exercise 1:
Below is an infinitely running while loop. 
Fix it to print the numbers 0-4, inclusive. 
"""

# # Uncomment these lines by highlighting all of them and pressing Ctrl + /

# print("Exercise 1:")
# count = 0 

# while count == 0:
#   print(count)

"""
Exercise 2:

Write a while loop that prints out the numbers 0-10, inclusive.
"""

# put exercise 2 here. 

# print("Exercise 2:")


"""
Exercise 3:

Write a while loop that prints the following output:
a
aa
aaa
aaaa
aaaaa
aaaaaa
"""
# write exercise 3 here.

# print("Exercise 3:")

"""
Exercise 4:

Write a while loop that prints every even number from 0 to 100. 
"""

# write exercise 4 here.

# print("Exercise 4:")

"""
Exercise 5:
Write a while loop that prints the first 20 powers of 2.
(1, 2, 4, 8, 16, 32, 64, 128, etc...)
"""

# write exercise 5 here. 

# print("Exercise 5:")

"""
Exercise 6:
Write a short program that takes a number from the user, and counts down from that number. 
"""

# write exercise 6 here. 

# print("Exercise 6:")

# number = int(input("What number are we counting down from?"))


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
4. Have an if statement in the while loop
5. Have a print statement in the if block
"""

# write your independent practice program below. 



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
Hint: You will need 3 while loops for this.
"""

# write your optional challenge programs below. 
```
## In-Class Exercises

The 6 exercises listed above are the in-class activity for the day. Before any coding is done, while loops are demonstrated on the board. 

## Assignments
On Google Classroom: 

Problems 5.1.1, 5.1.2, and 5.1.3 from:
 https://runestone.academy/ns/books/published/CS1-Python-Subgoals/while_counter.html?mode=browsing

Write a 1 sentence explaining each answer as a private comment on the Google Classroom assignment. 