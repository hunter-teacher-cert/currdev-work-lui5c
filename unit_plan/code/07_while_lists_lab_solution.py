# Lists + While lab

# Task 1: write a program that asks the user for integers to be put into a list. Convert every number that the user enters into an integer and then append the integers to a list. When the user types "done", stop adding to the list.

numlist = []
toAdd = ""
while toAdd != "done":
  toAdd = input("add a number:")
  if toAdd != "done":
    numlist.append(int(toAdd))


# Task 2: write a while loop that goes through the list that the user generated and prints out the maximum value.

maximum = float("-inf")
i = 0
while i < len(numlist):
  if numlist[i] > maximum:
    maximum = numlist[i]
  i += 1

print("The maximum of the list is", maximum)

# Task 3: write a while loop that goes through the list that the user generated and prints out the minimum value. 

minimum = float('inf')
i = 0
while i < len(numlist):
  if numlist[i] < minimum:
    minimum = numlist[i]
  i += 1

print("The minimum of the list is", minimum)

# Extension task: See if you can use your knowledge of loops and lists to sort the list of integers from smallest to greatest. 

# Answers may vary. Here is one example. 

sorted_list = []
while len(numlist) > 0:
  i = 0 
  min_index = 0
  while i < len(numlist):
    if numlist[i] < numlist[min_index] or i == 0:
      min_index = i

    # at the end of the loop
    if i == len(numlist)-1:
      toPop = numlist.pop(min_index)
      sorted_list.append(toPop)
    i += 1

print("sorted list:", sorted_list)