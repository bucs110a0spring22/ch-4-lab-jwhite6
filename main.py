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
  for i in range(-360, 361):
    y = math.sin(math.radians(i)) 
    dart.goto(i, y)

def setupWindow(wn = None):
  wn.bgcolor("lightgreen")
  wn.setworldcoordinates(-360, -1, 361, 1)
  
def setupAxis(dart = None):
  dart.goto(-360, 0)
  dart.goto(360, 0)
  dart.up()
  dart.goto(0, 1)
  dart.down()
  dart.goto(0, -1)
  
def drawCosineCurve(dart = None):
  dart.up()
  dart.goto(-360, 0)
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
    wn.exitonclick()

main()