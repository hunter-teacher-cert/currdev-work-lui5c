# Class 11 - lists + loops summative assessment

### Learning Objective[s]

### Standards

* **9-12.CT.4** - Implement a program using a combination of student-defined and third-party functions to organize the computation.

* **9-12.CT.8** - Develop a program that effectively uses control structures in order to create a computer program for practical intent, personal expression, or to address a societal issue.

* **9-12.CT.9** - Systematically test and refine programs using a range of test cases, based on anticipating common errors and user behavior.

* **9-12.CT.10** - Collaboratively design and develop a program or computational artifact for a specific audience and create documentation outlining implementation features to inform collaborators and users.


### Materials & Resources

## Summative Assessment

1. Give an example of a task that a **while** loop could accomplish, but not a **for** loop. Your answer should **not** be in code. Feel free to use an example from one of the labs we did. 

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

2. Give an example of a task that a **for** loop could accomplish, but not a **while** loop. Your answer should **not** be in code. Feel free to use an example from one of the labs we did. 

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

3. Write a program that uses a while loop to calculate the **sum of the first ten even numbers**. 

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
  
  
4. Write a program that uses a **for loop** to do the **same task as #3** - calculate the sum of the first ten even numbers. 

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
  
**Program A**
```python
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
vehicles = ["car", "bike", "skateboard", "rollerskates"]
```
5. Write a program that prints out every combination of color and vehicle from Program A. Your program can print it out in any order - one possible order would be:

```
red car
red bike
red skateboard
red rollerskates
orange car
orange bike
orange skateboard
orange rollerskates
yellow car
```
...and so on.  

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
Questions 6, 7, and 8 have to do with Program B. Read it closely.  

**Program B**
```python
user_name = input("what is your name?")

alphabet = "abcdefghijklmnopqrstuvwxyz"

finished = []

for l in user_name:       # flag A
  a = 0
  while alphabet[a] != l: # flag B
    a += 1
  finished.append(a)

# flag

print("Output:")
for b in finished:
  print(b, end=" ")
```  
6. What does the for loop marked with flag A do?

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

7. What does the while loop marked with flag B do?

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp; 

8. What does this entire program do?

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  

9. If <code>finished = [10, 9, 3, 3]</code> were inserted at the line marked `#flag C`, what would this program output?  

&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
## In-Class Exercises

## Assignments
