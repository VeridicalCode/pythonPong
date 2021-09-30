# super simple pong game to demo basic GUI programming and turtle
# by VeridicalQ

# call the built-in canvas library
# this thing used to just be a little turtle guy that ran around the screen leaving a line behind
# you steered it with math
# plus ça change eh?
import turtle

# create a canvas and give it some basic paramaters
pongWindow = turtle.Screen()
pongWindow.title("Pong by VeridicalQ")
pongWindow.bgcolor("black")
pongWindow.setup(width=800, height=600) # coordinate-based; center will be 0,0, goes to +/-400, 300
pongWindow.tracer(False) # 'tracing' shows the turtle's movement; if false, screen will never update by itself

# left paddle
paddleL = turtle.Turtle() # every screen element is a new specific object of the Turtle() class
paddleL.speed(0) # update speed set to max
paddleL.shape("square")
paddleL.color("white")
paddleL.penup() # don't draw, just move
paddleL.goto(-350, 0) #start location

# right paddle
paddleR = turtle.Turtle()

# ball


# core game loop to put it all together
while True:
  pongWindow.update() # we set tracer false so we do manual updates
