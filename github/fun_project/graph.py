import turtle
Cppsecrets=turtle.Screen()
turtle.screensize(1200,1200)
trtl=turtle.Turtle()
trtl.speed(10)
for i in range(0,400,20):
  trtl.pencolor('green')
  trtl.penup()
  trtl.setpos(-200+i,-200)
  if i==0:
    trtl.left(90)
  trtl.pendown()
  trtl.forward(400)
  trtl.backward(400)
for i in range(0,400,20):
  trtl.pencolor('red')
  trtl.penup()
  trtl.setpos(-200,-200+i)
  if i==0:
    trtl.right(90)
  trtl.pendown()
  trtl.forward(400)
  trtl.backward(400) 
trtl.penup()
trtl.home()
trtl.pendown()
trtl.pencolor('Blue')
trtl.backward(200)
trtl.forward(400)
trtl.backward(200)
trtl.left(90)
trtl.forward(200)
trtl.backward(400)
trtl.penup()
trtl.setpos(5,5)
trtl.pendown()
trtl.write(0)
trtl.penup()
trtl.setpos(190,5)
trtl.pendown()
trtl.write("x")
trtl.penup()
trtl.setpos(5,190)
trtl.pendown()
trtl.write("y")
trtl.penup()
trtl.setpos(80,-180)
trtl.pendown()
trtl.write("Bridgelabz Solutions")
trtl.ht()