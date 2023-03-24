import turtle
screen = turtle.Screen()
pen = turtle.Turtle()

colors = ['red', 'purple', 'blue','indigo','green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('Black')

for x in range(360):

    pen.speed(x+1)
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(89)

pen.pensize(8)
pen.forward(25)
pen.right(180)
pen.forward(50)
pen.left(75)
pen.forward(100)
pen.right(75)
pen.forward(35)
pen.right(105)
pen.forward(250)
pen.right(75)
pen.forward(50)
pen.right(75)
pen.forward(250)
pen.right(105)
pen.forward(35)
pen.right(75)
pen.forward(100)
pen.left(75)
pen.forward(50)


pen.up()
pen.goto(-25,10)
pen.begin_fill()
pen.down()
pen.right(105)
pen.forward(100)
pen.right(150)
pen.forward(100)
pen.right(105)
pen.forward(50)



pen.hideturtle()


screen.mainloop()
