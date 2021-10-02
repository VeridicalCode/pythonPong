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
pongWindow.setup(width=800, height=600)
pongWindow.tracer(False) # 'tracing' shows the turtle's movement; if false, screen will never update by itself
pongWindow.colormode(255) # so we can screw around with paddle colors
pongWindow.listen() # listen for keypress


# ====== OBJECTS =======

# left paddle
paddleL = turtle.Turtle() # every screen element is a new specific object of the Turtle() class
paddleL.speed(0) # update speed set to max
paddleL.shape("square")
paddleL.shapesize(stretch_wid=5, stretch_len=1) # counterintuitively, this makes it 5x taller, since default facing is ->
paddleL.color("white")
paddleL.penup() # don't draw, just move
paddleL.goto(-350, 0) #start location

# right paddle
paddleR = turtle.Turtle()
paddleR.speed(0)
paddleR.shape("square")
paddleR.shapesize(stretch_wid=5, stretch_len=1)
paddleR.color("white")
paddleR.penup()
paddleR.goto(350, 0) # 0,0 is center of screen

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle") # it's pyPong with turtle, the ball's gotta be a turtle
ball.color(40, 135, 15) # turtles are green!
ball.tilt(90) # turtle facing up
ball.penup()
ball.goto(0,0) # unnecessary, but we are thorough here
ball.dx = 0.1  # "speed" is update speed, delta[coordinate] is actual movement speed (in pixels)
ball.dy = 0.1  # an appropriate number will depend on processing power, so adjust this until ball movement is comfortable
          # TODO: we could add a "difficulty" prompt at game launch that sets ball speed

# ====== FUNCTIONS =======

# left paddle up
def paddleL_up():
  y = paddleL.ycor()  # get current position
  y += 20             # can be adjusted to alter movement speed
  paddleL.sety(y)

# left paddle down
def paddleL_down():
  y = paddleL.ycor()
  y -= 20
  paddleL.sety(y)

# right paddle up
def paddleR_up():
  y = paddleR.ycor()
  y += 20
  paddleR.sety(y)

# right paddle down
def paddleR_down():
  y = paddleR.ycor()
  y -= 20
  paddleR.sety(y)

# ====== KEYBINDS =======

# left side
pongWindow.onkeypress(paddleL_up, "w")
pongWindow.onkeypress(paddleL_down, "s")
# right side
pongWindow.onkeypress(paddleR_up, "Up")
pongWindow.onkeypress(paddleR_down, "Down")
# note both sides won't be able to move at the same time

# ====== CORE GAME LOOP =======

while True:
  pongWindow.update() # we set tracer false so we do manual updates

  # ball movement
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # border collision
  if ball.ycor() > 290:
    ball.sety(290) # safety check
    ball.dy *= -1 # reverse movement
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  # point checking. currently there's no score tracking, but we're not using an OR in case we want to add it
  if ball.xcor() > 360: # point to left player
    ball.setx(0)
    ball.sety(0)
  if ball.xcor() < -360: # point to right player
    ball.setx(0)
    ball.sety(0)