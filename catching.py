import pgzrun, random, pyautogui

print(pyautogui.size())
WIDTH, HEIGHT = pyautogui.size()

TITLE = "Shooting game"
cat= Actor("cat.png")
dog= Actor("dog.png")
cat.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)
dog.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)
message= "catch the cat"

def draw():
    screen.blit("bg.png",(0,0))
    cat.draw()
    dog.draw()
    screen.draw.text(message,(50,50))
def update():
    global message
    if keyboard.left:
        dog.x-=10
    if keyboard.right:
        dog.x+=10
    if cat.colliderect(dog):
        cat.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)
        dog.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)

        message="cat.png"
    else:
        message="catch the cat"
def on_key_down(key):
    if key==keys.UP:
        dog.y-=10
    if key==keys.DOWN:
        dog.y+=10
    

pgzrun.go()