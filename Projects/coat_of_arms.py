# Section 1 - Your code
from utils import *
set_background("pc")

s1 = create_sprite("soccerball", 100, 100)
s2 = create_sprite("bike", -100, 100)
s3 = create_sprite("cool_dog", -100, -100)
s4 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-50,200)
message1.color("red")
message1.write("Kai",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-300,-225)
message2.color("red")
message2.write("To achieve great things, two things are needed,",font = ("Arial", 20, "normal"))
message2.hideturtle()

message3 = create_sprite("alien",-300,-250)
message3.color("red")
message3.write("a plan, and not quite enough time",font = ("Arial", 20, "normal"))
message3.hideturtle()

######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()