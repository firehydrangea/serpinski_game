"""
Sarah Kudrick 4/2/23
inspired by this tiktok:
https://www.tiktok.com/t/ZTRcSEoCC/
draw the three corners of an eqilateral triangle.
draw a point randomly inside the triangle.
pick one of the three corners at random.
draw a point at the midpoint of those two points.
pick a corner randomly
draw a point at the midpoint of the last midpoint and the corner you chose
repeat
for tips to customize the drawing, look at comments throughout program.
"""

import turtle
import math
import random

t = turtle.Turtle()
t.speed(0)
t.penup()

#halfht represents half the height of the eqilateral triangle.
#it is set to 150 so the drawing fits nicely in the center of the canvas
#you can change it to make the drawing bigger or smaller.
halfht = 150
#pts represents the three corners of the triangle.
pts = [[0, halfht],[(float)(-2*halfht/math.sqrt(3)), -150],[(float)(2*halfht/math.sqrt(3)), -150]]
#equation timeeeeee
#-150 < y < 150
#-150 < y < (math.sqrt(3) * math.fabs(x) ) + 150
#(y-150)/math.sqrt(3) < x < (150-y)/math.sqrt(3)
print("The side length of the triangle is "+str((4*halfht)/math.sqrt(3)))
print("The center of the triangle is at (0,0)")
print("These are the three corners:")
for point in pts:
  print(point)
  t.goto(point)
  t.dot()

y = random.uniform(-halfht, halfht)
x = random.uniform((y-halfht)/math.sqrt(3), (halfht-y)/math.sqrt(3))
#innerPt represents the first dot that will be drawn.
#it is set to a random point inside of the triangle, so
#a few points might be in the whitespaces of the fractal.
#to avoid this, replace the line of code below with: innerPt = [0.0, 0.0]
innerPt = [x, y]
print("This is the first point generated:")
print(innerPt)

t.goto(innerPt)
t.dot()
#below is the repeating part of the fractal.
#to make it repeat less or more times, change the number 5000 to a larger or smaller number.
for i in range(5000):
  corner=random.randint(0,2)
  innerPt = [(float)(innerPt[0]+pts[corner][0])/2.0,(float)(innerPt[1]+pts[corner][1])/2.0]
  t.goto(innerPt)
  t.dot()

#notes:
#might need to consider using a noninclusive range for starting point generation.
#  this can be done with random.random*that calculation