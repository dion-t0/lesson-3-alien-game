import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="clicking game"

alien=Actor("alian")
alien.pos=50,50
message='game starts now!'

def draw() :
    screen.fill("black")
    alien.draw()
    #wright text
    screen.draw.text(message,center=(200,20), fontsize=30, color="white")

def move_alien() :
    alien.x=random.randint(50,450)
    alien.y=random.randint(50,450)

def on_mouse_down(pos):
    #if you dont type this its local
    global message 
    
    print("Hi !")
    #if you click on alien what happens

    #alien so it checks if its on the alien
    #collidepoint checks where mouse clicks
    if alien.collidepoint(pos):
        message="Good Shot!"
        move_alien()
    else:
        message="You missed it. try again!"




move_alien()

pgzrun.go()