from turtle import Turtle, Screen

# Create a Turtle object named "tim"
tim = Turtle()

# Create a Screen object to handle the GUI
screen = Screen()


# Function to handle generic key presses
# Currently prints the pressed key to the console
def handle_press(key: str):
    print(key)


# Function to move the turtle forward by 10 units
def move_forward():
    tim.forward(10)


# Function to turn the turtle 10 degrees to the right
def turn_right():
    tim.right(10)


# Function to turn the turtle 10 degrees to the left
def turn_left():
    tim.left(10)


# Function to move the turtle backward by 10 units
def move_backward():
    tim.backward(10)


# Make the screen listen for key presses
screen.listen()

# Bind keyboard keys to specific turtle control functions
screen.onkey(key="w", fun=move_forward)  # Move forward
screen.onkey(key="a", fun=turn_left)  # Turn left
screen.onkey(key="d", fun=turn_right)  # Turn right
screen.onkey(key="s", fun=move_backward)  # Move backward
screen.onkey(key="c", fun=screen.bye)  # Exit program on "c"

# Keeps the screen open until it is clicked again for termination
screen.exitonclick()