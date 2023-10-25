from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Turtle Hunt")

attacker = Turtle()
attacker.shape("turtle")
attacker.color("blue")
attacker.right(45)
attacker.penup()
attacker.setposition(-240,240)

defender = Turtle("turtle")
defender.color("red")
defender.left(135)
defender.penup()
defender.setposition(240, -240)

segment_1 = Turtle("square")
segment_1.color("white")
segment_1.penup()
segment_1.setposition(280,-280)

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.penup()
segment_2.setposition(280,-260)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.penup()
segment_3.setposition(260,-280)

segment_4 = Turtle("square")
segment_4.color("white")
segment_4.penup()
segment_4.setposition(260,-260)

segment_5 = Turtle("square")
segment_5.color("white")
segment_5.penup()
segment_5.setposition(280,-240)

segment_6 = Turtle("square")
segment_6.color("white")
segment_6.penup()
segment_6.setposition(240,-280)

pen = Turtle()
pen.color("white")

def go_up():
    y = attacker.ycor() + 15
    attacker.goto(attacker.xcor(), y)

def go_down():
    y = attacker.ycor() - 15
    attacker.goto(attacker.xcor(), y)

def go_right():
    x = attacker.xcor() + 15
    attacker.goto(x, attacker.ycor())

def go_left():
    x = attacker.xcor() - 15
    attacker.goto(x, attacker.ycor())

def go_up_follow():
    y = defender.ycor() + 10
    defender.goto(defender.xcor(), y)

def go_down_follow():
    y = defender.ycor() - 10
    defender.goto(defender.xcor(), y)

def go_right_follow():
    x = defender.xcor() + 10
    defender.goto(x, defender.ycor())

def go_left_follow():
    x = defender.xcor() - 10
    defender.goto(x, defender.ycor())

screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_right, "d")
screen.onkey(go_left, "a")
screen.onkey(go_up_follow, "Up")
screen.onkey(go_down_follow, "Down")
screen.onkey(go_right_follow, "Right")
screen.onkey(go_left_follow, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    
    if attacker.xcor() > 290 or attacker.xcor() < -290 or attacker.ycor() > 290 or attacker.ycor() < -290:
        game_is_on = False
        pen.goto(0, 0)
        pen.write("Game Over: Defender Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(defender) < 20:
        game_is_on = False
        pen.write("Game Over: Defender Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(segment_1) < 10:
        game_is_on = False
        pen.write("Game Over: Attacker Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(segment_2) < 10:
        game_is_on = False
        pen.write("Game Over: Attacker Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(segment_3) < 10:
        game_is_on = False
        pen.write("Game Over: Attacker Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(segment_4) < 10:
        game_is_on = False
        pen.write("Game Over: Attacker Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(segment_5) < 10:
        game_is_on = False
        pen.write("Game Over: Attacker Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

    if attacker.distance(segment_6) < 10:
        game_is_on = False
        pen.write("Game Over: Attacker Wins", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        screen.bye()

screen.mainloop()

