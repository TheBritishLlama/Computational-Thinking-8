import turtle, time, random, math
from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("capybara_sunset")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
# Source - https://stackoverflow.com/a/45439266
# Posted by skrx, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-29, License - CC BY-SA 3.0
crypto = 0
computers = 0
ferraris = 0
cost = 10
message_sprite = create_sprite("alien",-350,150)
message_sprite.color("white")

# Section 2 - controls
# TODO - define an action. ex: def my_control()
def add_crypto():
    global crypto
    crypto += 1
    x = random.randint(-250,250)
    y = random.randint(-80,200)
    create_sprite("BTC",x,y)

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

window.onkeypress(add_crypto,"space")

# TODO - make a second control
def buy_computer():
    global computers, crypto, cost
    if crypto >= cost:
        crypto = crypto - cost
        cost  = cost * 2
        computers += 1
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("computer",x,y)

def buy_ferrari():
    global crypto, ferraris
    if crypto >= 50:
        crypto = crypto - 50
        ferraris += 1
        x = random.randint(-200,200)
        y = -225
        create_sprite("ferrari",x,y)

window.onkeypress(buy_computer,"c")
window.onkeypress(buy_ferrari,"f")

# Section 3 - game loop
window.listen()
play = 1
while play >= 0:
    message_sprite.clear()
    crypto += computers / 20
    message_sprite.write(f"Crypto: {round(crypto)}\nComputer Price: {cost}\nFerraris: {ferraris}",font=("Arial",30,"normal"))
    message_sprite.hideturtle()
    # message_sprite.clear()
    # message_sprite.write(f"Crypto: {crypto}\nComputer Price: {cost}\nFerraris: {ferraris}",font=("Arial",30,"normal"))
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()