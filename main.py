import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function,
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(dart):
  dart.up()
  dart.goto(-360, 0)
  dart.down()
  for i in range(-360, 360):
    y = math.sin(math.radians(i))
    dart.goto(i, y)
  
def setupWindow(wn = None):
  wn.bgcolor("lightgreen")
  wn.setworldcoordinates(-360, -3, 361, 3)
  
def setupAxis(dart = None):
  dart.goto(-360, 0)
  dart.goto(361, 0)
  dart.up()
  dart.goto(0, 3)
  dart.down()
  dart.goto(0, -3)

def setupAxisForShape(dart = None):
  dart.goto(-360, 0)
  dart.goto(361, 0)
  dart.up()
  dart.goto(0, 361)
  dart.down()
  dart.goto(0, -360)
  
def drawCosineCurve(dart = None):
  dart.up()
  dart.goto(-360, 1)
  dart.down()
  for i in range(-360, 361):
    y = math.cos(math.radians(i)) 
    dart.goto(i, y) 
  
def drawTangentCurve(dart = None):
  dart.up()
  dart.goto(-360, 0)
  dart.down()
  for i in range(-360, 361):
    y = math.tan(math.radians(i)) 
    dart.goto(i, y)

def drawSecantCurve(dart = None):
  dart.up()
  dart.goto(-360, 1)
  dart.down()
  for i in range(-360, 361):
    y = math.cos(math.radians(i))
    sec = (1 / y)
    dart.goto(i, sec)

def drawBigShape(dart = None, wn = None, sides = 0, length = 0, color = None, perimeterB = 0):
  dart.clear()
  wn.setworldcoordinates(-360, -360, 361, 361)
  setupAxisForShape(dart)
  dart.up()
  dart.goto(0, 0)
  dart.color(color)
  dart.down()
  for i in range(sides):
    dart.stamp()
    dart.forward(length)
    dart.left(360 / sides)
  dart.color("black")
  perimeterB = sides * length
  return perimeterB
  
def drawLittleShape(dart = None, wn = None, sides = 0, length = 0, color = None, perimeterL = 0):
  wn.setworldcoordinates(-360, -360, 361, 361)
  setupAxisForShape(dart)
  dart.up()
  dart.goto(100, 100)
  dart.color(color)
  dart.down()
  for i in range(sides):
    dart.stamp()
    dart.forward(length)
    dart.left(360 / sides)
  perimeterL = sides * length
  return perimeterL
  
##########  Do Not Alter Any Code Past Here ########
  
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    drawSecantCurve(dart)
  
    sides = int(input("\nHow many sides do you want your big shape to have? "))
    length = int(input("\nChoose a side length greater than 200: "))
    if length <= 200:
      exit()
    color = input("\nWhat color do you want your big shape to be? ")
    perimeterB = drawBigShape(dart, wn, sides, length, color)
    print("\nThe perimeter of your big shape is", perimeterB)
  
    sides = int(input("\nHow many sides do you want your little shape to have? "))
    length = int(input("\nChoose a side length less than 150: "))
    if length >= 150:
      exit()
    color = input("\nWhat color do you want your little shape to be? ")
    perimeterL = drawLittleShape(dart, wn, sides, length, color)
    print("\nThe perimeter of your little shape is", perimeterL)
  
    factor = perimeterB / perimeterL
    print("\nThe perimeter of the big shape is", factor, "times greater than the perimeter of the little shape! ")
    wn.exitonclick()

main()