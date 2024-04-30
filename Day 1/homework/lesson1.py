from turtle import *

 #აქ დავიწყე კედლების კეთება

speed(30)

width(6)
color ("red")

forward(200)

left(90)

forward(200)

left(90)

forward(200)

left(90)

forward(200)

left(90) 

forward(75)

#აქ დავიწყე კარების კეთება

color("pink")
begin_fill()
left(90)

forward(100)

right(90)

forward(55)

right(90)

forward(100)
end_fill()
#აქ დავიწყე სახურავის კეთება
color("purple")
penup()
goto(200, 200)
pendown()

begin_fill()
right(140)
forward(150)
left(97)
forward(152)
end_fill()
#აქ დავიწყე ფანჯრების კეთება N1
color("red")
left(43)
forward(79)
left(90)
begin_fill()
color("brown")
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()

#აქ დავიწყე ფანჯრების კეთება N2

color("red")

penup()
goto(200, 200)
pendown()
left(90)
forward(79)
right(90)
color("brown")
begin_fill()
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

exitonclick()