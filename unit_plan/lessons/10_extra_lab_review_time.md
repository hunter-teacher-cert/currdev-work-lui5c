# Class 10 - lists + loops lab time + review

### Learning Objective[s]

* There are no explicit learning objectives, other than the sum of all of the learning objectives already stated for this unit.

### Standards

* **9-12.CT.4** - Implement a program using a combination of student-defined and third-party functions to organize the computation.

* **9-12.CT.8** - Develop a program that effectively uses control structures in order to create a computer program for practical intent, personal expression, or to address a societal issue.

* **9-12.CT.9** - Systematically test and refine programs using a range of test cases, based on anticipating common errors and user behavior.

* **9-12.CT.10** - Collaboratively design and develop a program or computational artifact for a specific audience and create documentation outlining implementation features to inform collaborators and users.


### Materials & Resources

## Practice Assessment

1. Write a program that asks the user, "what is the password?" and only prints "correct!" if they type "testing123". 

2. Write two programs for each of the below bullet points - one program should use a for loop, the other should use a while loop.   
- Given a list `a = [1, 2, 3, 4, 5]`, write a program that prints the first five multiples of each number in `a`.
- Given a list `b` that contains all of the integers between 0 and 99, write a program that goes through `b` and prints out whether each number in `b` is prime.

3. Write out all of the list methods that you remember. What do they each do?

4. What does this program do? Be very descriptive.
```python

values = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")

for j in range(26):
  values.append(0)

sample = "the quick brown fox jumps over the lazy dog"

for letter in sample:
  values[alphabet.index(letter)] += 1


for i in range(len(values)):
  print(alphabet[i], values[i])
```

## Handouts

## In-Class Exercises

## Assignments
