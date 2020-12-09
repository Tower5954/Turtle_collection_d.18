import turtle as t
from turtle import Screen
import heroes
import random

turtle_name = heroes.gen()
leo = t.Turtle()
leo.shape("turtle")
leo.color("dark green")

colour = ["blue", "light sea green", "lime green", "dark green", "lime", "yellow", "orange red", "red", "hot pink", "deep pink", "purple"]

def create_shape(num_sides):
    """ A function to keep creating shapes with a turtle"""
    angle = 360/ num_sides
    for _ in range(num_sides):
        leo.forward(100)
        leo.right(angle)

for shape_side_n in range(3, 11):
    leo.color(random.choice(colour))
    create_shape(shape_side_n)















screen = Screen()
screen.exitonclick()

