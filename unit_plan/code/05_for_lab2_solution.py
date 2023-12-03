"""
Definite Loops (for) Lab II

Use this starter code to create the design goal.

Don't change the setup code OR the code sandwiched between comments that say "DON'T TOUCH!"

"""

# setup - do not change!
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.setup(1.0, 1.0)
t.penup()
t.speed(0)

t.goto(-200, 150)
t.pendown()
t.setheading(0)



# BEGIN TRIANGLE CODE --- vvvvvvvvvvvvvvvvv
for i in range(3):
  t.forward(100)
  t.right(120)

# END TRIANGLE CODE --- ^^^^^^^^^^^^^^^^




# DONT TOUCH
t.penup()
t.goto(50, 150)
t.pendown()
t.setheading(0)
# DON'T TOUCH





# SQUARE CODE --- vvvvvvvvvvvvvvvvv
for i in range(4):
  t.forward(100)
  t.right(90)
# END SQUARE CODE--- ^^^^^^^^^^^^^^^^






# DON'T TOUCH
t.penup()
t.goto(-200, -50)
t.pendown()
t.setheading(0)
# DON'T TOUCH







# BEGIN STAR CODE --- vvvvvvvvvvvvvvvvv
for i in range(5):
  t.forward(75)
  t.left(144)
# END STAR CODE --- ^^^^^^^^^^^^^^^^




# DON'T TOUCH
t.penup()
t.goto(50, -50)
t.pendown()
t.setheading(0)
# DON'T TOUCH





# INFINITE DESIGN CODE --- vvvvvvvvvvvvvvvvv
for i in range(120):
  t.forward(100)
  t.left(122)
# END DESIGN CODE --- ^^^^^^^^^^^^^^^^






# DON'T TOUCH
t.penup()
t.goto(-50, 0)
t.pendown()
t.setheading(0)
# DON'T TOUCH











# ODD-POINTS STAR CODE --- vvvvvvvvvvvvvvvvv
amount_of_sides = 9

for i in range(9):
  t.forward(50)
  t.left(2*360/amount_of_sides)
# END ODD-POINTS STAR CODE --- ^^^^^^^^^^^^^^^^



input()