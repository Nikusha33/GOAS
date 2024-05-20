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
forward(70)
right(39)
forward(32)
left(90)
forward(21)
left(90)
forward(21)
right(140)
forward(35)
left(88)
forward(147)

end_fill()

#აქ დავიწყე ფანჯრების კეთება N1
penup()
goto(0, 200)
pendown()
color("red")
left(50)
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
left(91)
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
#სახურავი N2
penup()
goto(0, 0)
pendown()
left(180)
color("red")
forward(250)
right(90)
forward(200)
right(90)
forward(250)
left(180)
forward(250)
begin_fill()
color("purple")
right(120)
forward(108)
right(60)
forward(305)
right(140)
forward(145)
right(40)
forward(250)
end_fill()

#ფანჯარა N3
color("red")
left(90)
forward(80)
left(90)
color("brown")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
#ფანჯარა N4
penup()
goto(0, 70)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
right(90)
color("red")
forward(120)
left(90)
forward(200)
exitonclick()