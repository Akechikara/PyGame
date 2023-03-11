import turtle
tao = turtle.Pen()
tao.shape('turtle')

# for i in range(4):
#    tao.forward(1000)
#    tao.left(90)

def rect():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

# rect()

tao.penup()
tao.goto(200,200)
rect()
tao.pendown()
rect()
def walk(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

walk(200,-200)
rect()
walk(-200,200)
rect()
walk(-200,-200)
rect
walk(0,0)
tao.circle(100)


