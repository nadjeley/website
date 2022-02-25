import turtle
import random

window = turtle.Screen()
window.bgcolor('black')

# Create a turtle, named Kevin
kevin = turtle.Turtle()
kevin.speed(0)

# function to draw fireworks
def draw_firework(t):
  x = random.randint(-300,300)
  y = random.randint(-300,300)

  kevin.penup()
  kevin.goto(x,y)
  kevin.pendown()

  # TODO #1: create a variable to change the firework size then use that variable in the forward and backward methods
  travel = random.randint(5,100)
  for i in range(36):
    kevin.forward(travel)
    kevin.backward(travel)
    kevin.right(10)

# Draw five fireworks
for i in range(5):
  #TODO #2: Create three variables r, g, and b and set their values equal to a random number between 0 and 255. Replace the color blue with kevin.color(r,g,b)
  r= random.randint(0,255)
  g= random.randint(0,255)
  b= random.randint(0, 255)
  kevin.color(r, g, b)
  draw_firework(kevin)


def draw_stars(t):
  x = random.randint(-300,300)
  y = random.randint(-300,300)

  kevin.penup()
  kevin.goto(x,y)
  kevin.pendown()

  for i in range(5):

   kevin.forward(10)
   kevin.right(144)


for i in range(20):
  kevin.color("white")
  draw_stars(kevin)
