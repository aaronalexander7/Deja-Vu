from turtle import *
import os

screen = Screen()
screen.setup(width=.75, height=.75)# Setup screen
screen.bgcolor("teal")

car1 = Turtle()
car1.speed(0)
car1.shapesize(1.5)
car2 = Turtle()
car2.speed(0)
car2.shapesize(1.5)
writer = Turtle()

car1.penup()
car2.penup()
car1.setposition(-550, -550)
car2.setposition(-530, -550)
car1.color("blue")
car1.pencolor("red")
car2.color("green")
car2.pencolor("purple")

SPEED = 1
writer.speed(SPEED)
writer.shape("classic")
writer.shapesize(1.5, 1.5)
writer.color("pink")
writer.pencolor("yellow")
writer.pensize(2)

def write_deja_vu():
    writer.penup()
    writer.lt(135)
    writer.setpos(-200, 120)

    #D
    writer.lt(125)
    writer.pendown()
    writer.fd(120)
    writer.penup()
    writer.setposition(writer.xcor() - 20, writer.ycor() - 20)
    writer.lt(105)
    writer.pendown()
    writer.tilt(90) #Drift
    writer.circle(100, 180)
    writer.penup()
    writer.circle(100, 180)
    writer.fd(80)

    #e
    writer.pendown()
    writer.fd(30)
    writer.tilt(75)
    writer.lt(75)
    writer.circle(25, 300)
    writer.penup()
    writer.lt(30)
    writer.fd(60)

    #j
    writer.pendown()
    writer.tilt(180)
    writer.lt(200)
    writer.fd(80)
    writer.circle(-50, 45)
    writer.penup()
    writer.circle(-40, 190)
    writer.fd(100)

    #a
    writer.pendown()
    writer.fd(30)
    writer.tilt(50)
    writer.circle(-10, 125)
    writer.fd(60)
    writer.penup()
    writer.lt(105)
    writer.circle(25, 180)
    writer.pendown()
    writer.fd(10)
    writer.circle(25, 180)
    writer.fd(10)
    writer.penup()
    writer.fd(80)
    writer.lt(75)

    #V
    writer.pendown()
    writer.fd(200)
    writer.penup()
    writer.lt(30)
    writer.circle(50,180)
    writer.pendown()
    writer.fd(175)
    writer.penup()
    writer.lt(90)
    writer.tilt(-15)
    writer.fd(25)

    #u
    writer.lt(60)
    writer.fd(70)
    writer.circle(-20, 180)
    writer.tilt(-50)
    writer.pendown()
    writer.fd(40)
    writer.circle(-20, 180)
    writer.fd(40)
    writer.penup()

    #Drifteez
    writer.fd(200)
    writer.circle(-100, 300)
    writer.fd(200)
    writer.tilt(50)
    writer.circle(100, 240)
    writer.fd(200)
    writer.tilt(-50)
    writer.circle(-180, 250)
    writer.fd(240)
    writer.pendown()
    writer.fd(10)
    writer.penup()
    writer.fd(500)

def drifting_cars():
    car1.lt(45)
    car2.lt(45)
    car1.speed(13)
    car2.speed(13)
    car1.pendown()
    car2.pendown()

    #Racers' enterance
    for i in range(100):
        car1.fd(10)
        car2.fd(10)

    # drift loop
    car1.tilt(-50)
    car2.tilt(-50)

    for i in range(25):
        car1.circle(-150, 10)
        car2.circle(-150, 10)

    car1.tilt(50)
    car2.tilt(50)

    for i in range(50):
        car1.fd(10)
        car2.fd(10)

    car1.tilt(50)
    car2.tilt(50)

    for i in range(25):
        car1.circle(150, 10)
        car2.circle(150, 10)

    car1.tilt(-50)
    car2.tilt(-50)

    for i in range(20):
        car1.fd(10)
        car2.fd(10)

    car1.tilt(-50)
    car2.tilt(-50)
    x = 0
    while True:
        car1.circle(-(10 + x), 10)
        car2.circle(-(10 + x), 10)
        x += 1

def main():
    os.system("start " + os.path.dirname(os.path.realpath(__file__)) + "\dejavu.wav")
    write_deja_vu()
    drifting_cars()

    screen.exitonclick()

main()