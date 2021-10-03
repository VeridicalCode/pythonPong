# super simple pong game to demo basic GUI programming and turtle
# by VeridicalQ

# call the built-in canvas library and the built-in RNG
import turtle
import random

# create a canvas and give it some basic paramaters
pong_Window = turtle.Screen()
pong_Window.title("Pong by VeridicalQ")
pong_Window.bgcolor("black")
pong_Window.setup(width=800, height=600)
pong_Window.tracer(False) # 'tracing' shows the turtle's movement; if false, screen will never update by itself
pong_Window.colormode(255) # so we can make the turtle green
pong_Window.listen() # listen for keypress

# ====== OBJECTS =======

# left paddle
paddle_L = turtle.Turtle() # every screen element is a new specific object of the Turtle() class
paddle_L.speed(0) # update speed set to max
paddle_L.shape("square")
paddle_L.shapesize(stretch_wid=5, stretch_len=1) # counterintuitively, this makes it 5x taller, since default facing is ->
paddle_L.color("white")
paddle_L.penup() # don't draw, just move
paddle_L.goto(-350, 0) #start location

# right paddle
paddle_R = turtle.Turtle()
paddle_R.speed(0)
paddle_R.shape("square")
paddle_R.shapesize(stretch_wid=5, stretch_len=1)
paddle_R.color("white")
paddle_R.penup()
paddle_R.goto(350, 0) # 0,0 is center of screen

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle") # it's pyPong with turtle, the ball's gotta be a turtle
ball.color(40, 135, 15) # turtles are green!
ball.tilt(90) # turtle facing up
ball.penup()
ball.goto(0,0) # safety check
ball.dx = 0.1  # "speed" is update speed, delta[coordinate] is actual movement speed (in pixels)
ball.dy = 0.1  # an appropriate number will depend on processing power, so adjust this until ball movement is comfortable
          # TODO: we could add a "difficulty" prompt at game launch that sets ball speed

# ====== FUNCTIONS =======

# left paddle up
def paddle_L_up():
  y = paddle_L.ycor()  # get current position
  y += 20             # can be adjusted to alter movement speed
  paddle_L.sety(y)

# left paddle down
def paddle_L_down():
  y = paddle_L.ycor()
  y -= 20
  paddle_L.sety(y)

# right paddle up
def paddle_R_up():
  y = paddle_R.ycor()
  y += 20
  paddle_R.sety(y)

# right paddle down
def paddle_R_down():
  y = paddle_R.ycor()
  y -= 20
  paddle_R.sety(y)

# randomize ball travel direction
def randomize_aim():
  if random.randint(0, 1) == 0:
    return 1
  else:
    return -1

# ====== KEYBINDS =======

# left side
pong_Window.onkeypress(paddle_L_up, "w")
pong_Window.onkeypress(paddle_L_down, "s")
# right side
pong_Window.onkeypress(paddle_R_up, "Up")
pong_Window.onkeypress(paddle_R_down, "Down")
# note both sides won't be able to move at the same time

# ====== CORE GAME LOOP =======

while True:
  pong_Window.update() # we set tracer false so we do manual updates

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
  # off right side, point to left player
  if ball.xcor() > 360:
    ball.goto(0,0)
    ball.dx *= randomize_aim()
    ball.dy *= randomize_aim()
    print(ball.dx, ball.dy)
  # off left side, point to right player
  if ball.xcor() < -360:
    ball.goto(0,0)
    ball.dx *= randomize_aim()
    ball.dy *= randomize_aim()
    print(ball.dx, ball.dy)