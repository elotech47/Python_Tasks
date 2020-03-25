"""This program taks radius of a circle as input and computes then outputs the Area"""
import math
print("This is a basic calculator that computes the area of a circle given it's radius")

r = input("Please input the radius of the circle:...")
PI = math.pi
Area = PI * int(r) * int(r)

print("Area of the circle of radius " + str(r) + " is " + str(Area))