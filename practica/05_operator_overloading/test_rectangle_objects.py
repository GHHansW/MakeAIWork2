#!/usr/bin/env python

from rectangle_objects import Rectangle, Box, Triangle

rectangle = Rectangle(4, 5)
# area = rectangle.getArea()
print(f"The color of rectangle is {rectangle.getColor()}")
print(f"The area of the rectangle is : {rectangle.getArea()}")

# rectangleForStephan = Rectangle(10, 12, "red")
# print(f"The color of rectangle for Stephan is {rectangleForStephan.getColor()}")

box = Box(4, 4, 2)
area = box.getArea()
depth = box.getDepth()
print(f"The area of the box is : {area}")
print(f"The depth of the box is : {depth}")

triangle = Triangle(4, 4)
area = triangle.getArea()
base = triangle.getBase()
print(f"The area of the triangle is : {area}")
print(f"The base of the triangle is : {base}")