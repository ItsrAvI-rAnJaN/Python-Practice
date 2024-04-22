import turtle
Cppsecrets=turtle.Screen()
turtle.screensize(1200,1200)
vivax=turtle.Turtle()
def Multiple_Squares(length, colour):
  vivax.pencolor(colour)
  vivax.pensize(4)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.setheading(360)
  vivax.ht()
for i in range(50,110,10):
  Multiple_Squares(i,"red")