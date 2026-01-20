import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -225
y1 = 150
x2 = -225
y2 = 50
x3 = -225
y3 = -50
x4 = -225
y4 = -150


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("underwater")
t1 = create_sprite("fish",x1,y1)
t2 = create_sprite("cardinal",x2,y2)
t3 = create_sprite("pineapple",x3,y3)
# The dog is hypothetically faster, because it could roll a higher value with potential to move faster, but is still random.
t4 = create_sprite("cool_dog",x4,y4)
winmessage = create_sprite("alien", -50, 0)
winmessage.color("black")
winmessage.hideturtle()

# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(160):
    x1 += random.randint(0,5)
    x2 += random.randint(0,5)
    x3 += random.randint(0,5)
    x4 += random.randint(0,6)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    
    window.update()
    time.sleep(0.08)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Fish wins!")

elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("Cardinal wins!")

elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("Pineapple wins!")

elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    print("Dog wins!")

turtle.exitonclick()