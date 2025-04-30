import pgzrun
from pgzero.builtins import clock
import subprocess

# Ustawienia ekranu
WIDTH = 1000
HEIGHT = 590
TITLE = "Galactic Clicker"
FPS = 30

# Bohaterzy
hippo = Actor("hippo", (100, 300))
giraffe = Actor("giraffe", (500, 300))
walrus = Actor("walrus", (900, 300))
ship = Actor("ship", (100, 500))
enemy = Actor("enemy", (500, 500))
animal = Actor("cat", (340, 240))
crocodile = Actor('crocodile', (900, 500))

# Tło
bg = Actor('space')

# Bonusy
bonus_1 = Actor('bonus', (900, 50))
bonus_2 = Actor('bonus', (900, 150))
bonus_3 = Actor('bonus', (900, 250))
bonus_4 = Actor('bonus', (900, 350))
bonus_5 = Actor('bonus', (900, 450))
bonus_6 = Actor('bonus', (900, 550))
bonus_7 = Actor('bonus', (700, 50))

# Przyciski
shop = Actor("sklep", (500, 450))
collection = Actor("kolekcja", (500, 350))
gra = Actor("gra", (500, 250))
cross = Actor("cross", (20, 20))

# Zmienne
mode = "menu"
count = 0
click = 1
prize_1 = 15
prize_2 = 60
prize_3 = 240
prize_4 = 960
prize_5 = 3840
prize_6 = 15360
animals = []

# Dotyczy def draw()
def game_screen():
    bg.draw()
    animal.draw()

    # Bonusy
    bonus_1.draw()
    bonus_2.draw()
    bonus_3.draw()
    bonus_4.draw()
    bonus_5.draw()
    bonus_6.draw()
    cross.draw()

    # Bonusy z tekstem
    screen.draw.text("+1$ co 2s", center=(900, 35), color="black", fontsize=20)
    screen.draw.text(str(prize_1), center=(900, 60), color="black", fontsize=20)
    screen.draw.text("+10$ co 2s", center=(900, 135), color="black", fontsize=20)
    screen.draw.text(str(prize_2), center=(900, 160), color="black", fontsize=20)
    screen.draw.text("+30$ co 2s", center=(900, 235), color="black", fontsize=20)
    screen.draw.text(str(prize_3), center=(900, 260), color="black", fontsize=20)
    screen.draw.text("+90$ co 2s", center=(900, 335), color="black", fontsize=20)
    screen.draw.text(str(prize_4), center=(900, 360), color="black", fontsize=20)
    screen.draw.text("+270$ co 2s", center=(900, 435), color="black", fontsize=20)
    screen.draw.text(str(prize_5), center=(900, 460), color="black", fontsize=20)
    screen.draw.text("+810$ co 2s", center=(900, 535), color="black", fontsize=20)
    screen.draw.text(str(prize_6), center=(900, 560), color="black", fontsize=20)
    screen.draw.text(str(count), (100, 220), color="white", fontsize=46)

# Dotyczy def draw()
def menu_screen():
    bg.draw()
    gra.draw()
    collection.draw()
    shop.draw()
    screen.draw.text(str(count), (50, 50), color="white", fontsize=46)

# Dotyczy def draw()
def shop_screen():
    bg.draw()
    crocodile.draw()
    hippo.draw()
    giraffe.draw()
    walrus.draw()
    ship.draw()
    enemy.draw()
    cross.draw()
    screen.draw.text("cena: 1000$", center=(100, 400), color="white", fontsize=36)
    screen.draw.text("cena: 2000$", center=(500, 400), color="white", fontsize=36)
    screen.draw.text("cena: 4000$", center=(900, 400), color="white", fontsize=36)
    screen.draw.text("cena: 8000$", center=(100, 550), color="white", fontsize=36)
    screen.draw.text("cena: 16000$", center=(500, 550), color="white", fontsize=36)
    screen.draw.text("cena: 32000$", center=(896, 575), color="white", fontsize=36)

