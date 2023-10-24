import turtle
import random
tur1 = turtle.Turtle()
tur1.penup()
tur1.setpos(-400,-350)
tur1.seth(90)
tur1.color('red')
speed1 = (random.randint(1,35))
speed1 /= 50
print(speed1)
#turtle 2
tur2 = turtle.Turtle()
tur2.penup()
tur2.setpos(-300,-350)
tur2.seth(90)
tur2.color('blue')
speed2 = (random.randint(1,35))
speed2 /= 10
print(speed2)
#turtle 3
tur3 = turtle.Turtle()
tur3.penup()
tur3.setpos(-200,-350)
tur3.seth(90)
tur3.color('green')
speed3 = (random.randint(1,35))
speed3 /= 10
print(speed3)
#turtle 4
tur4 = turtle.Turtle()
tur4.penup()
tur4.setpos(-100,-350)
tur4.seth(90)
tur4.color('turquoise')
speed4 = (random.randint(1,35))
speed4 /= 10
print(speed4)
#turtle 5
tur5 = turtle.Turtle()
tur5.penup()
tur5.setpos(0,-350)
tur5.seth(90)
tur5.color('purple')
speed5 = (random.randint(1,35))
speed5 /= 10
print(speed5)
#turtle 6
tur6 = turtle.Turtle()
tur6.penup()
tur6.setpos(100,-350)
tur6.seth(90)
tur6.color('orange')
speed6 = (random.randint(1,35))
speed6 /= 10
print(speed6)
#turtle 7
tur7 = turtle.Turtle()
tur7.penup()
tur7.setpos(200,-350)
tur7.seth(90)
tur7.color('crimson')
speed7 = (random.randint(1,35))
speed7 /= 10
print(speed7)
#turtle 8
tur8 = turtle.Turtle()
tur8.penup()
tur8.setpos(300,-350)
tur8.seth(90)
tur8.color('steel blue')
speed8 = (random.randint(1,35))
speed8 /= 10
print(speed8)
#turtle 9
tur9 = turtle.Turtle()
tur9.penup()
tur9.setpos(400,-350)
tur9.seth(90)
tur9.color('tomato')
speed9 = (random.randint(1,35))
speed9 /= 10
print(speed9)
#type turtle
turtleWrite = turtle.Turtle()
turtleWrite.penup()
turtleWrite.hideturtle()
turtleWrite.setpos(-425,380)
turtleWrite.write("|Turtle 1 Speed: " + str(speed1) + " |Turtle 2 Speed: " + str(speed2) + " |Turtle 3 Speed: " + str(speed3) + " |Turtle 4 Speed: " + str(speed4) + " |Turtle 5 Speed: " + str(speed5) + " |Turtle 6 Speed: " + str(speed6) + " |Turtle 7 Speed: " + str(speed7) + " |Turtle 8 Speed: " + str(speed8) + " |Turtle 9 Speed: " + str(speed9))
while True:
    print(speed2)
    tur2.pendown()
    tur2.forward(speed2)
    print(speed1)
    tur1.pendown()
    tur1.forward(speed1)
    print(speed3)
    tur3.pendown()
    tur3.forward(speed3)
    print(speed4)
    tur4.pendown()
    tur4.forward(speed4)
    print(speed5)
    tur5.pendown()
    tur5.forward(speed5)
    print(speed6)
    tur6.pendown()
    tur6.forward(speed6)

    print(speed7)
    tur7.pendown()
    tur7.forward(speed7)

    print(speed8)
    tur8.pendown()
    tur8.forward(speed8)

    print(speed9)
    tur9.pendown()
    tur9.forward(speed9)
