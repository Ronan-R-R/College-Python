import turtle
import time

myGame = turtle.Screen()
myGame.title("Title Place Holder")
myGame.bgcolor("Grey")
myGame.screensize(400,800)

turt = turtle.Turtle()
turt.speed(0)
turt.color("Cyan")
turt.shape("turtle")
turt.penup()

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

myGame.listen()
myGame.onkeypress(toggle_pause, "p")

time_limit = 10
start_time = time.time()

while True:
    if not is_paused:
        turt.fd(1)
        turt.lt(1)

        elapse_time = time.time()-start_time
        print(time_limit-int(elapse_time))

        if elapse_time > time_limit:
            print("Game Over")
            exit()
    else:
        start_time = time.time()-elapse_time
        myGame.update()
