import turtle
rex = turtle.Turtle()
rex.color("green")

# Task 1. Ask the user to input how wide a circle to draw.
print("How wide do you want the circle to be?")
# Store the response in a variable

radius = (input("Enter a radius for the circle: "))

# Task 2. Convert the response to a number, store it in a new variable


# Task 3. Draw a circle using the input as the radius


# Task 4: Update task 2 to inform the user if the response is not a number
if radius is.digit():
    wide=int(radius)
    rex.circle(wide)
else:
    print("please type a decimal number")