# Dotyczy def draw()
def collection_screen():
    bg.draw()
    cross.draw()
    if giraffe in animals:
        giraffe.draw()
        screen.draw.text("+4", (500, 400), color="white", fontsize=36)
    if enemy in animals:
        enemy.draw()
        screen.draw.text("+32", (500, 550), color="white", fontsize=36)
    if ship in animals:
        ship.draw()
        screen.draw.text("+16", (100, 550), color="white", fontsize=36)
    if hippo in animals:
        hippo.draw()
        screen.draw.text("+2", (100, 400), color="white", fontsize=36)
    if crocodile in animals:
        crocodile.draw()
        screen.draw.text("+64", (900, 550), color="white", fontsize=36)
    if walrus in animals:
        walrus.draw()
        screen.draw.text("+8", (900, 370), color="white", fontsize=36)

def draw():
    if mode == "game":
        game_screen()
    elif mode == "menu":
        menu_screen()
    elif mode == "shop":
        shop_screen()
    elif mode == "collection":
        collection_screen()

# Do bonusów/ Dotyczy Bonuses_collisions()
def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 10

def for_bonus_3():
    global count
    count += 30

def for_bonus_4():
    global count
    count += 90

def for_bonus_5():
    global count
    count += 270

def for_bonus_6():
    global count
    count += 810

#Dotyczy on_mouse_game()
def bonuses_collisions(pos):
    global count, prize_1, prize_2, prize_3, prize_4, prize_5, prize_6, prize_7
    
    # Bonus 1
    if bonus_1.collidepoint(pos):
        if count >= prize_1:
            clock.schedule_interval(for_bonus_1, 2)
            count -= prize_1
            prize_1 *= 2
            
    # Bonus 2
    if bonus_2.collidepoint(pos):
        if count >= prize_2:
            clock.schedule_interval(for_bonus_2, 2)
            count -= prize_2
            prize_2 *= 2
            
    # Bonus 3
    if bonus_3.collidepoint(pos):
        if count >= prize_3:
            clock.schedule_interval(for_bonus_3, 2)
            count -= prize_3
            prize_3 *= 2
    
    # Bonus 4
    if bonus_4.collidepoint(pos):
        if count >= prize_4:
            clock.schedule_interval(for_bonus_4, 2)
            count -= prize_4
            prize_4 *= 2
    
    # Bonus 5
    if bonus_5.collidepoint(pos):
        if count >= prize_5:
            clock.schedule_interval(for_bonus_5, 2)
            count -= prize_5
            prize_5 *= 2
    
    # Bonus 6
    if bonus_6.collidepoint(pos):
        if count >= prize_6:
            clock.schedule_interval(for_bonus_6, 2)
            count -= prize_6
            prize_6 *= 2

# Dotyczy on_mouse_game()
def animal_bonuses_animates(pos):
    global click, count
    if animal.collidepoint(pos):
        count += click
        animal.y = 290
        animate(animal, tween='bounce_end', duration=0.5, y=340)

    if bonus_1.collidepoint(pos):
        bonus_1.y = 40
        animate(bonus_1, tween='bounce_end', duration=0.5, y=50)
        
    if bonus_2.collidepoint(pos):
        bonus_2.y = 140
        animate(bonus_2, tween='bounce_end', duration=0.5, y=150)
        
    if bonus_3.collidepoint(pos):
        bonus_3.y = 240
        animate(bonus_3, tween='bounce_end', duration=0.5, y=250)
        
    if bonus_4.collidepoint(pos):
        bonus_4.y = 340
        animate(bonus_4, tween='bounce_end', duration=0.5, y=350)
        
    if bonus_5.collidepoint(pos):
        bonus_5.y = 440
        animate(bonus_5, tween='bounce_end', duration=0.5, y=450)
        
    if bonus_6.collidepoint(pos):
        bonus_6.y = 540
        animate(bonus_6, tween='bounce_end', duration=0.5, y=550)
        
    if bonus_7.collidepoint(pos):
        bonus_7.y = 640
        animate(bonus_7, tween='bounce_end', duration=0.5, y=650)

