"""
A simple Turtle Race Game:

This Python script simulates a turtle race game using the Turtle module. It allows the user to place bets on which
turtle will win the race. Six turtles of different colors participate in the race, and they move forward randomly until
one of them crosses the finish line. The user is notified whether they won or lost their bet based on the winning
turtle's color.

Instructions:
- Run the script and follow the prompt to place your bet on a turtle.
- Watch the turtles race!
- The program will print whether you won or lost the bet.
"""

from turtle import Turtle, Screen
import random

# Variable to control if the race is on or not
is_race_on = False

# Create a screen object
screen = Screen()
screen.setup(width=500, height=400)

# Ask user to make a bet on the winning turtle, ever in lower case
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (red - "
                                                          "orange  - yellow - green - blue - purple)").lower()

# List of turtle colors
color = ["red", "orange", "yellow", "green", "blue", "purple"]

# List of y positions for the start turtles positions
y_positions = [-75, -45, -15, 15, 45, 75]

# List to hold all the turtle objects
all_turtle = []

# Create six turtles, set their color and initial position, and add them to the list
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

# If the user has made a bet, start the race
if user_bet:
    is_race_on = True

# While the race is on, move each turtle forward randomly
while is_race_on:

    # Loop through each turtle to move them forward
    for turtle in all_turtle:

        # Check if the turtle has crossed the finish line
        if turtle.xcor() > 230:

            # If a turtle crosses the finish line, end the race
            is_race_on = False

            # Get the color of the winning turtle
            winning_color = turtle.pencolor()

            # Check if the user's bet matches the winning turtle's color and print the result
            if winning_color == user_bet:

                # If the user won the bet, display a victory message on the screen
                screen.textinput("Race Result", f"You've won! The {winning_color} turtle is the winner! "
                                                f"Press OK to exit.")
            else:
                # If the user lost the bet, display a defeat message on the screen
                screen.textinput("Race Result", f"You've lost! The {winning_color} turtle is the winner! "
                                                f"Press OK to exit.")

            # Close the graphics window after the user views the result
            screen.bye()

            # Exit the loop once a turtle wins
            break

        # Move the turtle forward by a random distance
        rand_distance = random.randint(0, 10)

        # Move the turtle forward by the generated random distance
        turtle.forward(rand_distance)
