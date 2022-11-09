from turtle import *

color('pink')

speed(45)
hideturtle()

def curve():
    for i in range(200):
        right(1)
        forward(1)
begin_fill()

left(140)
forward(113)

curve()
left(120)

curve()

forward(112)
end_fill

up()
setpos(-50, 95)
down()
color('yellow')
write('Thảo ngu', font=('arial', 13, 'bold'))

done()
