from turtle import *
speed(1)
color('red','yellow')
begin_fill()
while True:
    forward(220)
    left(190)
    if abs(pos())<1:
        break
end_fill()
done()
