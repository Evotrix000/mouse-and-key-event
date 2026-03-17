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
    if cat.colliderect(dog):
        cat.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)
        dog.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)   
def on_mouse_down (pos):
    global message
    print(pos)
    if cat.collidepoint(pos):
        message="yea you caught the cat"
        pyautogui.alert("cat")
    if dog.collidepoint(pos):
        
        message="you caught the dog"
    
    cat.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)
    dog.pos= random.randint(0, WIDTH-50),random.randint(0,HEIGHT-50)
pgzrun.go()