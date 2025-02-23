# Turtle Etch-A-Sketch

This Python application allows users to control a turtle (a graphical representation) on the screen using keyboard commands. The application is built using Python's built-in `turtle` library and provides a simple, interactive way to control the movement and direction of the turtle.
## Features
- **Move Forward**: Press the **`W`** key to move the turtle forward by 10 units.
- **Turn Left**: Press the **`A`** key to rotate the turtle 10 degrees to the left.
- **Turn Right**: Press the **`D`** key to rotate the turtle 10 degrees to the right.
- **Move Backward**: Press the **`S`** key to move the turtle backward by 10 units.a
- **Reset/Clear Screen**: Press the **`C`** to clear the screen and reset turtle
- **Exit the Application**: Press the **`X`** key to close the application.

## Getting Started
### Prerequisites
- Python 3.7 or higher must be installed on your machine.
- The `turtle` library is included in the Python standard library and does not require additional installation.

### Installation
1. Clone or download the repository.
2. Ensure that `main.py` is present in the project directory.

## Usage
1. Run the following command in your terminal or IDE to start the application:
``` bash
    python main.py
```
1. Use the following keys to control the turtle:
    - **W**: Move Forward
    - **A**: Turn Left
    - **D**: Turn Right
    - **S**: Move Backward
    - **C**: Clear Screen, Reset Turtle
    - **X**: Exit the application

2. The turtle will respond to the specified key presses and perform the corresponding movements or actions.

## How It Works
- The application listens for keypress events using the `screen.listen()` function provided by the `turtle` library.
- Specific keys (`w`, `a`, `s`, `d`, `c`, `x`) are mapped to functions (`move_forward`, `turn_left`, `turn_right`, `move_backward`, `reset/clear screen`, `exit`), which are invoked when the keys are pressed.
- The turtle's movements are updated in real time on the screen, offering an interactive graphical experience.

## Example Screenshot
_(Add a screenshot if applicable)_
## Exit the Program
To exit the application:
- Press the **`C`** key to close the program gracefully, or
- Simply click anywhere on the turtle graphics screen using your mouse.

## License
This project is open source and available for modification or use in other projects.
Feel free to suggest improvements or report any issues via the repository! 🚀 Happy coding!

