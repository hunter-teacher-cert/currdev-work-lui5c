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
i = 0
while i < 3:
  t.forward(100)
  t.right(120)
  i += 1

# END TRIANGLE CODE --- ^^^^^^^^^^^^^^^^






# DONT TOUCH
t.penup()
t.goto(50, 150)
t.pendown()
t.setheading(0)
# DON'T TOUCH





# SQUARE CODE --- vvvvvvvvvvvvvvvvv
i = 0
while i < 4:
  t.forward(100)
  t.right(90)
  i += 1

# END SQUARE CODE--- ^^^^^^^^^^^^^^^^






# DON'T TOUCH
t.penup()
t.goto(-200, -50)
t.pendown()
t.setheading(0)
# DON'T TOUCH







# BEGIN STAR CODE --- vvvvvvvvvvvvvvvvv
i = 0
while i < 5:
  t.forward(100)
  t.right(144)
  i += 1

# END STAR CODE --- ^^^^^^^^^^^^^^^^




# DON'T TOUCH
t.penup()
t.goto(50, -50)
t.pendown()
t.setheading(0)
# DON'T TOUCH





# INFINITE DESIGN CODE --- vvvvvvvvvvvvvvvvv
i = 0
while i < 60:
  t.forward(100)
  t.right(122)
  i += 1

# END DESIGN CODE --- ^^^^^^^^^^^^^^^^






# DON'T TOUCH
t.penup()
t.goto(-50, 0)
t.pendown()
t.setheading(0)
# DON'T TOUCH











# ODD-POINTS STAR CODE --- vvvvvvvvvvvvvvvvv
amount_of_sides = 9

i = 0
while i < amount_of_sides:
  t.forward(50)
  t.right(2*360/amount_of_sides)
  i += 1

# END ODD-POINTS STAR CODE --- ^^^^^^^^^^^^^^^^



input()