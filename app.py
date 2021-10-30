# super simple pong game to demo basic GUI programming and turtle
# by VeridicalQ

# call the built-in canvas library and the built-in RNG
import turtle
import random

# variables for tracking player scores, ball speed
score_L = 0
score_R = 0
ball_delta = 0.1

# ====== OBJECTS =======
# the window itself, first: create a canvas and give it some basic paramaters
pong_Window = turtle.Screen()
pong_Window.title("Pong by VeridicalQ")
pong_Window.bgcolor("black")
pong_Window.setup(width=800, height=600)
pong_Window.tracer(False) # 'tracing' shows the turtle's movement; if false, screen will never update by itself
pong_Window.colormode(255) # so we can make the turtle green
pong_Window.listen() # listen for keypress


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

# score
score_text = turtle.Turtle()
score_text.speed(0)
score_text.color("white")
score_text.penup() # still need to do this even with a stationary obj because every turtle starts at 0,0
score_text.hideturtle() # we don't want to see it, just what it types
score_text.goto(0, 260)
score_text.write("Player 1: {}    Player 2: {}".format(score_L, score_R), align="center", font=("Courier", 24, "normal"))

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

  # ball border collision
  if ball.ycor() > 290:
    ball.sety(290) # safety check
    ball.dy *= -1 # reverse movement
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  # paddle border collision
  if paddle_R.ycor() > 290:
    paddle_R.sety(285) # just push it down a little
  if paddle_R.ycor() < -290:
    paddle_R.sety(-285)
  if paddle_L.ycor() > 290:
    paddle_L.sety(285) # just push it down a little
  if paddle_L.ycor() < -290:
    paddle_L.sety(-285)

  # point checking
  # off right side, point to left player (1)
  if ball.xcor() > 390:
    ball.goto(0,0)
    ball.dx *= randomize_aim()
    ball.dy *= randomize_aim()
    score_L += 1
    score_text.clear()
    score_text.write("Player 1: {}    Player 2: {}".format(score_L, score_R), align="center", font=("Courier", 24, "normal"))

  # off left side, point to right player (2)
  if ball.xcor() < -390:
    ball.goto(0,0)
    ball.dx *= randomize_aim()
    ball.dy *= randomize_aim()
    score_R += 1
    score_text.clear()
    score_text.write("Player 1: {}    Player 2: {}".format(score_L, score_R), align="center", font=("Courier", 24, "normal"))

  # paddle collision checking. paddles are 10 pixels wide and 50 pixels tall
  # hit right side paddle
  if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() <= paddle_R.ycor() + 40 and ball.ycor() >= paddle_R.ycor() -40:
    ball.setx(340) # we check for < 350 and push ball left to avoid weird behavior between paddle and edge
    ball.dx *= -1
  # hit left side paddle
  if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() <= paddle_L.ycor() + 40 and ball.ycor() >= paddle_L.ycor() -40:
    ball.setx(-340)
    ball.dx *= -1