# Dotyczy on_mouse_game(), on_mouse_shop(), on_mouse_collection()
def cross_button(pos):
    global mode
    if cross.collidepoint(pos):
        mode = "menu"

# Dotyczy on_mouse_menu()
def menu_menage(pos):
    global mode
    if collection.collidepoint(pos):
        mode = "collection"

    if shop.collidepoint(pos):
        mode = "shop"

    if gra.collidepoint(pos):
        mode = "game"

# Dotyczy on_maouse_shop()
def buy_skin(pos):
    global count, click
    if hippo.collidepoint(pos):
        if hippo not in animals:
            if count >= 1000:
                count -= 1000  # Odejmowanie ceny
                click = 2
                animals.append(hippo)
                animal.image = "hippo"
                hippo.y = 280
                animate(hippo, tween="bounce_end", duration=0.5, y=300)

    if giraffe.collidepoint(pos):
        if giraffe not in animals:
            if count >= 2000:
                count -= 2000
                click = 4
                animals.append(giraffe)
                animal.image = "giraffe"
                giraffe.y = 280
                animate(giraffe, tween="bounce_end", duration=0.5, y=300)

    if walrus.collidepoint(pos):
        if walrus not in animals:
            if count >= 4000:
                count -= 4000
                click = 8
                animals.append(walrus)
                animal.image = "walrus"
                walrus.y = 280
                animate(walrus, tween="bounce_end", duration=0.5, y=300)

    if ship.collidepoint(pos):
        if ship not in animals:
            if count >= 8000:
                count -= 8000
                click = 16
                animals.append(ship)
                animal.image = "ship"
                ship.y = 480
                animate(ship, tween="bounce_end", duration=0.5, y=500)

    if enemy.collidepoint(pos):
        if enemy not in animals:
            if count >= 16000:
                count -= 16000
                click = 32
                animals.append(enemy)
                animal.image = "enemy"
                enemy.y = 480
                animate(enemy, tween="bounce_end", duration=0.5, y=500)

    if crocodile.collidepoint(pos):
        if crocodile not in animals:
            if count >= 32000:
                count -= 32000
                click = 64
                animals.append(crocodile)
                animal.image = "crocodile"
                crocodile.y = 480
                animate(crocodile, tween="bounce_end", duration=0.5, y=500)

def change_skin(pos):
    if hippo.collidepoint(pos):
        animal.image = "hippo"
        hippo.y = 280
        animate(hippo, tween="bounce_end", duration = 0.5, y = 300)
        
    if giraffe.collidepoint(pos):
        animal.image = "giraffe"
        giraffe.y = 280
        animate(giraffe, tween="bounce_end", duration = 0.5, y = 300)
        
    if walrus.collidepoint(pos):
        animal.image = "walrus"
        walrus.y = 280
        animate(walrus, tween="bounce_end", duration = 0.5, y = 300)
        
    if ship.collidepoint(pos):
        animal.image = "ship"
        ship.y = 480
        animate(ship, tween="bounce_end", duration = 0.5, y = 500)
        
    if enemy.collidepoint(pos):
        animal.image = "enemy"
        enemy.y = 480
        animate(enemy, tween="bounce_end", duration = 0.5, y = 500)
        
    if crocodile.collidepoint(pos):
        animal.image = "crocodile"
        crocodile.y = 480
        animate(crocodile, tween="bounce_end", duration = 0.5, y = 500)

def on_mouse_down(pos):
    if mode == "game":
        bonuses_collisions(pos)
        animal_bonuses_animates(pos)
        cross_button(pos)
    if mode == "menu":
        menu_menage(pos)
    if mode == "shop":
        buy_skin(pos)
        cross_button(pos)
    if mode == "collection":
        cross_button(pos)
        change_skin(pos)

pgzrun.go()
