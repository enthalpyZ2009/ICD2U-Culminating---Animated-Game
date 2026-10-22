# Author: Angela Zhang
# Date: 5/20/2025
# Description:<In this storybook, you play as a hunter, whom a brave survivalist lost in the forgiven jungle. With limited health and food, you must make smart choices each day. To either rest or go find food, and surprises(dangerous!!)
# Every decision matters. If you don’t rest for 3 days, you are pulled into the Dreamland, where you need to survive attacks and earn coins by fighting off magical monsters.
# You have been assigned to defeat a giant jungle boss, which has been threatening your country. If you are rich enough. But if not… oops you have to fight.>


import turtle
import random
import time
import math

print("Welcome to the jungle survival game")
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Just an ordinary day camping…")

screen.tracer(0, 0)
# winsound.PlaySound(os.path.join(os.path.dirname(__file__), '02 Cornfield Chase.wav'),
#                    winsound.SND_LOOP | winsound.SND_ASYNC)

turtle.Turtle().hideturtle()
turtle.hideturtle()

WIDTH = 1000
HEIGHT = 800

fishingRodPen = turtle.Turtle()
fishingRodPen.hideturtle()

bossPen = turtle.Turtle()
bossPen.hideturtle()
bossPen.penup()
bossPen.speed(0)

msgPen = turtle.Turtle()
msgPen.hideturtle()

hunterPen = turtle.Turtle()
hunterPen.hideturtle()
hunterPen.pensize(3)

treePen = turtle.Turtle()
treePen.hideturtle()

rockPen = turtle.Turtle()
rockPen.hideturtle()

roadPen = turtle.Turtle()
roadPen.pensize(3)
roadPen.hideturtle()

signPen = turtle.Turtle()
signPen.pensize(3)
signPen.hideturtle()

fishSignPen = turtle.Turtle()
fishSignPen.pensize(3)
fishSignPen.hideturtle()

tentSignPen = turtle.Turtle()
tentSignPen.hideturtle()

backgroundPen = turtle.Turtle()
backgroundPen.hideturtle()

sunPen = turtle.Turtle()
sunPen.hideturtle()

skyPen = turtle.Turtle()
skyPen.hideturtle()

moonPen = turtle.Turtle()
moonPen.hideturtle()

starPen = turtle.Turtle()
starPen.hideturtle()

mountainsPen = turtle.Turtle()
mountainsPen.hideturtle()

tentPen = turtle.Turtle()
tentPen.hideturtle()

campfirePen = turtle.Turtle()
campfirePen.hideturtle()

flamePen = turtle.Turtle()
flamePen.hideturtle()
flamePen.penup()
flamePen.speed(0)
flamePen.shape("circle")

waterPen = turtle.Turtle()
waterPen.speed(0)
waterPen.hideturtle()

bridgePen = turtle.Turtle()
bridgePen.hideturtle()

grassPen = turtle.Turtle()
grassPen.hideturtle()
grassPen.speed(0)

nightPandaPen = turtle.Turtle()
nightPandaPen.hideturtle()

healthBarPen = turtle.Turtle()
healthBarPen.hideturtle()

foodBarPen = turtle.Turtle()
foodBarPen.hideturtle()

msgPen = turtle.Turtle()
msgPen.hideturtle()

eyeGlowPen = turtle.Turtle()
eyeGlowPen.hideturtle()

WIDTH, HEIGHT = 1000, 800

MAX_ENEMIES = 20
SPAWN_INTERVAL = 3
ATTACK_COOLDOWN = 0.3
MAX_HEALTH = 5
KNIFE_DURATION = 0.3

spawnedEnemies = 0
killedEnemies = 0
gameRunning = True
wobbleState = True
wobbleAngle = 10
wobbleDirection = 1
wobbleCounter = 0
wobbleSpeed = 5

playerPositionScene4 = [0, 0]
PLAYER_RADIUS = 15
PLAYER_SPEED = 5
playerDirection = "down"

ENEMY_SPEED = 10
enemyList = []

lastAttackTime = 0

healthScene4 = 5


lastSpawnTime = 0

knifeShowTime = 0

screen.register_shape("Heart.gif")
heartPen = turtle.Turtle()
heartPen.shape("Heart.gif")
heartPen.hideturtle()

screen.register_shape("Food.gif")
foodPen = turtle.Turtle()
foodPen.shape("Food.gif")
foodPen.hideturtle()

screen.register_shape("Skull.gif")
skullPen = turtle.Turtle()
skullPen.shape("Skull.gif")
skullPen.hideturtle()

glowPen = turtle.Turtle()
glowPen.hideturtle()
glowPen.speed(0)
glowPen.penup()
glowPen.color("#00ff00")

yWater = 0
waterDirection = 1
eye_glow_on = True
killEffects = []

transitionPen = turtle.Turtle()
transitionPen.hideturtle()
transitionPen.speed(0)

currentDay = 1
maxDays = 5
consecutiveNoRest = 0
playerCoins = 0
currentFishingAttempts = 0
maxFishingPerDay = 2
_scene_2_active = False
_scene_5_active = False
_fishing_animate_active = False
_fishing_return_scheduled = False
_dreamland_on_complete = None


def run_transition_card(title, subtitle, on_done, hold_ms=1600):
    transitionPen.clear()
    transitionPen.penup()
    screen.colormode(255)
    transitionPen.color(0, 0, 0)
    transitionPen.goto(-510, 410)
    transitionPen.pendown()
    transitionPen.begin_fill()
    for _ in range(2):
        transitionPen.forward(1020)
        transitionPen.left(90)
        transitionPen.forward(820)
        transitionPen.left(90)
    transitionPen.end_fill()
    transitionPen.penup()
    transitionPen.color("white")
    transitionPen.goto(0, 40)
    transitionPen.write(title, align="center", font=("Arial", 26, "bold"))
    if subtitle:
        transitionPen.goto(0, -20)
        transitionPen.write(subtitle, align="center", font=("Arial", 14, "normal"))
    screen.update()

    def finish():
        transitionPen.clear()
        screen.update()
        if on_done:
            on_done()

    screen.ontimer(finish, hold_ms)


def clear_hub_scene():
    backgroundPen.clear()
    roadPen.clear()
    treePen.clear()
    rockPen.clear()
    hunterPen.clear()
    tentSignPen.clear()
    fishSignPen.clear()
    signPen.clear()
    sunPen.clear()
    msgPen.clear()


def clear_rest_scene():
    global _scene_2_active
    _scene_2_active = False
    healthBarPen.clear()
    foodBarPen.clear()
    heartPen.clear()
    foodPen.clear()
    skyPen.clear()
    backgroundPen.clear()
    mountainsPen.clear()
    starPen.clear()
    rockPen.clear()
    tentPen.clear()
    campfirePen.clear()
    moonPen.clear()
    flamePen.clear()
    msgPen.clear()


def clear_fishing_scene():
    global _fishing_animate_active
    _fishing_animate_active = False
    hunterPen.clear()
    fishingRodPen.clear()
    fishSignPen.clear()
    waterPen.clear()
    bridgePen.clear()
    msgPen.clear()


def clear_dreamland_scene():
    global enemyList, spawnedEnemies, killedEnemies, healthScene4, gameRunning
    gameRunning = False
    grassPen.clear()
    treePen.clear()
    nightPandaPen.clear()
    hunterPen.clear()
    healthBarPen.clear()
    msgPen.clear()
    enemyList = []
    spawnedEnemies = 0
    killedEnemies = 0
    healthScene4 = MAX_HEALTH
    playerPositionScene4[0] = 0
    playerPositionScene4[1] = 0
    screen.bgcolor("skyblue")
    screen.update()


def draw_hub_frame():
    screen.bgcolor("skyblue")
    scene_1()
    draw_hunter_health_bar(150, 350)
    draw_hunter_food_bar(150, 280)
    screen.update()


def animate_walk_to_rest(on_done):
    for i in range(50):
        hunterPen.clear()
        hunterFrontView(-400 + 4 * i, -200 + 2 * i, 0.6)
        sword(-350 + 4 * i, -145 + 2 * i, 0.6, -50)
        screen.update()
    for i in range(190):
        hunterPen.clear()
        hunterFrontView(-200 + 4 * i, -100, 0.6)
        sword(-150 + 4 * i, -45, 0.6, -50)
        screen.update()
    if on_done:
        on_done()


def animate_walk_to_fish(on_done):
    for i in range(60):
        hunterPen.clear()
        hunterFrontView(-400 + 4 * i, -200, 0.6)
        sword(-350 + 4 * i, -145, 0.6, -50)
        screen.update()
    for i in range(190):
        hunterPen.clear()
        hunterFrontView(-160 + 4 * i, -200 - i * 0.5, 0.6)
        sword(-110 + 4 * i, -145 - i * 0.5, 0.6, -50)
        screen.update()
    if on_done:
        on_done()


def animate_walk_from_rest(on_done):
    for i in range(190):
        hunterPen.clear()
        hunterFrontView(560 - 4 * i, -100, 0.6)
        sword(610 - 4 * i, -45, 0.6, -50)
        screen.update()
    for i in range(50):
        hunterPen.clear()
        hunterFrontView(-400 + 4 * (49 - i), -200 + 2 * (49 - i), 0.6)
        sword(-350 + 4 * (49 - i), -145 + 2 * (49 - i), 0.6, -50)
        screen.update()
    if on_done:
        on_done()


def animate_walk_from_fish(on_done):
    for i in range(190):
        hunterPen.clear()
        hunterFrontView(600 - 4 * i, -200 - (189 - i) * 0.5, 0.6)
        sword(650 - 4 * i, -145 - (189 - i) * 0.5, 0.6, -50)
        screen.update()
    for i in range(60):
        hunterPen.clear()
        hunterFrontView(-400 + 4 * i, -200, 0.6)
        sword(-350 + 4 * i, -145, 0.6, -50)
        screen.update()
    if on_done:
        on_done()


def hunterFrontView(xHunterPos, yHunterPos, scale):
    # --- PANTS ---
    hunterPen.penup()
    hunterPen.pencolor("#000000")
    hunterPen.fillcolor("#f6e208")
    hunterPen.pensize(3 * scale)
    hunterPen.speed(0)

    hunterPen.goto(-50 * scale + xHunterPos, 34 * scale + yHunterPos)
    hunterPen.begin_fill()
    hunterPen.pendown()

    hunterPen.goto(50 * scale + xHunterPos, 34 * scale + yHunterPos)
    hunterPen.goto(82 * scale + xHunterPos, 68 * scale + yHunterPos)
    hunterPen.goto(-82 * scale + xHunterPos, 68 * scale + yHunterPos)
    hunterPen.goto(-50 * scale + xHunterPos, 34 * scale + yHunterPos)
    hunterPen.end_fill()

    # --- BODY ---
    hunterPen.penup()
    hunterPen.fillcolor("#15e109")
    hunterPen.goto(-82 * scale + xHunterPos, 68 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(82 * scale + xHunterPos, 68 * scale + yHunterPos)
    hunterPen.goto(82 * scale + xHunterPos, 158 * scale + yHunterPos)
    hunterPen.goto(101 * scale + xHunterPos, 170 * scale + yHunterPos)
    hunterPen.goto(65 * scale + xHunterPos, 195 * scale + yHunterPos)
    hunterPen.goto(-65 * scale + xHunterPos, 195 * scale + yHunterPos)
    hunterPen.goto(-101 * scale + xHunterPos, 170 * scale + yHunterPos)
    hunterPen.goto(-82 * scale + xHunterPos, 68 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- ARMS AND HANDS ---
    hunterPen.fillcolor("#f7cf89")
    hunterPen.goto(77 * scale + xHunterPos, 111 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(77 * scale + xHunterPos, 91 * scale + yHunterPos)
    hunterPen.goto(105 * scale + xHunterPos, 91 * scale + yHunterPos)
    hunterPen.goto(105 * scale + xHunterPos, 111 * scale + yHunterPos)
    hunterPen.goto(77 * scale + xHunterPos, 111 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()
    hunterPen.fillcolor("#a13a01")
    hunterPen.pendown()
    hunterPen.setheading(90)
    hunterPen.begin_fill()
    hunterPen.goto(77 * scale + xHunterPos, 160 * scale + yHunterPos)
    hunterPen.circle(-14 * scale, 180)  # circle radius needs scaling
    hunterPen.setheading(0)
    hunterPen.goto(105 * scale + xHunterPos, 112 * scale + yHunterPos)
    hunterPen.goto(77 * scale + xHunterPos, 112 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- HEAD ---
    hunterPen.fillcolor("#f7cf89")
    hunterPen.penup()
    hunterPen.goto(-50 * scale + xHunterPos, 170 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(50 * scale + xHunterPos, 170 * scale + yHunterPos)
    hunterPen.goto(85 * scale + xHunterPos, 230 * scale + yHunterPos)
    hunterPen.goto(114 * scale + xHunterPos, 230 * scale + yHunterPos)
    hunterPen.goto(114 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.goto(-114 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.goto(-114 * scale + xHunterPos, 230 * scale + yHunterPos)
    hunterPen.goto(-85 * scale + xHunterPos, 230 * scale + yHunterPos)
    hunterPen.goto(-50 * scale + xHunterPos, 170 * scale + yHunterPos)
    hunterPen.end_fill()

    # --- HAT ---
    hunterPen.fillcolor("#3ff73c")
    hunterPen.penup()
    hunterPen.goto(-75 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(-75 * scale + xHunterPos, 262 * scale + yHunterPos)
    hunterPen.goto(-56 * scale + xHunterPos, 244 * scale + yHunterPos)
    hunterPen.goto(56 * scale + xHunterPos, 244 * scale + yHunterPos)
    hunterPen.goto(75 * scale + xHunterPos, 262 * scale + yHunterPos)
    hunterPen.goto(75 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.goto(-75 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.end_fill()

    # --- HAT ---
    hunterPen.fillcolor("#ff7b00")
    hunterPen.penup()
    hunterPen.goto(-60 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(-31 * scale + xHunterPos, 320 * scale + yHunterPos)
    hunterPen.goto(31 * scale + xHunterPos, 320 * scale + yHunterPos)
    hunterPen.goto(60 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.goto(45 * scale + xHunterPos, 268 * scale + yHunterPos)
    hunterPen.goto(-45 * scale + xHunterPos, 268 * scale + yHunterPos)
    hunterPen.goto(-60 * scale + xHunterPos, 285 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- HAT ---
    hunterPen.fillcolor("#f6e208")
    hunterPen.goto(-53 * scale + xHunterPos, 293.44 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(-31 * scale + xHunterPos, 320 * scale + yHunterPos)
    hunterPen.goto(31 * scale + xHunterPos, 320 * scale + yHunterPos)
    hunterPen.goto(53 * scale + xHunterPos, 293.44 * scale + yHunterPos)
    hunterPen.goto(40 * scale + xHunterPos, 275 * scale + yHunterPos)
    hunterPen.goto(-40 * scale + xHunterPos, 275 * scale + yHunterPos)
    hunterPen.goto(-53 * scale + xHunterPos, 293.44 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- EAR ---
    hunterPen.penup()
    hunterPen.fillcolor("#ffc7ae")
    hunterPen.goto(-100 * scale + xHunterPos, 270 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(-82 * scale + xHunterPos, 270 * scale + yHunterPos)
    hunterPen.goto(-82 * scale + xHunterPos, 241 * scale + yHunterPos)
    hunterPen.goto(-100 * scale + xHunterPos, 241 * scale + yHunterPos)
    hunterPen.goto(-100 * scale + xHunterPos, 270 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()
    hunterPen.goto(100 * scale + xHunterPos, 270 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(82 * scale + xHunterPos, 270 * scale + yHunterPos)
    hunterPen.goto(82 * scale + xHunterPos, 241 * scale + yHunterPos)
    hunterPen.goto(100 * scale + xHunterPos, 241 * scale + yHunterPos)
    hunterPen.goto(100 * scale + xHunterPos, 270 * scale + yHunterPos)
    hunterPen.end_fill()

    # --- EYE ---
    hunterPen.pensize(5 * scale)
    hunterPen.penup()
    hunterPen.goto(-30 * scale + xHunterPos, 220 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.goto(-30 * scale + xHunterPos, 200 * scale + yHunterPos)
    hunterPen.penup()
    hunterPen.goto(30 * scale + xHunterPos, 220 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.goto(30 * scale + xHunterPos, 200 * scale + yHunterPos)
    hunterPen.penup()
    hunterPen.pensize(3 * scale)

    # --- SHOES ---
    # left
    hunterPen.goto(-58 * scale + xHunterPos, 45 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.fillcolor("#c61821")
    hunterPen.begin_fill()
    hunterPen.goto(-75 * scale + xHunterPos, 45 * scale + yHunterPos)
    hunterPen.goto(-90 * scale + xHunterPos, 0 * scale + yHunterPos)
    hunterPen.goto(-40 * scale + xHunterPos, 0 * scale + yHunterPos)
    hunterPen.goto(-15 * scale + xHunterPos, 22 * scale + yHunterPos)
    hunterPen.goto(-15 * scale + xHunterPos, 34 * scale + yHunterPos)
    hunterPen.goto(-58 * scale + xHunterPos, 45 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # right
    hunterPen.goto(58 * scale + xHunterPos, 45 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.fillcolor("#c61821")
    hunterPen.begin_fill()
    hunterPen.goto(75 * scale + xHunterPos, 45 * scale + yHunterPos)
    hunterPen.goto(90 * scale + xHunterPos, 0 * scale + yHunterPos)
    hunterPen.goto(40 * scale + xHunterPos, 0 * scale + yHunterPos)
    hunterPen.goto(15 * scale + xHunterPos, 22 * scale + yHunterPos)
    hunterPen.goto(15 * scale + xHunterPos, 34 * scale + yHunterPos)
    hunterPen.goto(58 * scale + xHunterPos, 45 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # belt
    hunterPen.fillcolor("#efd742")
    hunterPen.goto(-10 * scale + xHunterPos, 127 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(35 * scale + xHunterPos, 127 * scale + yHunterPos)
    hunterPen.goto(35 * scale + xHunterPos, 120 * scale + yHunterPos)
    hunterPen.goto(46 * scale + xHunterPos, 121 * scale + yHunterPos)
    hunterPen.goto(77 * scale + xHunterPos, 137.6 * scale + yHunterPos)
    hunterPen.goto(77 * scale + xHunterPos, 114.6 * scale + yHunterPos)
    hunterPen.goto(46 * scale + xHunterPos, 98 * scale + yHunterPos)
    hunterPen.goto(35 * scale + xHunterPos, 97 * scale + yHunterPos)
    hunterPen.goto(35 * scale + xHunterPos, 90 * scale + yHunterPos)
    hunterPen.goto(-15 * scale + xHunterPos, 90 * scale + yHunterPos)
    hunterPen.goto(-10 * scale + xHunterPos, 127 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.pensize(2 * scale)
    hunterPen.fillcolor("#e6b800")
    hunterPen.goto(-10 * scale + xHunterPos, 120 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(27 * scale + xHunterPos, 120 * scale + yHunterPos)
    hunterPen.goto(27 * scale + xHunterPos, 113 * scale + yHunterPos)
    hunterPen.goto(46 * scale + xHunterPos, 114 * scale + yHunterPos)
    hunterPen.goto(77 * scale + xHunterPos, 130.6 * scale + yHunterPos)
    hunterPen.goto(77 * scale + xHunterPos, 123.6 * scale + yHunterPos)
    hunterPen.goto(46 * scale + xHunterPos, 107 * scale + yHunterPos)
    hunterPen.goto(27 * scale + xHunterPos, 106 * scale + yHunterPos)
    hunterPen.goto(27 * scale + xHunterPos, 97 * scale + yHunterPos)
    hunterPen.goto(-12 * scale + xHunterPos, 97 * scale + yHunterPos)
    hunterPen.goto(-10 * scale + xHunterPos, 120 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- SHIELD ---
    hunterPen.pensize(3 * scale)
    hunterPen.penup()
    hunterPen.goto(-120 * scale + xHunterPos, 175 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.fillcolor("white")
    hunterPen.begin_fill()
    hunterPen.goto(-90 * scale + xHunterPos, 175 * scale + yHunterPos)
    hunterPen.goto(-90 * scale + xHunterPos, 159 * scale + yHunterPos)
    hunterPen.goto(-40 * scale + xHunterPos, 159 * scale + yHunterPos)
    hunterPen.goto(-40 * scale + xHunterPos, 175 * scale + yHunterPos)
    hunterPen.goto(-10 * scale + xHunterPos, 175 * scale + yHunterPos)
    hunterPen.goto(-10 * scale + xHunterPos, 100 * scale + yHunterPos)
    hunterPen.goto(-45 * scale + xHunterPos, 60 * scale + yHunterPos)
    hunterPen.goto(-85 * scale + xHunterPos, 60 * scale + yHunterPos)
    hunterPen.goto(-120 * scale + xHunterPos, 100 * scale + yHunterPos)
    hunterPen.goto(-120 * scale + xHunterPos, 175 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("#2929ce")
    hunterPen.begin_fill()
    hunterPen.goto(-110 * scale + xHunterPos, 149 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.goto(-20 * scale + xHunterPos, 149 * scale + yHunterPos)
    hunterPen.goto(-20 * scale + xHunterPos, 105 * scale + yHunterPos)
    hunterPen.goto(-48 * scale + xHunterPos, 73 * scale + yHunterPos)
    hunterPen.goto(-82 * scale + xHunterPos, 73 * scale + yHunterPos)
    hunterPen.goto(-110 * scale + xHunterPos, 105 * scale + yHunterPos)
    hunterPen.goto(-110 * scale + xHunterPos, 149 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("#8484f7")
    hunterPen.goto(-97 * scale + xHunterPos, 138 * scale + yHunterPos)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(-33 * scale + xHunterPos, 138 * scale + yHunterPos)
    hunterPen.goto(-37 * scale + xHunterPos, 100 * scale + yHunterPos)
    hunterPen.goto(-51 * scale + xHunterPos, 80 * scale + yHunterPos)
    hunterPen.goto(-79 * scale + xHunterPos, 80 * scale + yHunterPos)
    hunterPen.goto(-93 * scale + xHunterPos, 100 * scale + yHunterPos)
    hunterPen.goto(-97 * scale + xHunterPos, 138 * scale + yHunterPos)
    hunterPen.end_fill()
    hunterPen.penup()

    # Snowflake pattern on the --- SHIELD ---
    hunterPen.pensize(2 * scale)
    hunterPen.penup()
    hunterPen.goto(-87 * scale + xHunterPos, 85.0 * scale + yHunterPos)
    hunterPen.setheading(0)
    hunterPen.forward(22.5 * scale)
    hunterPen.left(90)
    hunterPen.forward(22.667 * scale)
    hunterPen.right(90)
    hunterPen.pendown()

    hunterPen.pencolor("white")
    hunterPen.penup()
    hunterPen.forward(12.5 * scale)
    hunterPen.right(50)
    hunterPen.forward(12.5 * scale)
    hunterPen.left(115.15)
    hunterPen.circle(22.667 * scale, 18)
    hunterPen.pencolor("aqua")
    hunterPen.pendown()
    hunterPen.circle(1.667 * scale)

    for _ in range(5):
        hunterPen.penup()
        hunterPen.circle(22.667 * scale, 60)
        hunterPen.pendown()
        hunterPen.pencolor("aqua")
        hunterPen.circle(1.667 * scale)

    hunterPen.penup()
    hunterPen.circle(22.5 * scale, 18)
    hunterPen.left(90)
    hunterPen.forward(22.5 * scale)
    hunterPen.left(90)
    hunterPen.forward(0.25 * scale)
    hunterPen.right(90)
    hunterPen.pendown()

    for _ in range(6):
        for _ in range(2):
            hunterPen.pencolor("white")
            hunterPen.forward(10.0 * scale)
            hunterPen.right(50)
            hunterPen.forward(10.0 * scale)
            hunterPen.right(130)

        for _ in range(2):
            hunterPen.pencolor("blue")
            hunterPen.forward(6.667 * scale)
            hunterPen.right(50)
            hunterPen.forward(6.667 * scale)
            hunterPen.right(130)

        hunterPen.left(60)
    hunterPen.penup()
    hunterPen.pencolor("black")
    hunterPen.pensize(3 * scale)


def hunterBackView(xHunterPos, yHunterPos, scale, armUp=False):
    hunterPen.pencolor("#000000")
    hunterPen.pensize(3 * scale)

    # --- SHIELD ---
    hunterPen.penup()
    hunterPen.goto(xHunterPos + 120 * scale, yHunterPos + 175 * scale)
    hunterPen.pendown()
    hunterPen.fillcolor("#708090")
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 90 * scale, yHunterPos + 175 * scale)
    hunterPen.goto(xHunterPos + 90 * scale, yHunterPos + 159 * scale)
    hunterPen.goto(xHunterPos + 40 * scale, yHunterPos + 159 * scale)
    hunterPen.goto(xHunterPos + 40 * scale, yHunterPos + 175 * scale)
    hunterPen.goto(xHunterPos + 10 * scale, yHunterPos + 175 * scale)
    hunterPen.goto(xHunterPos + 10 * scale, yHunterPos + 100 * scale)
    hunterPen.goto(xHunterPos + 45 * scale, yHunterPos + 60 * scale)
    hunterPen.goto(xHunterPos + 85 * scale, yHunterPos + 60 * scale)
    hunterPen.goto(xHunterPos + 120 * scale, yHunterPos + 100 * scale)
    hunterPen.goto(xHunterPos + 120 * scale, yHunterPos + 175 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- SHOES --- - Left
    hunterPen.goto(xHunterPos + (-58) * scale, yHunterPos + 45 * scale)
    hunterPen.pendown()
    hunterPen.fillcolor("#c61821")
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + (-75) * scale, yHunterPos + 45 * scale)
    hunterPen.goto(xHunterPos + (-90) * scale, yHunterPos + 0 * scale)
    hunterPen.goto(xHunterPos + (-40) * scale, yHunterPos + 0 * scale)
    hunterPen.goto(xHunterPos + (-15) * scale, yHunterPos + 22 * scale)
    hunterPen.goto(xHunterPos + (-15) * scale, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos + (-58) * scale, yHunterPos + 45 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- SHOES --- - Right
    hunterPen.goto(xHunterPos + 58 * scale, yHunterPos + 45 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 75 * scale, yHunterPos + 45 * scale)
    hunterPen.goto(xHunterPos + 90 * scale, yHunterPos + 0 * scale)
    hunterPen.goto(xHunterPos + 40 * scale, yHunterPos + 0 * scale)
    hunterPen.goto(xHunterPos + 15 * scale, yHunterPos + 22 * scale)
    hunterPen.goto(xHunterPos + 15 * scale, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos + 58 * scale, yHunterPos + 45 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- PANTS ---
    hunterPen.fillcolor("#f6e208")
    hunterPen.goto(xHunterPos + (-50) * scale, yHunterPos + 34 * scale)
    hunterPen.begin_fill()
    hunterPen.pendown()
    hunterPen.goto(xHunterPos + 50 * scale, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos + 82 * scale, yHunterPos + 68 * scale)
    hunterPen.goto(xHunterPos + (-82) * scale, yHunterPos + 68 * scale)
    hunterPen.goto(xHunterPos + (-50) * scale, yHunterPos + 34 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- ARMS AND HANDS ---
    hunterPen.fillcolor("#f7cf89")  # hand
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 91 * scale)
    hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 91 * scale)
    hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 111 * scale)
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # right
    hunterPen.fillcolor("#a13a01")
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
    hunterPen.setheading(90)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 160 * scale)
    hunterPen.circle(-14 * scale, 180)
    hunterPen.setheading(0)
    hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 112 * scale)
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 112 * scale)
    hunterPen.end_fill()
    hunterPen.penup()
    # left
    if armUp == False:
        # --- ARMS AND HANDS ---
        hunterPen.fillcolor("#f7cf89")
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 91 * scale)
        hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 91 * scale)
        hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 111 * scale)
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

        hunterPen.fillcolor("#a13a01")
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
        hunterPen.setheading(90)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 160 * scale)
        hunterPen.circle(-14 * scale, 180)
        hunterPen.setheading(0)
        hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 112 * scale)
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 112 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

        hunterPen.fillcolor("#f7cf89")
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 111 * scale)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 91 * scale)
        hunterPen.goto(xHunterPos + (-105) * scale, yHunterPos + 91 * scale)
        hunterPen.goto(xHunterPos + (-105) * scale, yHunterPos + 111 * scale)
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 111 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

        hunterPen.fillcolor("#a13a01")
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 111 * scale)
        hunterPen.setheading(90)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 160 * scale)
        hunterPen.circle(14 * scale, 180)
        hunterPen.setheading(0)
        hunterPen.goto(xHunterPos + (-105) * scale, yHunterPos + 112 * scale)
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 112 * scale)
        hunterPen.end_fill()
        hunterPen.penup()
    else:
        hunterPen.fillcolor("#f7cf89")
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 91 * scale)
        hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 91 * scale)
        hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 111 * scale)
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

        hunterPen.fillcolor("#a13a01")
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 111 * scale)
        hunterPen.setheading(90)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 160 * scale)
        hunterPen.circle(-14 * scale, 180)
        hunterPen.setheading(0)
        hunterPen.goto(xHunterPos + 105 * scale, yHunterPos + 112 * scale)
        hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 112 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

        # Light yellow rectangle (arm)
        hunterPen.fillcolor("#f7cf89")
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 195 - 111 * scale)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 195 - 91 * scale)
        hunterPen.goto(xHunterPos + (-105) * scale, yHunterPos + 195 - 91 * scale)
        hunterPen.goto(xHunterPos + (-105) * scale, yHunterPos + 195 - 111 * scale)
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 195 - 111 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

        # Brown sleeve arc
        hunterPen.fillcolor("#a13a01")
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 195 - 111 * scale)
        hunterPen.setheading(-90)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 195 - 160 * scale)
        hunterPen.circle(-14 * scale, 180)
        hunterPen.setheading(0)
        hunterPen.goto(xHunterPos + (-105) * scale, yHunterPos + 195 - 112 * scale)
        hunterPen.goto(xHunterPos + (-77) * scale, yHunterPos + 195 - 112 * scale)
        hunterPen.end_fill()
        hunterPen.penup()

    # --- HEAD ---
    hunterPen.fillcolor("#f7cf89")
    hunterPen.penup()
    hunterPen.goto(xHunterPos + scale * -50, yHunterPos + scale * 170)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + scale * 50, yHunterPos + scale * 170)
    hunterPen.goto(xHunterPos + scale * 85, yHunterPos + scale * 230)
    hunterPen.goto(xHunterPos + scale * 114, yHunterPos + scale * 230)
    hunterPen.goto(xHunterPos + scale * 114, yHunterPos + scale * 285)
    hunterPen.goto(xHunterPos + scale * -114, yHunterPos + scale * 285)
    hunterPen.goto(xHunterPos + scale * -114, yHunterPos + scale * 230)
    hunterPen.goto(xHunterPos + scale * -85, yHunterPos + scale * 230)
    hunterPen.goto(xHunterPos + scale * -50, yHunterPos + scale * 170)
    hunterPen.end_fill()

    # --- --- BODY --- ---
    hunterPen.penup()
    hunterPen.fillcolor("#15e109")
    hunterPen.goto(xHunterPos + scale * -82, yHunterPos + scale * 68)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + scale * 82, yHunterPos + scale * 68)
    hunterPen.goto(xHunterPos + scale * 82, yHunterPos + scale * 158)
    hunterPen.goto(xHunterPos + scale * 101, yHunterPos + scale * 170)
    hunterPen.goto(xHunterPos + scale * 65, yHunterPos + scale * 195)
    hunterPen.goto(xHunterPos + scale * -65, yHunterPos + scale * 195)
    hunterPen.goto(xHunterPos + scale * -101, yHunterPos + scale * 170)
    hunterPen.goto(xHunterPos + scale * -82, yHunterPos + scale * 158)
    hunterPen.goto(xHunterPos + scale * -82, yHunterPos + scale * 68)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- BELT ---
    hunterPen.penup()
    hunterPen.fillcolor("#efd742")
    hunterPen.goto(xHunterPos + scale * -82, yHunterPos + scale * 137.6)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + scale * -46, yHunterPos + scale * 121)
    hunterPen.goto(xHunterPos + scale * 46, yHunterPos + scale * 121)
    hunterPen.goto(xHunterPos + scale * 82, yHunterPos + scale * 137.6)
    hunterPen.goto(xHunterPos + scale * 82, yHunterPos + scale * 114.6)
    hunterPen.goto(xHunterPos + scale * 46, yHunterPos + scale * 98)
    hunterPen.goto(xHunterPos + scale * -46, yHunterPos + scale * 98)
    hunterPen.goto(xHunterPos + scale * -82, yHunterPos + scale * 114.6)
    hunterPen.goto(xHunterPos + scale * -82, yHunterPos + scale * 137.6)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- HAT BASE ---
    hunterPen.fillcolor("#3ff73c")
    hunterPen.penup()
    hunterPen.goto(xHunterPos + scale * -75, yHunterPos + scale * 285)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + scale * -75, yHunterPos + scale * 262)
    hunterPen.goto(xHunterPos + scale * -56, yHunterPos + scale * 244)
    hunterPen.goto(xHunterPos + scale * 56, yHunterPos + scale * 244)
    hunterPen.goto(xHunterPos + scale * 75, yHunterPos + scale * 262)
    hunterPen.goto(xHunterPos + scale * 75, yHunterPos + scale * 285)
    hunterPen.goto(xHunterPos + scale * -75, yHunterPos + scale * 285)
    hunterPen.end_fill()

    # --- --- HAT --- MIDDLE ---
    hunterPen.fillcolor("#ff7b00")
    hunterPen.penup()
    hunterPen.goto(xHunterPos + scale * -60, yHunterPos + scale * 285)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + scale * -31, yHunterPos + scale * 320)
    hunterPen.goto(xHunterPos + scale * 31, yHunterPos + scale * 320)
    hunterPen.goto(xHunterPos + scale * 60, yHunterPos + scale * 285)
    hunterPen.goto(xHunterPos + scale * 45, yHunterPos + scale * 268)
    hunterPen.goto(xHunterPos + scale * -45, yHunterPos + scale * 268)
    hunterPen.goto(xHunterPos + scale * -60, yHunterPos + scale * 285)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- --- HAT --- TOP ---
    hunterPen.fillcolor("#f6e208")
    hunterPen.penup()
    hunterPen.goto(xHunterPos + scale * -53, yHunterPos + scale * 293.44)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + scale * -31, yHunterPos + scale * 320)
    hunterPen.goto(xHunterPos + scale * 31, yHunterPos + scale * 320)
    hunterPen.goto(xHunterPos + scale * 53, yHunterPos + scale * 293.44)
    hunterPen.goto(xHunterPos + scale * 40, yHunterPos + scale * 275)
    hunterPen.goto(xHunterPos + scale * -40, yHunterPos + scale * 275)
    hunterPen.goto(xHunterPos + scale * -53, yHunterPos + scale * 293.44)
    hunterPen.end_fill()
    hunterPen.penup()


# flip == 1: facing right
# flip == -1: facing left
def hunterSideView(flip, xHunterPos, yHunterPos, scale, armUp=False):
    hunterPen.penup()
    hunterPen.pensize(3 * scale)
    # --- SHIELD ---
    hunterPen.goto(xHunterPos + 66 * scale * flip, yHunterPos + 220 * scale)
    hunterPen.fillcolor("#56628a")
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 85 * scale * flip, yHunterPos + 198 * scale)
    hunterPen.goto(xHunterPos + 85 * scale * flip, yHunterPos + 127 * scale)
    hunterPen.goto(xHunterPos + 70 * scale * flip, yHunterPos + 100 * scale)
    hunterPen.goto(xHunterPos + 20 * scale * flip, yHunterPos + 150 * scale)
    hunterPen.goto(xHunterPos + 66 * scale * flip, yHunterPos + 220 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("white")
    hunterPen.goto(xHunterPos + 75 * scale * flip, yHunterPos + 190 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 85 * scale * flip, yHunterPos + 188 * scale)
    hunterPen.goto(xHunterPos + 85 * scale * flip, yHunterPos + 152 * scale)
    hunterPen.goto(xHunterPos + 75 * scale * flip, yHunterPos + 146 * scale)
    hunterPen.goto(xHunterPos + 75 * scale * flip, yHunterPos + 190 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- BODY ---
    hunterPen.fillcolor("#15e109")
    hunterPen.goto(xHunterPos + 55 * scale * flip, yHunterPos + 185 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 67 * scale * flip, yHunterPos + 170 * scale)
    hunterPen.goto(xHunterPos + 64 * scale * flip, yHunterPos + 62 * scale)
    hunterPen.goto(xHunterPos - 64 * scale * flip, yHunterPos + 62 * scale)
    hunterPen.goto(xHunterPos - 67 * scale * flip, yHunterPos + 170 * scale)
    hunterPen.goto(xHunterPos - 55 * scale * flip, yHunterPos + 185 * scale)
    hunterPen.goto(xHunterPos + 55 * scale * flip, yHunterPos + 185 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- PANTS ---
    hunterPen.fillcolor("#f6e208")
    hunterPen.goto(xHunterPos - 64 * scale * flip, yHunterPos + 62 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 64 * scale * flip, yHunterPos + 62 * scale)
    hunterPen.goto(xHunterPos + 49 * scale * flip, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos - 49 * scale * flip, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos - 64 * scale * flip, yHunterPos + 62 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # head
    hunterPen.fillcolor("#f7cf89")
    hunterPen.goto(xHunterPos + 69 * scale * flip, yHunterPos + 263 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 66 * scale * flip, yHunterPos + 230 * scale)
    hunterPen.setheading(-93.58 if flip == 1 else -86.42)
    hunterPen.circle(-66 * scale * flip, 163)
    hunterPen.goto(xHunterPos - 69 * scale * flip, yHunterPos + 263 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- EYE ---
    hunterPen.pensize(5 * scale)
    hunterPen.goto(xHunterPos + 45 * scale * flip, yHunterPos + 240 * scale)
    hunterPen.pendown()
    hunterPen.goto(xHunterPos + 45 * scale * flip, yHunterPos + 220 * scale)
    hunterPen.pensize(3 * scale)
    hunterPen.penup()

    # --- HAT ---
    hunterPen.fillcolor("#15e109")
    hunterPen.goto(xHunterPos - 77 * scale * flip, yHunterPos + 277 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 77 * scale * flip, yHunterPos + 277 * scale)
    hunterPen.goto(xHunterPos + 77 * scale * flip, yHunterPos + 263 * scale)
    hunterPen.goto(xHunterPos - 77 * scale * flip, yHunterPos + 263 * scale)
    hunterPen.goto(xHunterPos - 77 * scale * flip, yHunterPos + 277 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("#ff7b00")
    hunterPen.goto(xHunterPos - 55 * scale * flip, yHunterPos + 277 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 55 * scale * flip, yHunterPos + 277 * scale)
    hunterPen.goto(xHunterPos + 30 * scale * flip, yHunterPos + 312 * scale)
    hunterPen.goto(xHunterPos - 30 * scale * flip, yHunterPos + 312 * scale)
    hunterPen.goto(xHunterPos - 55 * scale * flip, yHunterPos + 277 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("#f6e208")
    hunterPen.goto(xHunterPos - 30 * scale * flip, yHunterPos + 312 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 30 * scale * flip, yHunterPos + 312 * scale)
    hunterPen.goto(xHunterPos + 48 * scale * flip, yHunterPos + 286.8 * scale)
    hunterPen.goto(xHunterPos - 48 * scale * flip, yHunterPos + 286.8 * scale)
    hunterPen.goto(xHunterPos - 30 * scale * flip, yHunterPos + 312 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- EAR ---
    hunterPen.fillcolor("#f7cf89")
    hunterPen.goto(xHunterPos - 21 * scale * flip, yHunterPos + 230 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos - 7 * scale * flip, yHunterPos + 230 * scale)
    hunterPen.goto(xHunterPos - 7 * scale * flip, yHunterPos + 297 * scale)
    hunterPen.goto(xHunterPos - 21 * scale * flip, yHunterPos + 297 * scale)
    hunterPen.goto(xHunterPos - 21 * scale * flip, yHunterPos + 230 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # belt
    hunterPen.fillcolor("#efd742")
    hunterPen.goto(xHunterPos - 65.6 * scale, yHunterPos + 119.6 * scale)
    hunterPen.setheading(-30)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.circle(131.2 * scale, 60)
    hunterPen.goto(xHunterPos + 65.16 * scale, yHunterPos + 103.76 * scale)
    hunterPen.setheading(210)
    hunterPen.circle(-131.2 * scale, 60)
    hunterPen.goto(xHunterPos - 65.6 * scale, yHunterPos + 119.6 * scale)
    hunterPen.end_fill()
    hunterPen.penup()
    if armUp == False:
        # arm & hand
        hunterPen.fillcolor("#f7cf89")
        hunterPen.goto(xHunterPos - 19 * scale * flip, yHunterPos + 95 * scale)
        hunterPen.pendown()
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos + 19 * scale * flip, yHunterPos + 95 * scale)
        hunterPen.goto(xHunterPos + 19 * scale * flip, yHunterPos + 68 * scale)
        hunterPen.goto(xHunterPos - 19 * scale * flip, yHunterPos + 68 * scale)
        hunterPen.goto(xHunterPos - 19 * scale * flip, yHunterPos + 95 * scale)
        hunterPen.end_fill()

        hunterPen.fillcolor("#a13a01")
        hunterPen.begin_fill()
        hunterPen.goto(xHunterPos - 19 * scale * flip, yHunterPos + 143 * scale)
        hunterPen.setheading(90)
        hunterPen.circle(-19 * scale * flip, 185)
        hunterPen.setheading(0)
        hunterPen.goto(xHunterPos + 19 * scale * flip, yHunterPos + 95 * scale)
        hunterPen.goto(xHunterPos - 19 * scale * flip, yHunterPos + 95 * scale)
        hunterPen.end_fill()
        hunterPen.penup()
    else:
        if flip == -1:
            def armUpLeft():
                hunterPen.fillcolor("#f7cf89")
                hunterPen.goto(xHunterPos + 95 * scale - 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.pendown()
                hunterPen.begin_fill()
                hunterPen.goto(xHunterPos + 95 * scale - 92, yHunterPos + 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos + 68 * scale - 92, yHunterPos + 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos + 68 * scale - 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos + 95 * scale - 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.end_fill()

                hunterPen.fillcolor("#a13a01")
                hunterPen.begin_fill()
                hunterPen.goto(xHunterPos + 143 * scale - 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.setheading(0)
                hunterPen.circle(19 * scale * flip, 185)
                hunterPen.setheading(270)
                hunterPen.goto(xHunterPos + 95 * scale - 92, yHunterPos + 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos + 95 * scale - 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.end_fill()
                hunterPen.penup()

            armUpLeft()
        elif flip == 1:
            def armUpRight():
                hunterPen.fillcolor("#f7cf89")
                hunterPen.goto(xHunterPos - 95 * scale + 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.pendown()
                hunterPen.begin_fill()
                hunterPen.goto(xHunterPos - 95 * scale + 92, yHunterPos + 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos - 68 * scale + 92, yHunterPos + 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos - 68 * scale + 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos - 95 * scale + 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.end_fill()

                hunterPen.fillcolor("#a13a01")
                hunterPen.begin_fill()
                hunterPen.goto(xHunterPos - 143 * scale + 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.setheading(180)
                hunterPen.circle(-19 * scale * flip, 185)
                hunterPen.goto(xHunterPos - 95 * scale + 92, yHunterPos + 19 * scale * flip + 80)
                hunterPen.goto(xHunterPos - 95 * scale + 92, yHunterPos - 19 * scale * flip + 80)
                hunterPen.end_fill()
                hunterPen.penup()

            armUpRight()

    # left shoe
    hunterPen.fillcolor("#c61821")
    hunterPen.goto(xHunterPos - 54 * scale * flip, yHunterPos + 37 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.setheading(-120 if flip == 1 else -60)
    hunterPen.circle(17.5 * scale * flip, 87)
    hunterPen.setheading(-35 if flip == 1 else -145)
    hunterPen.circle(35.0 * scale * flip, 75)
    hunterPen.circle(14.7 * scale * flip, 125)
    hunterPen.goto(xHunterPos - 54 * scale * flip, yHunterPos + 39 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # right shoe
    hunterPen.fillcolor("#c61821")
    hunterPen.goto(xHunterPos + 14 * scale * flip, yHunterPos + 39 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.setheading(-120 if flip == 1 else -60)
    hunterPen.circle(17.5 * scale * flip, 82)
    hunterPen.setheading(-35 if flip == 1 else -145)
    hunterPen.circle(35.0 * scale * flip, 70)
    hunterPen.circle(14.7 * scale * flip, 120)
    hunterPen.goto(xHunterPos + 14 * scale * flip, yHunterPos + 39 * scale)
    hunterPen.end_fill()
    hunterPen.penup()


def hunterSitting(xHunterPos, yHunterPos, scale):
    hunterPen.penup()
    hunterPen.pensize(3 * scale)

    # right shoe
    hunterPen.fillcolor("#c61821")
    hunterPen.goto(xHunterPos + 14 * scale + 40, yHunterPos + 39 * scale + 10)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.setheading(-120 + 90)  # -30 degrees
    hunterPen.circle(17.5 * scale, 82)
    hunterPen.setheading(-35 + 90)  # 55 degrees
    hunterPen.circle(35.0 * scale, 70)
    hunterPen.circle(14.7 * scale, 120)
    hunterPen.goto(xHunterPos + 14 * scale + 40, yHunterPos + 39 * scale + 10)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- BODY ---
    hunterPen.fillcolor("#15e109")
    hunterPen.goto(xHunterPos + 55 * scale, yHunterPos + 185 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 67 * scale, yHunterPos + 170 * scale)
    hunterPen.goto(xHunterPos + 64 * scale, yHunterPos + 62 * scale)
    hunterPen.goto(xHunterPos - 64 * scale, yHunterPos + 62 * scale)
    hunterPen.goto(xHunterPos - 67 * scale, yHunterPos + 170 * scale)
    hunterPen.goto(xHunterPos - 55 * scale, yHunterPos + 185 * scale)
    hunterPen.goto(xHunterPos + 55 * scale, yHunterPos + 185 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- PANTS ---
    hunterPen.fillcolor("#f6e208")
    hunterPen.goto(xHunterPos - 64 * scale, yHunterPos + 62 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 64 * scale, yHunterPos + 62 * scale)
    hunterPen.goto(xHunterPos + 49 * scale, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos - 49 * scale, yHunterPos + 34 * scale)
    hunterPen.goto(xHunterPos - 64 * scale, yHunterPos + 62 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # head
    hunterPen.fillcolor("#f7cf89")
    hunterPen.goto(xHunterPos + 69 * scale, yHunterPos + 263 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 66 * scale, yHunterPos + 230 * scale)
    hunterPen.setheading(-93.58)
    hunterPen.circle(-66 * scale, 163)
    hunterPen.goto(xHunterPos - 69 * scale, yHunterPos + 263 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- EYE ---
    hunterPen.pensize(5 * scale)
    hunterPen.goto(xHunterPos + 45 * scale, yHunterPos + 240 * scale)
    hunterPen.pendown()
    hunterPen.goto(xHunterPos + 45 * scale, yHunterPos + 220 * scale)
    hunterPen.pensize(3 * scale)
    hunterPen.penup()

    # --- HAT ---
    hunterPen.fillcolor("#15e109")
    hunterPen.goto(xHunterPos - 77 * scale, yHunterPos + 277 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 277 * scale)
    hunterPen.goto(xHunterPos + 77 * scale, yHunterPos + 263 * scale)
    hunterPen.goto(xHunterPos - 77 * scale, yHunterPos + 263 * scale)
    hunterPen.goto(xHunterPos - 77 * scale, yHunterPos + 277 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("#ff7b00")
    hunterPen.goto(xHunterPos - 55 * scale, yHunterPos + 277 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 55 * scale, yHunterPos + 277 * scale)
    hunterPen.goto(xHunterPos + 30 * scale, yHunterPos + 312 * scale)
    hunterPen.goto(xHunterPos - 30 * scale, yHunterPos + 312 * scale)
    hunterPen.goto(xHunterPos - 55 * scale, yHunterPos + 277 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    hunterPen.fillcolor("#f6e208")
    hunterPen.goto(xHunterPos - 30 * scale, yHunterPos + 312 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos + 30 * scale, yHunterPos + 312 * scale)
    hunterPen.goto(xHunterPos + 48 * scale, yHunterPos + 286.8 * scale)
    hunterPen.goto(xHunterPos - 48 * scale, yHunterPos + 286.8 * scale)
    hunterPen.goto(xHunterPos - 30 * scale, yHunterPos + 312 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # --- EAR ---
    hunterPen.fillcolor("#f7cf89")
    hunterPen.goto(xHunterPos - 21 * scale, yHunterPos + 230 * scale)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(xHunterPos - 7 * scale, yHunterPos + 230 * scale)
    hunterPen.goto(xHunterPos - 7 * scale, yHunterPos + 297 * scale)
    hunterPen.goto(xHunterPos - 21 * scale, yHunterPos + 297 * scale)
    hunterPen.goto(xHunterPos - 21 * scale, yHunterPos + 230 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # belt
    hunterPen.fillcolor("#efd742")
    hunterPen.goto(xHunterPos - 65.6 * scale, yHunterPos + 119.6 * scale)
    hunterPen.setheading(-30)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.circle(131.2 * scale, 60)
    hunterPen.goto(xHunterPos + 65.16 * scale, yHunterPos + 103.76 * scale)
    hunterPen.setheading(210)
    hunterPen.circle(-131.2 * scale, 60)
    hunterPen.goto(xHunterPos - 65.6 * scale, yHunterPos + 119.6 * scale)
    hunterPen.end_fill()
    hunterPen.penup()

    # left shoe
    hunterPen.fillcolor("#c61821")
    hunterPen.goto(xHunterPos - 54 * scale + 90, yHunterPos + 37 * scale - 5)
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.setheading(-120 + 90)  # -30 degrees
    hunterPen.circle(17.5 * scale, 87)
    hunterPen.setheading(-35 + 90)  # 55 degrees
    hunterPen.circle(35.0 * scale, 75)
    hunterPen.circle(14.7 * scale, 125)
    hunterPen.goto(xHunterPos - 54 * scale + 83, yHunterPos + 39 * scale - 5)
    hunterPen.end_fill()
    hunterPen.penup()


def sword(xSwordPos=0, ySwordPos=0, scale=1.0, swordHeading=0):
    def transform(x, y):
        x *= scale
        y *= scale
        rad = math.radians(swordHeading)
        xRot = x * math.cos(rad) - y * math.sin(rad)
        yRot = x * math.sin(rad) + y * math.cos(rad)
        return xRot + xSwordPos, yRot + ySwordPos

    hunterPen.pencolor("black")
    hunterPen.fillcolor("#299fdd")
    hunterPen.pensize(3 * scale)
    hunterPen.penup()
    hunterPen.goto(*transform(-10, 0))
    hunterPen.begin_fill()
    hunterPen.pendown()
    hunterPen.goto(*transform(10, 0))
    hunterPen.goto(*transform(10, 30))
    hunterPen.goto(*transform(-10, 30))
    hunterPen.goto(*transform(-10, 0))
    hunterPen.end_fill()

    hunterPen.penup()
    hunterPen.goto(*transform(-30, 30))
    hunterPen.begin_fill()
    hunterPen.pendown()
    hunterPen.goto(*transform(30, 30))
    hunterPen.goto(*transform(30, 50))
    hunterPen.goto(*transform(-30, 50))
    hunterPen.goto(*transform(-30, 30))
    hunterPen.end_fill()

    hunterPen.fillcolor("#efefef")
    hunterPen.penup()
    hunterPen.goto(*transform(-15, 50))
    hunterPen.begin_fill()
    hunterPen.pendown()
    hunterPen.goto(*transform(15, 50))
    hunterPen.goto(*transform(23, 150))
    hunterPen.goto(*transform(0, 178))
    hunterPen.goto(*transform(-23, 150))
    hunterPen.goto(*transform(-15, 50))
    hunterPen.end_fill()

    hunterPen.penup()
    hunterPen.goto(*transform(0, 178))
    hunterPen.pendown()
    hunterPen.goto(*transform(0, 50))


def tree_1(treeColor, trunkColor, xTreePos, yTreePos, scale):
    def transform(x0, y0):
        return xTreePos + x0 * scale, yTreePos + y0 * scale

    # --- Trunk ---
    treePen.penup()
    treePen.goto(transform(-2.5, -30))
    treePen.pencolor(trunkColor)
    treePen.fillcolor(trunkColor)
    treePen.setheading(0)
    treePen.begin_fill()
    treePen.pendown()
    for _ in range(2):
        treePen.forward(5 * scale)
        treePen.right(90)
        treePen.forward(25 * scale)
        treePen.right(90)
    treePen.end_fill()

    # --- Leaves ---
    treePen.penup()
    treePen.goto(transform(0, 50))
    treePen.pencolor(treeColor)
    treePen.fillcolor(treeColor)
    treePen.begin_fill()
    treePen.pendown()

    treePen.setheading(289)
    treePen.forward(62.5 * scale)

    treePen.setheading(200)
    treePen.forward(3.05 * scale)

    treePen.setheading(287)
    treePen.forward(12.5 * scale)

    treePen.setheading(200)
    treePen.forward(3 * scale)

    treePen.setheading(287)
    treePen.forward(12.5 * scale)

    treePen.goto(transform(0, -30))
    treePen.goto(transform(-22.02, -35.055))
    treePen.goto(transform(-18.3675, -23.1))

    treePen.setheading(160)
    treePen.forward(3 * scale)

    treePen.setheading(73)
    treePen.forward(12.5 * scale)

    treePen.setheading(160)
    treePen.forward(3 * scale)

    treePen.setheading(71)
    treePen.forward(62.5 * scale)

    treePen.end_fill()


def tree_2(treeColor, trunkColor, xTreePos, yTreePos, scale):
    def transform(x0, y0):
        return xTreePos + x0 * scale, yTreePos + y0 * scale

    treePen.setheading(0)
    treePen.pensize(5)
    treePen.pencolor(trunkColor)
    treePen.penup()
    treePen.goto(transform(0, 0))
    treePen.pendown()
    treePen.goto(transform(0, 100))
    treePen.penup()
    treePen.goto(transform(0, 60))
    treePen.pendown()
    treePen.pencolor(treeColor)
    treePen.fillcolor(treeColor)
    treePen.begin_fill()
    treePen.circle(40 * scale)
    treePen.end_fill()
    treePen.penup()
    treePen.pencolor(trunkColor)
    treePen.goto(transform(0, 20))
    treePen.pendown()
    treePen.goto(transform(40, 42))
    treePen.penup()
    treePen.pencolor(treeColor)
    treePen.fillcolor(treeColor)
    treePen.setheading(90)
    treePen.begin_fill()
    treePen.pendown()
    treePen.circle(10 * scale)
    treePen.end_fill()


def tree_3(treeColor, trunkColor, xTreePos, yTreePos, scale):
    def transform(x0, y0):
        return xTreePos + x0 * scale, yTreePos + y0 * scale

    treePen.pensize(5)
    treePen.penup()
    treePen.goto(transform(0, 50))
    treePen.setheading(0)
    treePen.pendown()
    treePen.pencolor(treeColor)
    treePen.fillcolor(treeColor)
    treePen.begin_fill()
    treePen.circle(60 * scale, 45)
    treePen.circle(45 * scale, 45)
    treePen.right(10)
    treePen.circle(150 * scale, 57)
    treePen.circle(20 * scale, 90)
    treePen.circle(150 * scale, 57)
    treePen.circle(60 * scale, 69)
    treePen.goto(transform(0, 50))
    treePen.end_fill()
    treePen.pencolor(trunkColor)
    treePen.penup()
    treePen.goto(transform(0, 0))
    treePen.pendown()
    treePen.goto(transform(0, 180))
    treePen.penup()
    treePen.goto(transform(0, 55))
    treePen.pendown()
    treePen.goto(transform(30, 65))
    treePen.penup()
    treePen.goto(transform(0, 80))
    treePen.pendown()
    treePen.goto(transform(-40, 90))
    treePen.penup()
    treePen.goto(transform(0, 115))
    treePen.pendown()
    treePen.goto(transform(50, 130))
    treePen.penup()


def tree_4(treeColor, trunkColor, outlineColor, xTreePos, yTreePos, scale):
    def transform(x0, y0):
        return xTreePos + x0 * scale, yTreePos + y0 * scale

    # leaf
    treePen.pencolor(outlineColor)
    treePen.fillcolor(treeColor)
    treePen.pensize(6)
    treePen.penup()
    treePen.goto(transform(12, 5))
    treePen.begin_fill()
    treePen.pendown()
    treePen.setheading(-120)
    treePen.circle(-20 * scale, 120)
    treePen.setheading(-140)
    treePen.circle(-25 * scale, 173)
    treePen.setheading(140)
    treePen.circle(-25 * scale, 173)
    treePen.setheading(60)
    treePen.circle(-35 * scale, 173)
    treePen.setheading(-30)
    treePen.circle(-27 * scale, 173)
    treePen.goto(transform(12, 5))
    treePen.end_fill()
    # branches
    treePen.pensize(3)
    treePen.pencolor(trunkColor)
    treePen.penup()
    treePen.goto(transform(-2, -10))
    treePen.pendown()
    treePen.goto(transform(-2, 55))
    treePen.penup()
    treePen.goto(transform(-2, 20))
    treePen.pendown()
    treePen.goto(transform(10, 30))
    treePen.penup()
    treePen.goto(transform(-2, 40))
    treePen.pendown()
    treePen.goto(transform(-10, 50))
    treePen.penup()
    treePen.goto(transform(0, -10))
    treePen.pendown()
    treePen.goto(transform(32, 45))
    treePen.penup()
    treePen.goto(transform(18, 17))
    treePen.pendown()
    treePen.goto(transform(30, 20))
    treePen.penup()
    treePen.goto(transform(27, 33))
    treePen.pendown()
    treePen.goto(transform(23, 40))
    treePen.penup()
    treePen.goto(transform(-4.8, -10))
    treePen.pendown()
    treePen.goto(transform(-31, 40))
    treePen.penup()
    treePen.goto(transform(-17, 15))
    treePen.pendown()
    treePen.goto(transform(-30, 18))
    treePen.penup()
    treePen.goto(transform(-20, 25))
    treePen.pendown()
    treePen.goto(transform(-17, 35))


def tree_5(treeColor, trunkColor, xTreePos, yTreePos, scale):
    def transform(x0, y0):
        return xTreePos + x0 * scale, yTreePos + y0 * scale

    # leaf
    treePen.pencolor(treeColor)
    treePen.fillcolor(treeColor)
    treePen.penup()
    treePen.goto(transform(0, 70))
    treePen.pendown()
    treePen.begin_fill()
    treePen.goto(transform(-40, 5))
    treePen.goto(transform(40, 5))
    treePen.end_fill()
    treePen.penup()
    treePen.pensize(3)
    treePen.pencolor(trunkColor)
    treePen.penup()
    treePen.goto(transform(-2, -10))
    treePen.pendown()
    treePen.goto(transform(-2, 55))
    treePen.penup()
    treePen.goto(transform(-2, 20))
    treePen.pendown()
    treePen.goto(transform(10, 30))
    treePen.penup()
    treePen.goto(transform(-2, 40))
    treePen.pendown()
    treePen.goto(transform(-10, 50))
    treePen.penup()


def rock_2(xRockPos, yRockPos, scale, rockColor):
    def transform(x, y):
        return xRockPos + x * scale, yRockPos + y * scale

    rockPen.penup()
    rockPen.fillcolor(rockColor)
    rockPen.goto(transform(-99, 20))
    rockPen.pendown()
    rockPen.begin_fill()
    rockPen.goto(transform(-90, 2.5))
    rockPen.goto(transform(-60, 0))
    rockPen.goto(transform(-40, 5))
    rockPen.goto(transform(-41, 25))
    rockPen.goto(transform(-69, 45))
    rockPen.goto(transform(-88, 41))
    rockPen.goto(transform(-99, 20))
    rockPen.end_fill()

    rockPen.penup()
    rockPen.pendown()
    rockPen.goto(transform(-94, 25))
    rockPen.goto(transform(-86, 22))
    rockPen.goto(transform(-65, 26))
    rockPen.goto(transform(-41, 25))
    rockPen.penup()
    rockPen.goto(transform(-86, 22))
    rockPen.pendown()
    rockPen.goto(transform(-80, 5))


def rock_1(xRockPos, yRockPos, scale, rockColor):
    def transform(x, y):
        return xRockPos + x * scale, yRockPos + y * scale

    rockPen.penup()
    rockPen.pensize(3 * scale)
    rockPen.fillcolor(rockColor)
    rockPen.goto(transform(-100, 40))
    rockPen.pendown()
    rockPen.begin_fill()
    rockPen.goto(transform(-70, 10))
    rockPen.goto(transform(0, 0))
    rockPen.goto(transform(50, 10))
    rockPen.goto(transform(95, 16))
    rockPen.goto(transform(105, 40))
    rockPen.goto(transform(100, 67))
    rockPen.goto(transform(40, 112))
    rockPen.goto(transform(4, 131))
    rockPen.goto(transform(-87, 80))
    rockPen.goto(transform(-100, 40))
    rockPen.end_fill()

    rockPen.penup()
    rockPen.goto(transform(1, 121))
    rockPen.pendown()
    rockPen.goto(transform(-20, 90))
    rockPen.goto(transform(-79, 80))
    rockPen.penup()
    rockPen.goto(transform(-20, 90))
    rockPen.pendown()
    rockPen.goto(transform(70, 60))


def sign(xSignPos, ySignPos, scale):
    def transform(x, y):
        return x * scale + xSignPos, y * scale + ySignPos

    signPen.pencolor("#deb488")
    signPen.fillcolor("#deb488")

    signPen.begin_fill()
    signPen.penup()
    signPen.goto(transform(-40, -150))
    signPen.pendown()
    signPen.setheading(90)
    for _ in range(2):
        signPen.forward(40 * scale)
        signPen.left(90)
        signPen.forward(7 * scale)
        signPen.left(90)
    signPen.end_fill()
    signPen.begin_fill()
    signPen.penup()
    signPen.goto(transform(-65, -135))
    signPen.pendown()
    signPen.setheading(0)
    signPen.forward(40 * scale)
    signPen.setheading(45)
    signPen.forward(14.1 * scale)
    signPen.setheading(135)
    signPen.forward(14.1 * scale)
    signPen.setheading(180)
    signPen.forward(40 * scale)
    signPen.left(90)
    signPen.forward(20 * scale)
    signPen.end_fill()


def fishSign(fishSignX, fishSignY, scale):
    fishSignPen.pensize(2.5 * scale)
    fishSignPen.color("#293e5c")
    fishSignPen.penup()
    fishSignPen.goto(fishSignX, fishSignY)

    fishSignPen.setheading(40)
    fishSignPen.pendown()
    fishSignPen.circle(-50 * scale, 100)

    fishSignPen.penup()
    fishSignPen.goto(fishSignX, fishSignY)
    fishSignPen.setheading(-40)
    fishSignPen.pendown()
    fishSignPen.circle(50 * scale, 100)

    fishSignPen.penup()
    fishSignPen.goto(fishSignX + 12 * scale, fishSignY)
    fishSignPen.dot(5 * scale)


def tentSign(tentSignX, tentSignY, scale):
    def transform(x, y):
        return tentSignX + x * scale, tentSignY + y * scale

    tentSignPen.hideturtle()
    tentSignPen.pensize(3 * scale)
    tentSignPen.pencolor("#253645")

    tentSignPen.penup()
    tentSignPen.goto(transform(-31, 0))
    tentSignPen.pendown()
    tentSignPen.goto(transform(31, 0))
    tentSignPen.goto(transform(-6, 58))

    tentSignPen.penup()
    tentSignPen.goto(transform(-31, 0))
    tentSignPen.pendown()
    tentSignPen.goto(transform(6, 58))

    tentSignPen.penup()
    tentSignPen.goto(transform(31, 0))
    tentSignPen.pendown()
    tentSignPen.goto(transform(36, 10))

    tentSignPen.penup()
    tentSignPen.goto(transform(-31, 0))
    tentSignPen.pendown()
    tentSignPen.goto(transform(-36, 10))

    tentSignPen.penup()
    tentSignPen.goto(transform(0, 50))
    tentSignPen.pendown()
    tentSignPen.goto(transform(0, 0))
    tentSignPen.penup()
    tentSignPen.goto(transform(0, 20))
    tentSignPen.pendown()
    tentSignPen.goto(transform(-11, 0))
    tentSignPen.goto(transform(-11, 20))
    tentSignPen.goto(transform(0, 20))


def sun(sunXPos, sunYPos):
    screen.colormode(255)
    for i in range(50):
        r, g, b = 255, 140 + (115 * i // 49), 0
        sunPen.color((r, g, b))
        sunPen.pensize(4)
        sunPen.penup()
        sunPen.goto(sunXPos, sunYPos - 50 + i)
        sunPen.pendown()
        sunPen.begin_fill()
        sunPen.circle(50 - i)
        sunPen.end_fill()

    sunPen.color("gold")
    sunPen.penup()
    sunPen.goto(sunXPos, sunYPos)
    for angle in range(0, 360, 15):
        sunPen.setheading(angle)
        sunPen.forward(60)
        sunPen.pendown()
        sunPen.forward(40)
        sunPen.penup()
        sunPen.backward(100)


def scene_1():
    # the path
    screen.bgcolor("skyblue")
    backgroundPen.penup()
    backgroundPen.pencolor("#41980a")
    backgroundPen.fillcolor("#41980a")
    backgroundPen.begin_fill()
    backgroundPen.goto(-500, -0)
    backgroundPen.goto(500, 0)
    backgroundPen.goto(500, -400)
    backgroundPen.goto(-500, -400)
    backgroundPen.goto(-500, 0)
    backgroundPen.end_fill()
    roadPen.penup()
    roadPen.pencolor("#5f3f09")
    roadPen.fillcolor("#8a6240")
    roadPen.penup()
    roadPen.goto(-500, -124)
    roadPen.pendown()
    roadPen.begin_fill()
    roadPen.circle(950, 13)
    roadPen.circle(2000, 5)
    roadPen.circle(-500, 25)
    roadPen.circle(900, 13)
    roadPen.circle(-900, 13)

    roadPen.goto(500, -115.64)
    roadPen.setheading(173)
    roadPen.pendown()
    roadPen.circle(2010, 17)

    roadPen.setheading(-5)
    roadPen.circle(-2010, 50)

    roadPen.goto(500, -350)
    roadPen.pendown()
    roadPen.setheading(160)
    roadPen.circle(2000, 29.8)
    roadPen.goto(-500, -124)
    roadPen.end_fill()
    tree_3("#66ae80", "#8e5a3f", -250, -80, 0.8)
    tree_1("#87b87c", "#8e5a3f", -450, 0, 2)
    rock_1(-300, -90, 0.4, "#535353")
    rock_2(-300, -90, 0.4, "#797979")
    tree_2("#a0c21e", "#8e5a3f", -350, -100, 1)
    tree_3("#66ae80", "#8e5a3f", -250, -80, 0.8)
    tree_3("#a3a72c", "#8e5a3f", -125, -50, 0.8)
    tree_2("#9ca964", "#8e5a3f", -10, -25, 1.25)
    tree_1("#dcdda4", "#8e5a3f", 100, 75, 1.8)
    tree_1("#58b767", "#8e5a3f", 150, 75, 1.8)
    tree_3("#a3a72c", "#8e5a3f", 230, -25, 0.8)
    tree_2("#9ca964", "#8e5a3f", 330, -25, 1.25)
    tree_2("#448f71", "#8e5a3f", 380, -25, 1.25)
    tree_3("#a0c31f", "#8e5a3f", 470, -25, 0.8)
    hunterFrontView(-400, -200, 0.6)
    sword(-350, -145, 0.6, -50)
    tree_4("#8cbb7b", "#766e41", "#8cbb7b", -300, -420, 2)
    tree_4("#428f70", "#8b5943", "#428f70", -450, -380, 1)
    rock_1(-100, -390, 1, "#535353")
    rock_2(-100, -390, 1, "#797979")
    tree_4("#a4aa2a", "#8b5943", "#a4aa2a", 100, -400, 1.5)
    tree_5("#4b8e6f", "#8e5a3f", 300, -400, 1.5)
    sign(350, 100, 2)
    fishSign(225, -150, 1)
    sign(360, 220, 1.7)
    tentSign(285, -10, 0.6)
    sun(-350, 280)


def nightSky():
    r1, g1, b1 = 0.043, 0.008, 0.094
    r2, g2, b2 = 37 / 225, 73 / 225, 161 / 225
    skyPen.penup()
    for y in range(400, -400, -2):
        colorChange = (400 - y) / 800

        r = r1 + (r2 - r1) * colorChange
        g = g1 + (g2 - g1) * colorChange
        b = b1 + (b2 - b1) * colorChange
        screen.colormode(1.0)
        skyPen.color((r, g, b))
        skyPen.goto(-500, y)
        skyPen.begin_fill()
        skyPen.pendown()
        skyPen.goto(500, y)
        skyPen.goto(500, y - 2)
        skyPen.goto(-500, y - 2)
        skyPen.goto(-500, y)
        skyPen.end_fill()
        skyPen.penup()


def moon():
    moonPen.penup()
    moonPen.pencolor("#f5ebd1")
    moonPen.fillcolor("#f5ebd1")
    moonPen.goto(0, 100)
    moonPen.pendown()
    moonPen.begin_fill()
    moonPen.circle(130)
    moonPen.end_fill()
    moonPen.penup()


starPos = []


def createStars():
    for _ in range(1000):
        x = random.randint(-500, 500)
        y = random.randint(-160, 800)
        size = random.random() * 3
        starPos.append((x, y, size))


def drawStars():
    starPen.clear()
    for x, y, baseSize in starPos:
        starPen.penup()
        starPen.goto(x, y)
        adjustedSize = baseSize * random.uniform(1.2, 2.5)
        starPen.pendown()
        starPen.dot(adjustedSize, "white")


def mountains():
    mountainsPen.penup()
    mountainsPen.color("#0b0d11")
    mountainsPen.goto(-500, -40)
    mountainsPen.setheading(0)
    mountainsPen.pendown()
    mountainsPen.begin_fill()

    # Outer mountain range
    for _ in range(10):
        mountainLength = 300
        mountainAngle = 50
        mountainsPen.left(mountainAngle)
        mountainsPen.forward(mountainLength)
        mountainsPen.right(2 * mountainAngle)
        mountainsPen.forward(mountainLength)
        mountainsPen.setheading(0)

    mountainsPen.goto(500, -400)
    mountainsPen.goto(-500, -400)
    mountainsPen.end_fill()

    # Inner mountain range
    mountainsPen.penup()
    mountainsPen.color("#1d2537")
    mountainsPen.goto(-450, -160)
    mountainsPen.setheading(0)
    mountainsPen.pendown()
    mountainsPen.begin_fill()

    for _ in range(10):
        mountainLength = 250
        mountainAngle = 25
        mountainsPen.left(mountainAngle)
        mountainsPen.forward(mountainLength)
        mountainsPen.right(2 * mountainAngle)
        mountainsPen.forward(mountainLength)
        mountainsPen.setheading(0)

    mountainsPen.goto(500, -400)
    mountainsPen.goto(-500, -400)
    mountainsPen.end_fill()


def tent(x, y, scale=1.0):
    tentPen.fillcolor("#2a3940")
    tentPen.penup()
    tentPen.goto(x, y)
    tentPen.pendown()
    tentPen.begin_fill()
    tentPen.goto(x + scale * -70, y + scale * 10)
    tentPen.setheading(77)
    tentPen.circle(scale * -245, 30)
    tentPen.goto(x + scale * 92.03, y + scale * 122.82)
    tentPen.goto(x, y)
    tentPen.end_fill()

    # Right outer tent
    tentPen.goto(x, y)
    tentPen.begin_fill()
    tentPen.goto(x + scale * 148, y)
    tentPen.setheading(101.5)
    tentPen.circle(scale * 300, 26)
    tentPen.setheading(-150)
    tentPen.circle(scale * 215, 42.9)
    tentPen.goto(x + scale * 149, y)
    tentPen.end_fill()

    # Right front tent flap (orange)
    tentPen.fillcolor("#d27317")
    tentPen.penup()
    tentPen.goto(x, y)
    tentPen.begin_fill()
    tentPen.pendown()
    tentPen.goto(x + scale * 140, y)
    tentPen.setheading(100)
    tentPen.circle(scale * 280, 26)
    tentPen.setheading(-150)
    tentPen.circle(scale * 200, 40)
    tentPen.goto(x, y)
    tentPen.end_fill()

    # Tent door (brown)
    tentPen.penup()
    tentPen.fillcolor("#4e3129")
    tentPen.goto(x + scale * 41, y + scale * 20)
    tentPen.pendown()
    tentPen.begin_fill()
    tentPen.setheading(90)
    tentPen.circle(scale * -40, 180)
    tentPen.goto(x + scale * 41, y + scale * 20)
    tentPen.end_fill()


def campfire(campfirexPos, campfireyPos, scale):
    rock_2(campfirexPos + 10 * scale, campfireyPos + 25 * scale, 0.7 * scale, "#76584f")
    rock_2(campfirexPos - 20 * scale, campfireyPos + 25 * scale, 0.7 * scale, "#76584f")
    rock_2(campfirexPos + 60 * scale, campfireyPos + 25 * scale, 0.8 * scale, "#76584f")
    rock_2(campfirexPos + 110 * scale, campfireyPos + 15 * scale, 0.8 * scale, "#76584f")
    rock_2(campfirexPos - 10 * scale, campfireyPos - 10 * scale, 0.8 * scale, "#76584f")
    rock_2(campfirexPos + 30 * scale, campfireyPos - 15 * scale, 0.7 * scale, "#76584f")
    rock_2(campfirexPos + 80 * scale, campfireyPos - 20 * scale, 0.9 * scale, "#76584f")
    rock_2(campfirexPos + 120 * scale, campfireyPos - 15 * scale, 0.8 * scale, "#76584f")

    campfirePen.penup()
    campfirePen.pensize(5 * scale)
    campfirePen.goto(campfirexPos - 75 * scale, campfireyPos)
    campfirePen.pendown()
    campfirePen.goto(campfirexPos - 75 * scale, campfireyPos + 191 * scale)
    campfirePen.penup()
    campfirePen.goto(campfirexPos - 82 * scale, campfireyPos + 191 * scale)
    campfirePen.pendown()
    campfirePen.goto(campfirexPos + 82 * scale, campfireyPos + 191 * scale)
    campfirePen.penup()
    campfirePen.goto(campfirexPos + 75 * scale, campfireyPos)
    campfirePen.pendown()
    campfirePen.goto(campfirexPos + 75 * scale, campfireyPos + 191 * scale)
    campfirePen.penup()

    campfirePen.pensize(2 * scale)
    campfirePen.goto(campfirexPos - 45 * scale, campfireyPos + 144 * scale)
    campfirePen.setheading(-90)
    campfirePen.pendown()
    campfirePen.fillcolor("#262521")
    campfirePen.begin_fill()
    campfirePen.circle(60 * scale, 45)
    campfirePen.circle(45 * scale, 90)
    campfirePen.circle(60 * scale, 45)
    campfirePen.goto(campfirexPos - 45 * scale, campfireyPos + 144 * scale)
    campfirePen.end_fill()

    campfirePen.setheading(90)
    campfirePen.circle(-60 * scale, 45)
    campfirePen.circle(-45 * scale, 90)
    campfirePen.circle(-60 * scale, 45)
    campfirePen.penup()

    campfirePen.penup()
    campfirePen.pensize(1)
    campfirePen.fillcolor("#ccb9a6")
    campfirePen.goto(-50 * scale + campfirexPos, 25 * scale + campfireyPos)
    campfirePen.pendown()
    campfirePen.setheading(110)
    campfirePen.begin_fill()
    campfirePen.circle(-15 * scale, 80)
    campfirePen.goto(60 * scale + campfirexPos, 15 * scale + campfireyPos)
    campfirePen.setheading(-60)
    campfirePen.circle(-50 * scale, 5)
    campfirePen.circle(-10 * scale, 500)
    campfirePen.goto(-50 * scale + campfirexPos, 25 * scale + campfireyPos)
    campfirePen.end_fill()
    campfirePen.penup()
    campfirePen.goto(-35 * scale + campfirexPos, 5 * scale + campfireyPos)
    campfirePen.begin_fill()
    campfirePen.pendown()
    campfirePen.circle(10 * scale, 620)
    campfirePen.goto(49 * scale + campfirexPos, 50 * scale + campfireyPos)
    campfirePen.setheading(95)
    campfirePen.circle(15 * scale, 80)
    campfirePen.goto(-44.96 * scale + campfirexPos, 4.13 * scale + campfireyPos)
    campfirePen.end_fill()


particleX = []
particleY = []
particleSize = []
particleLife = []


def spawnFlame(x, y, count=6):
    for _ in range(count):
        particleX.append(x + random.randint(-8, 8))  # slightly wider spread
        particleY.append(y)
        particleSize.append(random.uniform(0.6, 1.2))  # larger base size
        particleLife.append(32 + random.randint(0, 10))  # slightly longer life


def updateFlame():
    flamePen.clear()

    for i in range(len(particleX) - 1, -1, -1):
        x = particleX[i] + random.randint(-2, 2)
        y = particleY[i] + random.randint(2, 3)
        life = particleLife[i] - 1

        if life > 20:
            flamePen.color("red")
        elif life > 10:
            flamePen.color("orange")
        else:
            flamePen.color("gray")

        scale = max(0.1, particleSize[i] * life / 30)
        flamePen.goto(x, y)
        flamePen.shapesize(scale)
        flamePen.stamp()

        particleX[i] = x
        particleY[i] = y
        particleLife[i] = life

        if life <= 0:
            del particleX[i]
            del particleY[i]
            del particleSize[i]
            del particleLife[i]

    spawnFlame(150, -235, 6)



def scene_2():
    backgroundPen.penup()
    # sky and the moon
    nightSky()
    drawStars()
    moon()
    # mountains
    mountains()
    # the ground
    backgroundPen.pencolor("#885f2d")
    backgroundPen.fillcolor("#885f2d")
    backgroundPen.begin_fill()
    backgroundPen.goto(-500, -160)
    backgroundPen.pendown()
    backgroundPen.goto(500, -160)
    backgroundPen.goto(500, -400)
    backgroundPen.goto(-500, -400)
    backgroundPen.goto(-500, -160)
    backgroundPen.end_fill()
    tent(-310, -200, 1.5)
    campfire(150, -250, 1.25)


createStars()
spawnFlame(150, -235, 40)


def updateScene_2():
    if not _scene_2_active:
        return
    healthBarPen.clear()
    foodBarPen.clear()
    heartPen.clear()
    foodPen.clear()
    skyPen.clear()
    backgroundPen.clear()
    mountainsPen.clear()
    starPen.clear()
    rockPen.clear()
    tentPen.clear()
    campfirePen.clear()
    moonPen.clear()

    scene_2()  # static scene drawing
    draw_hunter_health_bar(150, 350)
    draw_hunter_food_bar(150, 280)
    updateFlame()  # keep flame animation running

    screen.update()

    screen.ontimer(updateScene_2, 100)


def showSleepMessage():
    if not _scene_2_active:
        return
    msgPen.clear()
    msgPen.penup()
    msgPen.goto(-200, 150)
    msgPen.color("black")
    msgPen.write("Sleep through the night...", font=("Arial", 16, "normal"))


def water(yWater):
    waterPen.clear()
    waterPen.penup()

    waveHeight = 10
    waveLength = 20

    waterPen.goto(-500, -200 + yWater)
    waterPen.pendown()
    waterPen.color("#1E90FF")
    waterPen.fillcolor("#1E90FF")
    waterPen.begin_fill()

    x = -500
    up = True

    while x <= 500:
        if up:
            waterPen.goto(x, -200 + waveHeight + yWater)
        else:
            waterPen.goto(x, -200 + yWater)
        up = not up
        x += waveLength

    waterPen.goto(500, -400)
    waterPen.goto(-500, -400)
    waterPen.goto(-500, -200 + yWater)
    waterPen.end_fill()

def bridge():
    bridgePen.pensize(1)
    bridgePen.penup()
    bridgePen.pencolor("black")
    bridgePen.fillcolor("#c07839")
    bridgePen.goto(-225, -148)
    bridgePen.pendown()
    bridgePen.begin_fill()
    bridgePen.goto(-225, -250)
    bridgePen.goto(-157, -250)
    bridgePen.goto(-157, -148)
    bridgePen.goto(-225, -148)
    bridgePen.end_fill()
    bridgePen.goto(-500, -70)
    bridgePen.pendown()
    bridgePen.begin_fill()
    bridgePen.goto(-130, -70)
    bridgePen.circle(-20, 90)
    bridgePen.setheading(-90)
    bridgePen.goto(-110, -150)
    bridgePen.circle(-20, 90)
    bridgePen.goto(-500, -170)
    bridgePen.goto(-500, -70)
    bridgePen.end_fill()
    bridgePen.penup()
    bridgePen.goto(-500, -86)
    bridgePen.pendown()
    bridgePen.goto(-110, -86)
    bridgePen.penup()


# arm & hand
def arm(xHunterPos, yHunterPos, scale, angle):
    hunterPen.pensize(scale * 3)

    def rotate(x, y):
        rad = math.radians(angle)
        cosA = math.cos(rad)
        sinA = math.sin(rad)
        return (
            xHunterPos + (x * scale) * cosA - (y * scale) * sinA,
            yHunterPos + (x * scale) * sinA + (y * scale) * cosA
        )

    hunterPen.penup()
    hunterPen.fillcolor("#f7cf89")
    hunterPen.goto(*rotate(-19, 95))
    hunterPen.pendown()
    hunterPen.begin_fill()
    hunterPen.goto(*rotate(19, 95))
    hunterPen.goto(*rotate(19, 68))
    hunterPen.goto(*rotate(-19, 68))
    hunterPen.goto(*rotate(-19, 95))
    hunterPen.end_fill()

    hunterPen.fillcolor("#a13a01")
    hunterPen.begin_fill()
    hunterPen.goto(*rotate(-19, 143))
    hunterPen.setheading(90 + angle)
    hunterPen.circle(-19 * scale, 185)
    hunterPen.setheading(0 + angle)
    hunterPen.goto(*rotate(19, 95))
    hunterPen.goto(*rotate(-19, 95))
    hunterPen.end_fill()
    hunterPen.penup()


def fishingRod(fishingrodX, fishingrodY, fishingrodHeading):
    fishingRodPen.clear()
    fishingRodPen.pencolor("#fdad21")
    fishingRodPen.fillcolor("#fdad21")
    fishingRodPen.penup()
    fishingRodPen.goto(fishingrodX, fishingrodY)
    fishingRodPen.setheading(fishingrodHeading)
    fishingRodPen.begin_fill()
    fishingRodPen.pendown()
    fishingRodPen.forward(365)
    fishingRodPen.right(90)
    fishingRodPen.forward(10)
    fishingRodPen.right(90)
    fishingRodPen.forward(270)
    fishingRodPen.left(90)
    fishingRodPen.forward(20)
    fishingRodPen.right(90)
    fishingRodPen.forward(40)
    fishingRodPen.right(90)
    fishingRodPen.forward(20)
    fishingRodPen.left(90)
    fishingRodPen.forward(55)
    fishingRodPen.right(90)
    fishingRodPen.forward(10)
    fishingRodPen.end_fill()
    fishingRodPen.right(90)
    fishingRodPen.forward(365)
    fishingRodPen.right(90)
    fishingRodPen.forward(10)
    fishingRodPen.penup()

fishColors = ["#dddddd", "#e80301", "#0eccf9", "#b37200", "#0bb200", "gold"]


def fish(fishSignX, fishSignY, scale, fishColor):
    fishSignPen.pensize(2.5 * scale)
    fishSignPen.pencolor(fishColor)
    fishSignPen.fillcolor(fishColor)
    fishSignPen.penup()
    fishSignPen.goto(fishSignX, fishSignY)

    fishSignPen.setheading(40 - 90)
    fishSignPen.pendown()
    fishSignPen.begin_fill()
    fishSignPen.circle(-50 * scale, 100)
    fishSignPen.setheading(0)

    fishSignPen.forward(26.60)

    fishSignPen.setheading(150)
    fishSignPen.pendown()
    fishSignPen.circle(-50 * scale, 100)
    print(fishSignPen.pos())
    fishSignPen.end_fill()
    fishSignPen.penup()
    fishSignPen.pencolor("black")
    fishSignPen.goto(fishSignX + 12 * scale - 10, fishSignY - 20)
    fishSignPen.dot(5 * scale)


def bucket():
    bridgePen.penup()
    bridgePen.pencolor("#d2d2d2")
    bridgePen.fillcolor("#d2d2d2")
    bridgePen.begin_fill()
    bridgePen.goto(-400, -70)
    bridgePen.pendown()
    bridgePen.goto(-335, -70)
    bridgePen.goto(-315, 16)
    bridgePen.goto(-420, 16)
    bridgePen.goto(-400, -70)
    bridgePen.end_fill()

    bridgePen.penup()
    bridgePen.pencolor("#c9c9cb")
    bridgePen.fillcolor("#c9c9cb")
    bridgePen.pensize(5)
    bridgePen.goto(-355, 0)
    bridgePen.pendown()
    bridgePen.setheading(-90)
    bridgePen.circle(30, 90)
    bridgePen.goto(-315, 16)

def animate():
    global yWater, waterDirection
    if not _fishing_animate_active:
        return
    water(yWater)

    yWater += waterDirection
    if yWater > 3 or yWater < -3:
        waterDirection *= -1

    screen.ontimer(animate, 200)

def scene_3():
    global currentFishingAttempts,  maxFishingPerDay
    screen.bgcolor("#c8e8f2")

    def drawInitialScene():
        bridge()
        arm(-155, -85, 0.8, 0)
        hunterSitting(-200, -97, 0.8)
        arm(-185, -100, 0.8, 0)
        bucket()
        water(yWater)
        msgPen.goto(0, 300)
        msgPen.write("Click to cast rod", align="center", font=("Arial", 20, "bold"))
        screen.update()

    def castRod():
        for i in range(60):
            hunterPen.clear()
            fishingRodPen.clear()
            arm(-70, 20, 0.8, 90)
            fishingRod(-150, 10, 140 - 2 * i)
            hunterSitting(-200, -97, 0.8)
            arm(-75, 10, 0.8, 90)
            screen.update()

    def fishCaught():
        msgPen.clear()
        msgPen.goto(0, 300)
        msgPen.write("Fish caught! (Click to collect)", align="center", font=("Arial", 20, "bold"))
        global caughtFishColor
        caughtFishColor = fishColors[random.randint(0, 5)]
        for i in range(340):
            screen.update()
            fishSignPen.clear()
            fish(200, -200 + i, 1, caughtFishColor)
            waterPen.clear()
            water(yWater)
        screen.onclick(collectFish)

    def collectFish(x, y):
        screen.onclick(None)
        msgPen.clear()
        msgPen.goto(0, 300)
        msgPen.write("Collecting fish...", align="center", font=("Arial", 20, "bold"))

        for i in range(30):
            hunterPen.clear()
            fishingRodPen.clear()
            fishSignPen.clear()
            arm(-70, 20, 0.8, 90)
            fishingRod(-150, 10, 85 + i)
            fish(fishingRodPen.xcor(), fishingRodPen.ycor(), 1, caughtFishColor)
            hunterSitting(-200, -97, 0.8)
            arm(-75, 10, 0.8, 90)
            screen.update()

        fishSignPen.clear()
        screen.update()

        msgPen.clear()
        msgPen.goto(0, 300)
        msgPen.write("Fish collected!", align="center", font=("Arial", 20, "bold"))
        screen.update()

        # Show effect of fish
        screen.ontimer(displayFishEffect, 1000)

    def displayFishEffect():
        msgPen.clear()
        msgPen.goto(0, 250)
        if caughtFishColor == "gold":
            msgPen.write("Gold fish! Increased attack!", align="center", font=("Arial", 16, "normal"))
        elif caughtFishColor == "purple":
            hunterPen.hp -= 1
            msgPen.write("Poisonous fish! -1 HP", align="center", font=("Arial", 16, "normal"))
        else:
            hunterPen.food += 0.5
            msgPen.write("Fish adds +0.5 food.", align="center", font=("Arial", 16, "normal"))

        screen.update()
        screen.ontimer(resetScene, 3000)

    def resetScene():
        hunterPen.clear()
        fishingRodPen.clear()
        fishSignPen.clear()
        waterPen.clear()
        msgPen.clear()
        bridgePen.clear()
        drawInitialScene()
        screen.onclick(onClick)

    def onClick(x, y):
        global currentFishingAttempts
        if currentFishingAttempts >= maxFishingPerDay:
            msgPen.clear()
            msgPen.goto(0, 300)
            msgPen.write("You've already fished twice today!\nTry again tomorrow.", align="center",
                         font=("Arial", 18, "bold"))
            screen.update()
            schedule_return_from_fishing()
            return

        currentFishingAttempts += 1
        screen.onclick(None)
        msgPen.clear()
        castRod()
        msgPen.goto(0, 300)
        msgPen.write("Waiting for fish...", align="center", font=("Arial", 20, "bold"))
        screen.update()
        screen.ontimer(fishCaught, 4000)

    drawInitialScene()
    screen.onclick(onClick)


def schedule_return_from_fishing():
    global _fishing_return_scheduled
    if _fishing_return_scheduled:
        return
    _fishing_return_scheduled = True
    screen.onclick(None)
    screen.ontimer(finish_fishing_day, 2200)


def finish_fishing_day():
    run_transition_card(
        "Leaving the river",
        f"Day {currentDay} — back to camp",
        begin_walk_from_fishing,
    )


def begin_walk_from_fishing():
    clear_fishing_scene()
    animate_walk_from_fish(after_return_to_hub)


def after_return_to_hub():
    clear_hub_scene()
    draw_hub_frame()
    on_day_activity_complete()



def grass(x, y):
    grassPen.penup()
    grassPen.pencolor("#5db53d")
    grassPen.fillcolor("#5db53d")
    grassPen.goto(x, y)
    grassPen.setheading(60)
    grassPen.pendown()

    grassPen.begin_fill()
    grassPen.forward(25)
    grassPen.setheading(-60)
    grassPen.forward(15)
    grassPen.setheading(60)
    grassPen.forward(20)
    grassPen.setheading(-70)
    grassPen.forward(28)
    grassPen.goto(x, y)
    grassPen.end_fill()


def nightPanda(xPosNightPanda=0, yPosNightPanda=0, scale=1, angle=0):
    radians = math.radians(angle)

    def transform(x, y):
        x *= scale
        y *= scale
        xr = x * math.cos(radians) - y * math.sin(radians)
        yr = x * math.sin(radians) + y * math.cos(radians)

        return xPosNightPanda + xr, yPosNightPanda + yr

    # Right foot
    nightPandaPen.pensize(5 * scale)
    nightPandaPen.fillcolor("#5d5d5d")
    nightPandaPen.penup()
    nightPandaPen.goto(transform(15, -58))
    nightPandaPen.setheading(110 + angle)
    nightPandaPen.begin_fill()
    nightPandaPen.pendown()
    nightPandaPen.circle(-20 * scale, 180)
    nightPandaPen.goto(transform(15, -58))
    nightPandaPen.end_fill()

    # Left foot
    nightPandaPen.fillcolor("#5d5d5d")
    nightPandaPen.penup()
    nightPandaPen.goto(transform(-17, -60))
    nightPandaPen.setheading(70 + angle)
    nightPandaPen.pendown()
    nightPandaPen.begin_fill()
    nightPandaPen.circle(20 * scale, 180)
    nightPandaPen.goto(transform(-17, -60))
    nightPandaPen.end_fill()

    # Body
    nightPandaPen.fillcolor("#5d5d5d")
    nightPandaPen.penup()
    nightPandaPen.goto(transform(0, -50))
    nightPandaPen.setheading(0 + angle)
    nightPandaPen.pendown()
    nightPandaPen.begin_fill()
    nightPandaPen.circle(50 * scale, 120)
    nightPandaPen.setheading(20 + angle)
    nightPandaPen.circle(15 * scale, 240)
    nightPandaPen.setheading(150 + angle)
    nightPandaPen.circle(50 * scale, 60)
    nightPandaPen.setheading(90 + angle)
    nightPandaPen.circle(15 * scale, 240)
    nightPandaPen.setheading(236 + angle)
    nightPandaPen.circle(50 * scale, 133)
    nightPandaPen.goto(transform(0, -50))
    nightPandaPen.end_fill()

    # Ears
    nightPandaPen.penup()
    nightPandaPen.fillcolor("#bec1be")
    nightPandaPen.goto(transform(18, 4))
    nightPandaPen.setheading(0 + angle)
    nightPandaPen.pendown()
    nightPandaPen.begin_fill()
    nightPandaPen.circle(10 * scale)
    nightPandaPen.end_fill()

    nightPandaPen.penup()
    nightPandaPen.goto(transform(-18, 4))
    nightPandaPen.setheading(0 + angle)
    nightPandaPen.pendown()
    nightPandaPen.begin_fill()
    nightPandaPen.circle(10 * scale)
    nightPandaPen.end_fill()

    # Face + Belly
    nightPandaPen.penup()
    nightPandaPen.goto(transform(-30, -5))
    nightPandaPen.pendown()
    nightPandaPen.begin_fill()
    nightPandaPen.goto(transform(-18, -5))
    nightPandaPen.goto(transform(-14, -16))
    nightPandaPen.goto(transform(-7, -5))
    nightPandaPen.goto(transform(7, -5))
    nightPandaPen.goto(transform(14, -16))
    nightPandaPen.goto(transform(18, -5))
    nightPandaPen.goto(transform(30, -5))
    nightPandaPen.setheading(-100 + angle)
    nightPandaPen.circle(-45 * scale, 35)
    nightPandaPen.goto(transform(9, -23))
    nightPandaPen.goto(transform(9, -33))
    nightPandaPen.goto(transform(-9, -33))
    nightPandaPen.goto(transform(-8, -23))
    nightPandaPen.goto(transform(-18, -28))
    nightPandaPen.setheading(140 + angle)
    nightPandaPen.circle(-45 * scale, 35)
    nightPandaPen.goto(transform(-30, -5))
    nightPandaPen.end_fill()


def scene_4(on_complete=None):
    global moveUp, moveDown, moveLeft, moveRight, _dreamland_on_complete, gameRunning
    global enemyList, spawnedEnemies, killedEnemies, healthScene4
    _dreamland_on_complete = on_complete
    gameRunning = True
    moveUp = moveDown = moveLeft = moveRight = False
    enemyList = []
    spawnedEnemies = 0
    killedEnemies = 0
    healthScene4 = MAX_HEALTH
    playerPositionScene4[0] = 0
    playerPositionScene4[1] = 0
    grassPen.clear()
    treePen.clear()
    nightPandaPen.clear()
    hunterPen.clear()
    healthBarPen.clear()
    msgPen.clear()
    screen.bgcolor("#97db61")
    for _ in range(15):
        x = random.randint(-500, 500)
        y = random.randint(-400, 400)
        grass(x, y)
    for _ in range(20):
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            x = random.randint(-500, 500)
            y = random.randint(300, 400)
        elif side == "bottom":
            x = random.randint(-500, 500)
            y = random.randint(-400, -300)
        elif side == "left":
            x = random.randint(-500, -400)
            y = random.randint(-400, 350)
        elif side == "right":
            x = random.randint(400, 500)
            y = random.randint(-350, 400)

        scale = random.uniform(0.6, 1.0)
        tree_4("#009a12", "saddlebrown", "#157516", x, y, scale)

    def drawPlayer():
        hunterPen.clear()
        x, y = playerPositionScene4
        scale = 0.5
        swordOut = time.time() - knifeShowTime < KNIFE_DURATION

        if playerDirection == "up":
            if swordOut:
                sword(-56 + x, 140 + y, scale, 0)
                hunterBackView(x, y, scale, True)
            else:
                sword(-56 + x, 60 + y, scale, 30)
                hunterBackView(x, y, scale, False)
        elif playerDirection == "down":
            hunterFrontView(x, y, scale)
            angle = -180 if swordOut else -50
            sword(55 + x, 60 + y, scale, angle)
        elif playerDirection == "left":
            hunterSideView(-1, x, y, scale, swordOut)
            angle = 90
            sx = -45 if swordOut else 2
            sy = 80 if swordOut else 43
            sword(sx + x, sy + y, scale, angle)
        elif playerDirection == "right":
            hunterSideView(1, x, y, scale, swordOut)
            angle = -90
            sx = 45 if swordOut else 2
            sy = 80 if swordOut else 43
            sword(sx + x, sy + y, scale, angle)

    def healthBar():
        bar_width = 200
        bar_height = 15

        # --- Player Health ---
        healthBarPen.clear()
        px, py = -450, 350
        current_player_hp = max(0, healthScene4)
        fill_width = (current_player_hp / MAX_HEALTH) * bar_width

        healthBarPen.penup()
        healthBarPen.goto(px, py)
        healthBarPen.fillcolor("#8251a8" if current_player_hp > 3 else "red")
        healthBarPen.begin_fill()
        for _ in range(2):
            healthBarPen.forward(fill_width)
            healthBarPen.right(90)
            healthBarPen.forward(bar_height)
            healthBarPen.right(90)
        healthBarPen.end_fill()

        healthBarPen.penup()
        healthBarPen.goto(px + bar_width + 5, py - bar_height)
        healthBarPen.setheading(0)
        healthBarPen.color("black")
        healthBarPen.write(f"HP: {current_player_hp} / {MAX_HEALTH}", font=("Arial", 12, "normal"))

    def moveUpKey():
        global moveUp, playerDirection
        moveUp = True
        playerDirection = "up"

    def stopMoveUp():
        global moveUp
        moveUp = False

    def moveDownKey():
        global moveDown, playerDirection
        moveDown = True
        playerDirection = "down"

    def stopMoveDown():
        global moveDown
        moveDown = False

    def moveLeftKey():
        global moveLeft, playerDirection
        moveLeft = True
        playerDirection = "left"

    def stopMoveLeft():
        global moveLeft
        moveLeft = False

    def moveRightKey():
        global moveRight, playerDirection
        moveRight = True
        playerDirection = "right"

    def stopMoveRight():
        global moveRight
        moveRight = False

    def attack(x, y):
        global lastAttackTime, knifeShowTime, enemyList, killedEnemies

        now = time.time()
        if now - lastAttackTime < ATTACK_COOLDOWN:
            return
        lastAttackTime = now
        knifeShowTime = now

        px, py = playerPositionScene4
        swordX, swordY = px, py

        if playerDirection == "up":
            swordY += 100
            swordX -= 50
            hitboxW, hitboxH = 60, 130
        elif playerDirection == "down":
            # swordY += 100
            swordX += 40
            hitboxW, hitboxH = 80, 100
        elif playerDirection == "left":
            swordY += 80
            swordX -= 40
            hitboxW, hitboxH = 120, 80
        elif playerDirection == "right":
            swordY += 80
            swordX += 40
            hitboxW, hitboxH = 100, 60
        else:
            hitboxW, hitboxH = 80, 120

        newEnemies = []
        enemyKilled = False

        for ex, ey, touchStart in enemyList:
            dx = abs(ex - swordX)
            dy = abs(ey - swordY)

            if not enemyKilled and dx <= hitboxW and dy <= hitboxH:
                killedEnemies += 1
                enemyKilled = True
                continue

            newEnemies.append([ex, ey, touchStart])

        enemyList[:] = newEnemies

        if killedEnemies == MAX_ENEMIES and not enemyList:
            screen.ontimer(lambda: gameOver(win=True), 300)

    def spawnEnemy():
        global enemyList, spawnedEnemies
        if len(enemyList) >= MAX_ENEMIES:
            return False

        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            x = random.randint(-1000 // 2, 1000 // 2)
            y = 800 // 2
        elif side == 'bottom':
            x = random.randint(-1000 // 2, 1000 // 2)
            y = -800 // 2
        elif side == 'left':
            x = -1000 // 2
            y = random.randint(-800 // 2, 800 // 2)
        else:
            x = 1000 // 2
            y = random.randint(-800 // 2, 800 // 2)

        enemyList.append([x, y, None])
        spawnedEnemies += 1
        return True

    def gameLoop():
        global playerPositionScene4, enemyList, healthScene4, lastSpawnTime, knifeShowTime, wobbleState, gameRunning
        if not gameRunning:
            return

        nightPandaPen.clear()

        if moveUp and playerPositionScene4[1] + PLAYER_RADIUS < HEIGHT // 2:
            playerPositionScene4[1] += PLAYER_SPEED
        if moveDown and playerPositionScene4[1] - PLAYER_RADIUS > -HEIGHT // 2:
            playerPositionScene4[1] -= PLAYER_SPEED
        if moveLeft and playerPositionScene4[0] - PLAYER_RADIUS > -WIDTH // 2:
            playerPositionScene4[0] -= PLAYER_SPEED
        if moveRight and playerPositionScene4[0] + PLAYER_RADIUS < WIDTH // 2:
            playerPositionScene4[0] += PLAYER_SPEED

        now = time.time()
        if now - lastSpawnTime > SPAWN_INTERVAL:
            spawned = 0
            while (spawned < 2 and
                   spawnedEnemies < MAX_ENEMIES and
                   len(enemyList) < MAX_ENEMIES):
                if spawnEnemy():
                    spawned += 1
                else:
                    break
            lastSpawnTime = now

        newEnemies = []
        for ex, ey, touchStart in enemyList:
            dx = playerPositionScene4[0] - ex
            dy = playerPositionScene4[1] - ey
            dist = math.hypot(dx, dy)
            if dist != 0:
                ex += ENEMY_SPEED * dx / dist
                ey += ENEMY_SPEED * dy / dist

            if dist < PLAYER_RADIUS + 10:
                if touchStart is None:
                    touchStart = now
                elif now - touchStart > 1:
                    healthScene4 -= 1
                    if healthScene4 <= 0:
                        gameOver(win=False)
                        return
                    touchStart = now
            else:
                touchStart = None
            newEnemies.append([ex, ey, touchStart])
        enemyList[:] = newEnemies

        global wobbleCounter, wobbleDirection, wobbleAngle

        wobbleCounter += 1
        if wobbleCounter >= wobbleSpeed:
            wobbleDirection *= -1
            wobbleCounter = 0

        wobbleAngle = 10 * wobbleDirection

        msgPen.clear()
        drawPlayer()

        for ex, ey, _ in enemyList:
            nightPanda(ex, ey, scale=0.6, angle=wobbleAngle)

        healthBar()
        screen.update()
        screen.ontimer(gameLoop, 30)

    def gameOver(win=False):
        global gameRunning
        gameRunning = False

        msgPen.clear()
        msgPen.penup()
        msgPen.goto(0, 0)
        msgPen.color("black")

        if win:
            msgPen.write("You Win!", align="center", font=("Arial", 30, "bold"))
        else:
            msgPen.write("Game Over! You Lose.", align="center", font=("Arial", 30, "bold"))

        screen.update()

        def leave_dreamland():
            clear_dreamland_scene()
            run_transition_card(
                "Leaving Dreamland",
                "You return to the forest paths...",
                _dreamland_on_complete,
            )

        if _dreamland_on_complete:
            screen.ontimer(leave_dreamland, 2200)

    screen.listen()
    screen.onkeypress(moveUpKey, "w")
    screen.onkeyrelease(stopMoveUp, "w")

    screen.onkeypress(moveDownKey, "s")
    screen.onkeyrelease(stopMoveDown, "s")

    screen.onkeypress(moveLeftKey, "a")
    screen.onkeyrelease(stopMoveLeft, "a")

    screen.onkeypress(moveRightKey, "d")
    screen.onkeyrelease(stopMoveRight, "d")
    screen.onclick(attack)

    gameLoop()

def scene_5():
    # the path
    nightSky()
    drawStars()
    moon()
    backgroundPen.penup()
    backgroundPen.pencolor("#41980a")
    backgroundPen.fillcolor("#41980a")
    backgroundPen.begin_fill()
    backgroundPen.goto(-500, -0)
    backgroundPen.goto(500, 0)
    backgroundPen.goto(500, -400)
    backgroundPen.goto(-500, -400)
    backgroundPen.goto(-500, 0)
    backgroundPen.end_fill()
    roadPen.penup()
    roadPen.pencolor("#5f3f09")
    roadPen.fillcolor("#8a6240")
    roadPen.penup()
    roadPen.goto(-500, -124)
    roadPen.pendown()
    roadPen.begin_fill()
    roadPen.goto(500, -124)
    roadPen.goto(500, -274)
    roadPen.goto(-500, -274)
    roadPen.end_fill()
    tree_3("#66ae80", "#8e5a3f", -250, -80, 0.8)
    tree_1("#87b87c", "#8e5a3f", -450, 0, 2)
    rock_1(-300, -90, 0.4, "#535353")
    rock_2(-300, -90, 0.4, "#797979")
    tree_2("#a0c21e", "#8e5a3f", -350, -100, 1)
    tree_3("#66ae80", "#8e5a3f", -250, -80, 0.8)
    tree_3("#a3a72c", "#8e5a3f", -125, -50, 0.8)
    tree_2("#9ca964", "#8e5a3f", -10, -25, 1.25)
    tree_1("#dcdda4", "#8e5a3f", 100, 75, 1.8)
    tree_1("#58b767", "#8e5a3f", 150, 75, 1.8)
    tree_3("#a3a72c", "#8e5a3f", 230, -25, 0.8)
    tree_2("#9ca964", "#8e5a3f", 330, -25, 1.25)
    tree_2("#448f71", "#8e5a3f", 380, -25, 1.25)
    tree_3("#a0c31f", "#8e5a3f", 470, -25, 0.8)
    hunterFrontView(-400, -200, 0.6)
    sword(-350, -145, 0.6, -50)
    tree_4("#8cbb7b", "#766e41", "#8cbb7b", -300, -420, 2)
    tree_4("#428f70", "#8b5943", "#428f70", -450, -380, 1)
    rock_1(-100, -390, 1, "#535353")
    rock_2(-100, -390, 1, "#797979")
    tree_4("#a4aa2a", "#8b5943", "#a4aa2a", 100, -400, 1.5)
    tree_5("#4b8e6f", "#8e5a3f", 300, -400, 1.5)
    skullPen.shape("Skull.gif")
    skullPen.penup()
    skullPen.goto(300, -190)
    skullPen.stamp()

    # Draw glowing eyes only if toggle is on
    if eye_glow_on:
        glowPen.penup()
        glowPen.fillcolor("#32cd32")  # bright green

        # Left eye
        glowPen.goto(290, -189)
        glowPen.dot(10)

        # Right eye
        glowPen.goto(310, -189)
        glowPen.dot(10)


def updateScene_5():
    global eye_glow_on
    if not _scene_5_active:
        return

    # Clear all pens
    skyPen.clear()
    backgroundPen.clear()
    mountainsPen.clear()
    starPen.clear()
    roadPen.clear()
    treePen.clear()
    rockPen.clear()
    moonPen.clear()
    skullPen.clear()
    hunterPen.clear()
    glowPen.clear()

    # Flip toggle to create flicker effect
    eye_glow_on = not eye_glow_on

    scene_5()
    screen.update()
    screen.ontimer(updateScene_5, 300)

hunterPen.hp = 10
hunterPen.food = 5
playerPosition = [0, -220]
bossPen.hp = 50
bossPosition = [400, 200]
bossDirection = "right"
swordOut = False

is_jumping = False
jump_velocity = 0
gravity = -0.3
jump_strength = 6
turn_number = 0

magic_balls = []
move_speed = 20
first_turn = True
game_over = False
healthBarPen = turtle.Turtle()
healthBarPen.hideturtle()
healthBarPen.penup()
healthBarPen.speed(0)

bossHealthBar = turtle.Turtle()
bossHealthBar.hideturtle()
bossHealthBar.penup()
bossHealthBar.speed(0)
game_over = False

def hulkArmDown(bossX, bossY, bossScale = 0.8, flip = 1):
    def transform(x, y):
        if flip == -1:
            x = -x
        return bossX + x * bossScale, bossY + (y + 85) * bossScale

    def flipHeading(deg):
        return 180 - deg if flip == -1 else deg

    bossPen.color("black")

    # Body
    bossPen.fillcolor("#08af71")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(*transform(-21, -94))
    bossPen.pendown()
    bossPen.goto(*transform(-86, -93))
    bossPen.setheading(flipHeading(309))
    bossPen.circle(8 * bossScale * flip, -149)
    bossPen.goto(*transform(-75, -72))
    bossPen.goto(*transform(-59, -72))
    bossPen.goto(*transform(-59, -63))
    bossPen.goto(*transform(-37, -37))
    bossPen.goto(*transform(-33, -3))
    bossPen.penup()
    bossPen.goto(*transform(37, -4))
    bossPen.pendown()
    bossPen.goto(*transform(36, -34))
    bossPen.goto(*transform(56, -60))
    bossPen.goto(*transform(57, -74))
    bossPen.goto(*transform(75, -71))
    bossPen.goto(*transform(74, -80))
    bossPen.goto(*transform(83, -80))
    bossPen.goto(*transform(86, -87))
    bossPen.goto(*transform(86, -94))
    bossPen.goto(*transform(9, -94))
    bossPen.goto(*transform(11, -73))
    bossPen.goto(*transform(6, -73))
    bossPen.goto(*transform(0, -59))
    bossPen.goto(*transform(-8, -74))
    bossPen.goto(*transform(-21, -74))
    bossPen.goto(*transform(-21, -94))
    bossPen.end_fill()

    # Arm
    bossPen.fillcolor("#08af71")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(*transform(-34, -5))
    bossPen.pendown()
    bossPen.goto(*transform(-45, -7))
    bossPen.goto(*transform(-59, -12))
    bossPen.setheading(flipHeading(167))
    bossPen.circle(14 * bossScale * flip, -143)
    bossPen.goto(*transform(-68, -40))
    bossPen.setheading(flipHeading(10))
    bossPen.circle(16 * bossScale * flip, -127)
    bossPen.goto(*transform(-85, 0))
    bossPen.setheading(flipHeading(259))
    bossPen.circle(45 * bossScale * flip, -92)
    bossPen.goto(*transform(48, 33))
    bossPen.setheading(flipHeading(178))
    bossPen.circle(39 * bossScale * flip, -89)
    bossPen.goto(*transform(86, -27))
    bossPen.setheading(flipHeading(78))
    bossPen.circle(22 * bossScale * flip, -120)
    bossPen.setheading(flipHeading(310))
    bossPen.circle(20 * bossScale * flip, -81)
    bossPen.goto(*transform(39, -3))
    bossPen.penup()
    bossPen.goto(*transform(-34, -5))
    bossPen.pendown()
    bossPen.end_fill()

    # Hair
    bossPen.fillcolor("black")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(*transform(-21, 34))
    bossPen.pendown()
    bossPen.setheading(flipHeading(20))
    bossPen.circle(13 * bossScale * flip, -115)
    bossPen.setheading(flipHeading(352))
    bossPen.circle(9 * bossScale * flip, -146)
    bossPen.setheading(flipHeading(345))
    bossPen.circle(8 * bossScale * flip, -172)
    bossPen.setheading(flipHeading(315))
    bossPen.circle(9 * bossScale * flip, -159)
    bossPen.setheading(flipHeading(245))
    bossPen.circle(13 * bossScale * flip, -111)
    bossPen.setheading(flipHeading(241))
    bossPen.circle(13 * bossScale * flip, -128)
    bossPen.setheading(flipHeading(234))
    bossPen.circle(9 * bossScale * flip, -146)
    bossPen.setheading(flipHeading(221))
    bossPen.circle(6 * bossScale * flip, -154)
    bossPen.setheading(flipHeading(203))
    bossPen.circle(9 * bossScale * flip, -177)
    bossPen.setheading(flipHeading(165))
    bossPen.circle(8 * bossScale * flip, -180)
    bossPen.goto(*transform(-21, 34))
    bossPen.end_fill()

    # Face
    bossPen.fillcolor("#08af71")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(*transform(-21, 34))
    bossPen.pendown()
    bossPen.setheading(flipHeading(315))
    bossPen.circle(42 * bossScale * flip, 90)
    bossPen.setheading(flipHeading(17))
    bossPen.circle(14 * bossScale * flip, 91)
    bossPen.goto(*transform(47, 71))
    bossPen.setheading(flipHeading(6))
    bossPen.circle(33 * bossScale * flip, -39)
    bossPen.setheading(flipHeading(59))
    bossPen.circle(8 * bossScale * flip, -134)
    bossPen.setheading(flipHeading(47))
    bossPen.circle(10 * bossScale * flip, -95)
    bossPen.setheading(flipHeading(45))
    bossPen.circle(32 * bossScale * flip, -32)
    bossPen.goto(*transform(-22, 57))
    bossPen.goto(*transform(-28, 59))
    bossPen.setheading(flipHeading(183))
    bossPen.circle(8 * bossScale * flip, 166)
    bossPen.goto(*transform(-23, 42))
    bossPen.goto(*transform(-22, 32))
    bossPen.goto(*transform(-21, 34))
    bossPen.end_fill()

    # Eyes
    bossPen.pensize(8)
    bossPen.color("white")
    bossPen.penup()
    bossPen.goto(*transform(-3, 60))
    bossPen.pendown()
    bossPen.goto(*transform(-3, 47))
    bossPen.penup()
    bossPen.goto(*transform(29, 62))
    bossPen.pendown()
    bossPen.goto(*transform(29, 51))

    bossPen.color("black")
    bossPen.penup()
    bossPen.goto(*transform(-9, 61))
    bossPen.pendown()
    bossPen.goto(*transform(5, 66))
    bossPen.goto(*transform(11, 63))
    bossPen.goto(*transform(4, 66))
    bossPen.goto(*transform(3, 47))
    bossPen.penup()
    bossPen.goto(*transform(18, 61))
    bossPen.pendown()
    bossPen.goto(*transform(27, 66))
    bossPen.goto(*transform(31, 64))
    bossPen.goto(*transform(33, 62))
    bossPen.goto(*transform(24, 64))
    bossPen.goto(*transform(24, 48))

    # Mouth
    bossPen.pensize(2)
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(*transform(11, 39))
    bossPen.pendown()
    bossPen.setheading(flipHeading(135))
    bossPen.circle(4 * bossScale * flip, 123)
    bossPen.goto(*transform(4, 36))
    bossPen.goto(*transform(6, 32))
    bossPen.goto(*transform(11, 32))
    bossPen.goto(*transform(18, 32))
    bossPen.setheading(flipHeading(340))
    bossPen.circle(4 * bossScale * flip, 123)
    bossPen.goto(*transform(15, 43))
    bossPen.goto(*transform(11, 42))
    bossPen.goto(*transform(11, 39))
    bossPen.end_fill()

    # Pants
    bossPen.pensize(6)
    bossPen.fillcolor("#8e3ec3")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(*transform(-36, -35))
    bossPen.pendown()
    bossPen.goto(*transform(-58, -60))
    bossPen.goto(*transform(-58, -67))
    bossPen.penup()
    bossPen.goto(*transform(-18, -71))
    bossPen.pendown()
    bossPen.goto(*transform(-11, -71))
    bossPen.goto(*transform(-1, -57))
    bossPen.goto(*transform(6, -71))
    bossPen.goto(*transform(13, -73))
    bossPen.penup()
    bossPen.goto(*transform(57, -63))
    bossPen.pendown()
    bossPen.goto(*transform(36, -36))
    bossPen.penup()
    bossPen.goto(*transform(-36, -35))
    bossPen.end_fill()

    bossPen.color("#355E3B")
    bossPen.penup()
    bossPen.goto(transform(-27, -7))
    bossPen.pendown()
    bossPen.goto(transform(35, -7))
    bossPen.penup()
    bossPen.goto(transform(-23, 21))
    bossPen.pendown()
    bossPen.seth(flipHeading(287))
    bossPen.circle(18 * bossScale * flip, 98)
    bossPen.penup()
    bossPen.goto(transform(44, 26))
    bossPen.pendown()
    bossPen.seth(flipHeading(59))
    bossPen.circle(28 * bossScale * flip, -74)
    bossPen.penup()
    bossPen.goto(transform(6, 5))
    bossPen.pendown()
    bossPen.goto(transform(6, -27))



def hulkArmUp(bossX, bossY, bossScale=1, flip=1):
    bossPen.pensize(6)
    def transform(x, y):
        if flip == -1:
            x = -x
        return bossX + x * bossScale, bossY + (y + 85) * bossScale

    def flipHeading(deg):
        if flip == -1:
            return 180 - deg
        else:
            return deg

    bossPen.color("black")

    ## body
    bossPen.fillcolor("#08af71")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(transform(-21, -94))
    bossPen.pendown()
    bossPen.goto(transform(-86, -93))
    bossPen.seth(flipHeading(309))
    bossPen.circle(8 * bossScale * flip, -149)
    bossPen.goto(transform(-75, -72))
    bossPen.goto(transform(-59, -72))
    bossPen.goto(transform(-59, -63))
    bossPen.goto(transform(-37, -37))
    bossPen.goto(transform(-33, -3))
    bossPen.penup()
    bossPen.goto(transform(37, -4))
    bossPen.pendown()
    bossPen.goto(transform(36, -34))
    bossPen.goto(transform(56, -60))
    bossPen.goto(transform(57, -74))
    bossPen.goto(transform(75, -71))
    bossPen.goto(transform(74, -80))
    bossPen.goto(transform(83, -80))
    bossPen.goto(transform(86, -87))
    bossPen.goto(transform(86, -94))
    bossPen.goto(transform(9, -94))
    bossPen.goto(transform(11, -73))
    bossPen.goto(transform(6, -73))
    bossPen.goto(transform(0, -59))
    bossPen.goto(transform(-8, -74))
    bossPen.goto(transform(-21, -74))
    bossPen.goto(transform(-21, -94))
    bossPen.end_fill()

    ## arm1
    bossPen.fillcolor("#08af71")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(transform(-36, -3))
    bossPen.pendown()
    bossPen.seth(flipHeading(24))
    bossPen.circle(37 * bossScale * flip, -95)
    bossPen.goto(transform(-87, 87))
    bossPen.seth(flipHeading(244))
    bossPen.circle(18 * bossScale * flip, -117)
    bossPen.seth(flipHeading(129))
    bossPen.circle(17 * bossScale * flip, -114)
    bossPen.goto(transform(-70, 61))
    bossPen.goto(transform(-61, 62))
    bossPen.goto(transform(-60, 38))
    bossPen.seth(flipHeading(333))
    bossPen.circle(38 * bossScale * flip, 53)
    bossPen.goto(transform(41, 34))
    bossPen.seth(flipHeading(340))
    bossPen.circle(24 * bossScale * flip, 73)
    bossPen.goto(transform(69, 60))
    bossPen.goto(transform(74, 60))
    bossPen.goto(transform(68, 60))
    bossPen.seth(flipHeading(340))
    bossPen.circle(16 * bossScale * flip, -136)
    bossPen.seth(flipHeading(222))
    bossPen.circle(17 * bossScale * flip, -106)
    bossPen.goto(transform(95, 24))
    bossPen.seth(flipHeading(97))
    bossPen.circle(34 * bossScale * flip, -142)
    bossPen.penup()
    bossPen.goto(transform(-36, -3))
    bossPen.end_fill()

    ## hair
    bossPen.fillcolor("black")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(transform(-21, 34))
    bossPen.pendown()
    bossPen.seth(flipHeading(20))
    bossPen.circle(13 * bossScale * flip, -115)
    bossPen.seth(flipHeading(352))
    bossPen.circle(9 * bossScale * flip, -146)
    bossPen.seth(flipHeading(345))
    bossPen.circle(8 * bossScale * flip, -172)
    bossPen.seth(flipHeading(315))
    bossPen.circle(9 * bossScale * flip, -159)
    bossPen.seth(flipHeading(245))
    bossPen.circle(13 * bossScale * flip, -111)
    bossPen.seth(flipHeading(241))
    bossPen.circle(13 * bossScale * flip, -128)
    bossPen.seth(flipHeading(234))
    bossPen.circle(9 * bossScale * flip, -146)
    bossPen.seth(flipHeading(221))
    bossPen.circle(6 * bossScale * flip, -154)
    bossPen.seth(flipHeading(203))
    bossPen.circle(9 * bossScale * flip, -177)
    bossPen.seth(flipHeading(165))
    bossPen.circle(8 * bossScale * flip, -180)
    bossPen.goto(transform(-21, 34))
    bossPen.end_fill()

    # face
    bossPen.fillcolor("#08af71")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(transform(-21, 34))
    bossPen.pendown()
    bossPen.seth(flipHeading(315))
    bossPen.circle(42 * bossScale * flip, 90)
    bossPen.seth(flipHeading(17))
    bossPen.circle(14 * bossScale * flip, 91)
    bossPen.goto(transform(47, 71))
    bossPen.seth(flipHeading(6))
    bossPen.circle(33 * bossScale * flip, -39)
    bossPen.seth(flipHeading(59))
    bossPen.circle(8 * bossScale * flip, -134)
    bossPen.seth(flipHeading(47))
    bossPen.circle(10 * bossScale * flip, -95)
    bossPen.seth(flipHeading(45))
    bossPen.circle(32 * bossScale * flip, -32)
    bossPen.goto(transform(-22, 57))
    bossPen.goto(transform(-28, 59))
    bossPen.seth(flipHeading(183))
    bossPen.circle(8 * bossScale * flip, 166)
    bossPen.goto(transform(-23, 42))
    bossPen.goto(transform(-22, 32))
    bossPen.goto(transform(-21, 34))
    bossPen.end_fill()

    # eye
    bossPen.pensize(8)
    bossPen.color("white")
    bossPen.penup()
    bossPen.goto(transform(-3, 60))
    bossPen.pendown()
    bossPen.goto(transform(-3, 47))
    bossPen.penup()
    bossPen.goto(transform(29, 62))
    bossPen.pendown()
    bossPen.goto(transform(29, 51))

    bossPen.color("black")
    bossPen.penup()
    bossPen.goto(transform(-9, 61))
    bossPen.pendown()
    bossPen.goto(transform(5, 66))
    bossPen.goto(transform(11, 63))
    bossPen.goto(transform(4, 66))
    bossPen.goto(transform(3, 47))
    bossPen.penup()
    bossPen.goto(transform(18, 61))
    bossPen.pendown()
    bossPen.goto(transform(27, 66))
    bossPen.goto(transform(31, 64))
    bossPen.goto(transform(33, 62))
    bossPen.goto(transform(24, 64))
    bossPen.goto(transform(24, 48))

    bossPen.pensize(2)
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(transform(11, 39))
    bossPen.pendown()
    bossPen.seth(flipHeading(135))
    bossPen.circle(4 * bossScale * flip, 123)
    bossPen.goto(transform(4, 36))
    bossPen.goto(transform(6, 32))
    bossPen.goto(transform(11, 32))
    bossPen.goto(transform(18, 32))
    bossPen.seth(flipHeading(340))
    bossPen.circle(4 * bossScale * flip, 165)
    bossPen.goto(transform(15, 43))
    bossPen.goto(transform(11, 42))
    bossPen.goto(transform(11, 39))
    bossPen.end_fill()

    ## pants
    bossPen.pensize(6)
    bossPen.fillcolor("#8e3ec3")
    bossPen.begin_fill()
    bossPen.penup()
    bossPen.goto(transform(-36, -35))
    bossPen.pendown()
    bossPen.goto(transform(-58, -60))
    bossPen.goto(transform(-58, -67))
    bossPen.penup()
    bossPen.goto(transform(-18, -71))
    bossPen.pendown()
    bossPen.goto(transform(-11, -71))
    bossPen.goto(transform(-1, -57))
    bossPen.goto(transform(6, -71))
    bossPen.goto(transform(13, -73))
    bossPen.penup()
    bossPen.goto(transform(57, -63))
    bossPen.pendown()
    bossPen.goto(transform(36, -36))
    bossPen.penup()
    bossPen.goto(transform(-36, -35))
    bossPen.end_fill()

    bossPen.color("#355E3B")
    bossPen.penup()
    bossPen.goto(transform(-27, -7))
    bossPen.pendown()
    bossPen.goto(transform(35, -7))
    bossPen.penup()
    bossPen.goto(transform(-23, 21))
    bossPen.pendown()
    bossPen.seth(flipHeading(287))
    bossPen.circle(18 * bossScale * flip, 98)
    bossPen.penup()
    bossPen.goto(transform(44, 26))
    bossPen.pendown()
    bossPen.seth(flipHeading(59))
    bossPen.circle(28 * bossScale * flip, -74)
    bossPen.penup()
    bossPen.goto(transform(6, 5))
    bossPen.pendown()
    bossPen.goto(transform(6, -27))

def draw_hunter_food_bar(px, py):
    bar_width = 100
    bar_height = 15
    player_max_food = 5

    # --- Player Food ---
    foodBarPen.clear()
    current_player_food = max(0, hunterPen.food)
    fill_width = (current_player_food / player_max_food) * bar_width

    foodPen.penup()
    foodPen.goto(px - 40, py)
    foodPen.stamp()

    foodBarPen.penup()
    foodBarPen.goto(px, py)
    foodBarPen.fillcolor("orange" if current_player_food > 2 else "red")
    foodBarPen.begin_fill()
    for _ in range(2):
        foodBarPen.forward(fill_width)
        foodBarPen.right(90)
        foodBarPen.forward(bar_height)
        foodBarPen.right(90)
    foodBarPen.end_fill()

    foodBarPen.penup()
    foodBarPen.goto(px + bar_width + 10, py - bar_height)
    foodBarPen.setheading(0)
    foodBarPen.color("white")
    foodBarPen.write(f"Food: {current_player_food} / {player_max_food}", font=("Arial", 12, "normal"))

def draw_hunter_health_bar(px, py):
    global game_over

    bar_width = 200
    bar_height = 15
    player_max_hp = 10

    # --- Player Health ---
    healthBarPen.clear()
    # px, py = -400, 350
    current_player_hp = max(0, hunterPen.hp)
    fill_width = (current_player_hp / player_max_hp) * bar_width
    heartPen.penup()
    heartPen.goto(px - 50, 350)
    heartPen.stamp()
    heartPen.penup()
    healthBarPen.penup()
    healthBarPen.goto(px, py)
    healthBarPen.fillcolor("lime" if current_player_hp > 3 else "red")
    healthBarPen.begin_fill()
    for _ in range(2):
        healthBarPen.forward(fill_width)
        healthBarPen.right(90)
        healthBarPen.forward(bar_height)
        healthBarPen.right(90)
    healthBarPen.end_fill()

    healthBarPen.penup()
    healthBarPen.goto(px + bar_width + 10, py - bar_height)
    healthBarPen.setheading(0)
    healthBarPen.color("white")
    healthBarPen.write(f"HP: {current_player_hp} / {player_max_hp}", font=("Arial", 12, "normal"))

def draw_boss_health_bar(bx, by):
    global game_over

    bar_width = 200
    bar_height = 15
    boss_max_hp = 50

    # --- Boss Health ---
    bossHealthBar.clear()
    # bx, by = 250, 350
    current_boss_hp = max(0, bossPen.hp)
    boss_fill_width = (current_boss_hp / boss_max_hp) * bar_width

    bossHealthBar.penup()
    bossHealthBar.goto(bx, by)
    bossHealthBar.fillcolor("orange" if current_boss_hp > 20 else "red")
    bossHealthBar.begin_fill()
    for _ in range(2):
        bossHealthBar.forward(boss_fill_width)
        bossHealthBar.right(90)
        bossHealthBar.forward(bar_height)
        bossHealthBar.right(90)
    bossHealthBar.end_fill()

    bossHealthBar.penup()
    bossHealthBar.goto(bx + bar_width - 300, by - bar_height)
    bossHealthBar.setheading(0)
    bossHealthBar.color("white")
    bossHealthBar.write(f"Boss: {current_boss_hp} / {boss_max_hp}", font=("Arial", 12, "normal"))
def scene_6():
    global moveLeft, moveRight, playerDirection
    moveLeft = False
    moveRight = False
    playerDirection = "right"
    screen.bgcolor("#f89387")
    backgroundPen.pencolor("#8d1e06")
    backgroundPen.fillcolor("#8d1e06")
    backgroundPen.penup()
    backgroundPen.goto(-500, 400)
    backgroundPen.pendown()
    backgroundPen.begin_fill()
    backgroundPen.goto(-462, 265)
    backgroundPen.goto(-430, 400)
    backgroundPen.goto(-405, 355)
    backgroundPen.goto(-376.5, 325)
    backgroundPen.goto(-367.5, 320)
    backgroundPen.goto(-357.5, 305)
    backgroundPen.goto(-340, 337)
    backgroundPen.goto(-339.5, 351.5)
    backgroundPen.goto(-331, 360)
    backgroundPen.goto(-327, 377.5)
    backgroundPen.goto(-310, 300)
    backgroundPen.goto(-286.5, 277.5)
    backgroundPen.goto(-270, 313)
    backgroundPen.goto(-267.5, 320)
    backgroundPen.goto(-240, 350)
    backgroundPen.goto(-210, 329)
    backgroundPen.goto(-209, 324)
    backgroundPen.goto(-190, 305)
    backgroundPen.goto(-170, 329)
    backgroundPen.goto(-162.5, 357.5)
    backgroundPen.goto(-150, 400)
    backgroundPen.goto(10, 325)
    backgroundPen.goto(13, 307.5)
    backgroundPen.goto(19, 300)
    backgroundPen.goto(24.5, 263.5)
    backgroundPen.goto(35, 282.5)
    backgroundPen.goto(42.5, 347)
    backgroundPen.goto(72.5, 380)
    backgroundPen.goto(76.5, 375)
    backgroundPen.goto(92.5, 275)
    backgroundPen.goto(106.5, 247.5)
    backgroundPen.goto(132.5, 250)
    backgroundPen.goto(142.5, 277)
    backgroundPen.goto(172.5, 254)
    backgroundPen.goto(204, 321.5)
    backgroundPen.goto(215, 302.5)
    backgroundPen.goto(240, 255)
    backgroundPen.goto(257.5, 307.5)
    backgroundPen.goto(290, 282.5)
    backgroundPen.goto(305, 235)
    backgroundPen.goto(328.5, 282.5)
    backgroundPen.goto(332.5, 279)
    backgroundPen.goto(342.5, 305)
    backgroundPen.goto(354, 275)
    backgroundPen.goto(367.5, 260)
    backgroundPen.goto(375, 290)
    backgroundPen.goto(382.5,304)
    backgroundPen.goto(400, 285)
    backgroundPen.goto(412.5, 279)
    backgroundPen.goto(429, 250)
    backgroundPen.goto(440, 234)
    backgroundPen.goto(464, 250)
    backgroundPen.goto(477.5, 270)
    backgroundPen.goto(476.5, 317.5)
    backgroundPen.goto(500, 310)
    backgroundPen.goto(500, 400)
    backgroundPen.goto(-500, 400)
    backgroundPen.end_fill()

    backgroundPen.penup()
    backgroundPen.pencolor("#431600")
    backgroundPen.fillcolor("#431600")
    backgroundPen.goto(-500, 300)
    backgroundPen.pendown()
    backgroundPen.begin_fill()
    backgroundPen.goto(-450, 325)
    backgroundPen.goto(-439, 275)
    backgroundPen.goto(-430, 260)
    backgroundPen.goto(-405, 200)
    backgroundPen.goto(-360, 369)
    backgroundPen.goto(-340, 337)
    backgroundPen.goto(-303, 360)
    backgroundPen.goto(-267.5, 330)
    backgroundPen.goto(-270, 313)
    backgroundPen.goto(-237.5, 320)
    backgroundPen.goto(-240, 305)
    backgroundPen.goto(-220, 310)
    backgroundPen.goto(-197, 252.5)
    backgroundPen.goto(-170, 329)
    backgroundPen.goto(-126.5, 320)
    backgroundPen.goto(-125, 292.5)
    backgroundPen.goto(-112.5, 284)
    backgroundPen.goto(-100, 240)
    backgroundPen.goto(-87.5, 280)
    backgroundPen.goto(-77.5, 290)
    backgroundPen.goto(-70, 315)
    backgroundPen.goto(-28, 334)
    backgroundPen.goto(-30, 317.5)
    backgroundPen.goto(-2, 330)
    backgroundPen.goto(3, 315)
    backgroundPen.goto(30, 340)
    backgroundPen.goto(42.5, 347)
    backgroundPen.goto(53, 347)
    backgroundPen.goto(55, 330)
    backgroundPen.goto(59, 329)
    backgroundPen.goto(70, 320)
    backgroundPen.goto(72, 291)
    backgroundPen.goto(93, 316.5)
    backgroundPen.goto(107.5, 325)
    backgroundPen.goto(104, 291)
    backgroundPen.goto(111, 283)
    backgroundPen.goto(122.5, 228)
    backgroundPen.goto(151.5, 310)
    backgroundPen.goto(180, 356.5)
    backgroundPen.goto(240, 342)
    backgroundPen.goto(300, 360)
    backgroundPen.goto(295, 329)
    backgroundPen.goto(297.5, 309)
    backgroundPen.goto(310, 272.5)
    backgroundPen.goto(340, 340)
    backgroundPen.goto(350, 327.5)
    backgroundPen.goto(404.5, 312.5)
    backgroundPen.goto(408.5, 225)
    backgroundPen.goto(440, 286.5)
    backgroundPen.goto(500, 287.5)
    backgroundPen.goto(500, 400)
    backgroundPen.goto(-500, 400)
    backgroundPen.goto(-500, 300)
    backgroundPen.end_fill()

    def check_game_over():
        global game_over
        current_player_hp = max(0, hunterPen.hp)
        current_boss_hp = max(0, bossPen.hp)

        if not game_over:
            if current_player_hp <= 0:
                game_over = True
                display_game_over("GAME OVER!")
                stop_game()
            elif current_boss_hp <= 0:
                game_over = True
                display_game_over("YOU WIN!")
                stop_game()

    def drawPlayer():
        hunterPen.clear()
        x, y = playerPosition
        scale = 0.5
        if playerDirection == "left":
            hunterSideView(-1, x, y, scale, swordOut)
            if swordOut:
                sword(x - 45, y + 80, scale, 90)
            else:
                sword(x + 2, y + 40, scale, 90)
        elif playerDirection == "right":
            hunterSideView(1, x, y, scale, swordOut)
            if swordOut:
                sword(x + 45, y + 80, scale, -90)
            else:
                sword(x + 2, y + 40, scale, -90)

    platform = turtle.Turtle()
    platform.hideturtle()
    platform.penup()
    platform.goto(-500, -230)
    platform.pendown()
    platform.begin_fill()
    platform.color("#8d1e06")
    for _ in range(2):
        platform.forward(1000)
        platform.left(90)
        platform.forward(20)
        platform.left(90)
    platform.end_fill()
    platform.color("#431600")
    platform.begin_fill()
    for _ in range(2):
        platform.goto(-500, -230)
        platform.goto(500, -230)
        platform.goto(500, -400)
        platform.goto(-500, -400)
        platform.goto(-500, -230)
    platform.end_fill()
    platform_y = -240
    draw_boss_health_bar(-350, 350)
    draw_hunter_health_bar(150, 350)
    def jump():
        global is_jumping, jump_velocity
        print("Jump triggered!")
        if not is_jumping:
            is_jumping = True
            jump_velocity = jump_strength
            apply_gravity()

    GROUND_LEVEL = platform_y + 20

    def apply_gravity():
        global is_jumping, jump_velocity, playerPosition

        if is_jumping:
            playerPosition[1] += jump_velocity
            jump_velocity += gravity

            # Snap back to ground
            if playerPosition[1] <= GROUND_LEVEL:
                playerPosition[1] = GROUND_LEVEL
                is_jumping = False
                jump_velocity = 0

        drawPlayer()
        screen.update()
        screen.ontimer(apply_gravity, 30)

    def move():
        global playerPosition
        if moveLeft:
            playerPosition[0] -= move_speed
        if moveRight:
            playerPosition[0] += move_speed

        playerPosition[0] = max(-500, min(500, playerPosition[0]))

        drawPlayer()
        screen.update()
        screen.ontimer(move, 50)

    def moveLeftKey():
        global moveLeft, playerDirection
        moveLeft = True
        playerDirection = "left"

    def stopMoveLeft():
        global moveLeft
        moveLeft = False

    def moveRightKey():
        global moveRight, playerDirection
        moveRight = True
        playerDirection = "right"

    def stopMoveRight():
        global moveRight
        moveRight = False

    def hunter_attack(x=None, y=None):
        global swordOut
        # Show sword immediately on click
        swordOut = True
        drawPlayer()
        screen.update()

        # Hide sword after 300 ms
        def resetSword():
            global swordOut
            swordOut = False
            drawPlayer()
            screen.update()

        screen.ontimer(resetSword, 300)

        # Now check if boss is in attack range and facing direction
        if abs(playerPosition[0] - bossPosition[0]) < 200:
            if (playerDirection == "right" and bossPosition[0] >= playerPosition[0]) or \
                    (playerDirection == "left" and bossPosition[0] <= playerPosition[0]):
                bossPen.hp -= 1
                draw_boss_health_bar(-350, 350)
                check_game_over()
                print(f"Boss HP: {bossPen.hp}")

    screen.listen()
    screen.onkeypress(moveLeftKey, "a")
    screen.onkeyrelease(stopMoveLeft, "a")
    screen.onkeypress(moveRightKey, "d")
    screen.onkeyrelease(stopMoveRight, "d")
    screen.onkeypress(jump, "w")

    screen.onscreenclick(hunter_attack)

    def slide_back_to_right(callback):
        start_x, start_y = bossPosition
        end_x, end_y = 350, start_y
        steps = 30

        def slide_step(i):
            if i <= steps:
                t = i / steps
                x = start_x + (end_x - start_x) * t
                y = start_y + (end_y - start_y) * t
                bossPen.clear()
                bossPosition[0], bossPosition[1] = x, y
                hulkArmDown(x, y, bossScale=0.9, flip=(1 if bossDirection == "right" else -1))
                screen.update()
                screen.ontimer(lambda: slide_step(i + 1), 10)
            else:
                callback()

        slide_step(0)

    def slide_to_magic_position(callback):
        start_x, start_y = bossPen.position()
        end_x, end_y = 0, 140
        steps = 30

        def slide_step(i):
            if i <= steps:
                t = i / steps
                x = start_x + (end_x - start_x) * t
                y = start_y + (end_y - start_y) * t
                bossPen.clear()
                bossPosition[0], bossPosition[1] = x, y
                hulkArmDown(x, y, 0.9, flip=(1 if bossDirection == "right" else -1))
                screen.update()
                screen.ontimer(lambda: slide_step(i + 1), 5)
            else:
                callback()

        slide_step(0)

    def screen_shake():
        for _ in range(10):
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            screen._root.geometry(f"+{x}+{y}")
            screen.update()
            time.sleep(0.02)
        screen._root.geometry("+0+0")

    def move_magic_balls():
        still_moving = False
        for ball in magic_balls:
            bx, by = ball.position()

            if not hasattr(ball, "ready_to_attack") or not ball.ready_to_attack:
                continue

            tx, ty = ball.target_x, ball.target_y
            dx = tx - bx
            dy = ty - by
            dist = (dx ** 2 + dy ** 2) ** 0.5
            step = ball.speed_move

            if dist > step:
                ball.setx(bx + dx / dist * step)
                ball.sety(by + dy / dist * step)
                still_moving = True

                px, py = playerPosition
                if abs(ball.xcor() - px) <= 40 and abs(ball.ycor() - py) < 190:
                    hunterPen.hp -= 1
                    draw_hunter_health_bar(150, 350)
                    check_game_over()
                    print(f"Player hit mid-air! HP is now {hunterPen.hp}")
                    ball.hideturtle()
                    ball.ready_to_attack = False
            else:
                ball.goto(tx, ty)
                ball.ready_to_attack = False
                ball.hideturtle()
                print("Ball landed on platform.")

        if still_moving:
            screen.ontimer(move_magic_balls, 30)

    def boss_charge_step(index, x_vals, callback):
        if index < len(x_vals):
            bossPen.setx(x_vals[index])
            screen.update()
            screen.ontimer(lambda: boss_charge_step(index + 1, x_vals, callback), 10)
        else:
            boss_charge_to_hunter(callback)

    def boss_charge_to_hunter(callback):
        hx = hunterPen.xcor()
        hy = platform_y + 40  # fixed target height
        bx, by = bossPen.position()
        steps = 20
        dx = (hx - bx) / steps
        dy = (hy - by) / steps
        positions = [(bx + dx * i, by + dy * i) for i in range(1, steps + 1)]

        def move_step(i):
            if i < len(positions):
                x, y = positions[i]
                bossPen.clear()
                bossPosition[0], bossPosition[1] = x, y
                hulkArmDown(x, y, 0.9, 1)
                screen.update()
                screen.ontimer(lambda: move_step(i + 1), 5)
            else:
                if abs(bossPosition[0] - playerPosition[0]) <= 70:
                    hunterPen.hp -= 1
                    draw_hunter_health_bar(150, 350)
                    check_game_over()
                    print(f"Hunter HP: {hunterPen.hp}")
                    for j in range(5):
                        hunterPen.sety(hunterPen.ycor() + 5)
                        screen.update()
                        time.sleep(0.05)
                        hunterPen.sety(hunterPen.ycor() - 5)
                        screen.update()
                        time.sleep(0.05)
                    screen_shake()
                screen.ontimer(lambda: slide_to_magic_position(callback), 3000)

        move_step(0)

    def boss_charge_attack(callback):
        start_x, start_y = 400, 200
        end_x, end_y = -500, 0
        steps = 30
        path = []
        for i in range(steps + 1):
            t = i / steps
            x = start_x + (end_x - start_x) * t
            base_y = start_y + (end_y - start_y) * t

            bump_height = 50  # how high the bump is
            bump = bump_height * math.sin(math.pi * t)
            y = base_y + bump
            path.append((x, y))

        def move_diagonal(i):
            if i <= steps:
                x, y = path[i]
                bossPen.clear()
                bossPosition[0], bossPosition[1] = x, y
                hulkArmDown(x, y, 0.9, -1)
                screen.update()
                screen.ontimer(lambda: move_diagonal(i + 1), 10)
            else:
                boss_charge_to_hunter(callback)

        move_diagonal(0)

    def boss_magic_attack(callback):
        bossPen.clear()
        bossPosition[0], bossPosition[1] = 0, 140
        hulkArmUp(0, 140, 0.9, flip=(1 if bossDirection == "right" else -1))
        screen.update()
        magic_balls.clear()

        ball_count = 8
        arc_width = 300
        arc_height = 100

        start_x, start_y = bossPen.position()

        for i in range(ball_count):
            ball = turtle.Turtle()
            ball.shapesize(2)
            ball.shape("circle")
            ball.color("#69ff9b")
            ball.penup()
            ball.speed(0)
            ball.goto(start_x, start_y)

            # Calculate spread target in an arc (evenly spaced)
            t = i / (ball_count - 1)  # Goes from 0 to 1
            offset_x = -arc_width // 2 + t * arc_width
            offset_y = arc_height * math.sin(math.pi * t)
            ball.spread_target = (start_x + offset_x, start_y + offset_y + 2)
            ball.has_moved = False
            magic_balls.append(ball)

        def spread_step():
            done = True
            for ball in magic_balls:
                if not ball.has_moved:
                    bx, by = ball.position()
                    tx, ty = ball.spread_target
                    dx = tx - bx
                    dy = ty - by
                    dist = (dx ** 2 + dy ** 2) ** 0.5
                    step_size = 5
                    if dist > step_size:
                        ball.setx(bx + dx / dist * step_size)
                        ball.sety(by + dy / dist * step_size)
                        done = False
                    else:
                        ball.goto(tx, ty)
                        ball.has_moved = True
            screen.update()
            if not done:
                screen.ontimer(spread_step, 20)
            else:
                screen.ontimer(start_ball_attack_sequence, 300)

        def start_ball_attack_sequence():
            def send_ball(index):
                if index >= len(magic_balls):
                    print("All balls launched.")
                    screen.ontimer(callback, 500)
                    return

                ball = magic_balls[index]

                target_x = hunterPen.xcor()
                target_y = platform_y + 10

                ball.target_x = target_x
                ball.target_y = target_y
                ball.speed_move = 15
                ball.ready_to_attack = True
                move_magic_balls()
                print(f"Ball {index} is set to attack at ({ball.target_x}, {ball.target_y})")

                screen.ontimer(lambda: send_ball(index + 1), 300)

            send_ball(0)

        spread_step()

    def after_boss_charge():
        boss_magic_attack(lambda:
                          slide_back_to_right(lambda:
                                              screen.ontimer(game_turn, 1000)
                                              )
                          )

    def display_game_over(message):
        bossPen.clear()
        hunterPen.clear()
        bossPen.hideturtle()
        hunterPen.hideturtle()

        msgPen.penup()
        msgPen.goto(0, 0)
        msgPen.color("red" if "Game Over" in message else "green")
        msgPen.write(message, align="center", font=("Arial", 48, "bold"))

        screen.update()

    def stop_game():
        screen.update()
        screen.exitonclick()

    def game_turn():
        global turn_number, first_turn, game_over

        if game_over:
            return

        if first_turn:
            first_turn = False
            screen.ontimer(game_turn, 1000)
            return

        turn_number += 1
        print(f"TURN {turn_number} begins")

        boss_charge_attack(lambda:
                           screen.ontimer(after_boss_charge, 1000)
                           )

    move()
    apply_gravity()
    move_magic_balls()
    game_turn()
    screen.mainloop()

def hunter_is_alive():
    return hunterPen.food > 0 and hunterPen.hp > 0


def show_survival_game_over():
    run_transition_card(
        "The Hunter has fallen",
        "Food or Heart reached zero.",
        None,
        3000,
    )


def on_day_activity_complete():
    global currentDay, consecutiveNoRest
    if not hunter_is_alive():
        show_survival_game_over()
        return

    if consecutiveNoRest >= 2:
        enter_dreamland()
        return

    currentDay += 1
    if currentDay > maxDays:
        go_to_boss_path()
        return

    begin_day_at_hub()


def enter_dreamland():
    global consecutiveNoRest
    consecutiveNoRest = 0
    clear_hub_scene()
    run_transition_card(
        "Dreamland",
        "You have not rested for 2 days...",
        start_dreamland_fight,
        2200,
    )


def start_dreamland_fight():
    clear_hub_scene()
    clear_dreamland_scene()
    run_transition_card("Dreamland Fight", "Magical monsters await...", lambda: scene_4(on_complete=after_dreamland), 1400)


def after_dreamland():
    global consecutiveNoRest, currentDay
    clear_dreamland_scene()
    consecutiveNoRest = 0
    if not hunter_is_alive():
        show_survival_game_over()
        return
    # Dreamland replaces the normal end-of-day advance; continue the journey.
    currentDay += 1
    if currentDay > maxDays:
        go_to_boss_path()
        return
    begin_day_at_hub()


def go_to_boss_path():
    global _scene_5_active
    clear_hub_scene()
    run_transition_card(
        "The Path to the Boss",
        "A giant dragon awaits at the end...",
        start_boss_path_scene,
        2000,
    )


def start_boss_path_scene():
    global _scene_5_active
    _scene_5_active = True
    updateScene_5()
    screen.ontimer(finish_boss_path_transition, 3500)


def finish_boss_path_transition():
    global _scene_5_active
    _scene_5_active = False
    skyPen.clear()
    backgroundPen.clear()
    starPen.clear()
    roadPen.clear()
    treePen.clear()
    rockPen.clear()
    moonPen.clear()
    skullPen.clear()
    hunterPen.clear()
    glowPen.clear()
    run_transition_card(
        "BOSS",
        start_boss_fight,
        1800,
    )


def start_boss_fight():
    scene_6()


def begin_day_at_hub():
    clear_rest_scene()
    clear_fishing_scene()
    draw_hub_frame()
    run_transition_card(
        f"Day {currentDay} of {maxDays}",
        "Two paths: rest or fishing.",
        prompt_daily_choice,
    )


def prompt_daily_choice():
    msgPen.clear()
    msgPen.penup()
    msgPen.goto(-200, 155)
    msgPen.color("black")
    msgPen.write(
        "If you go to fish, you can get food bar, but there's unknown dangers.\n"
        "But going to sleep will lose a food bar.\n\n"
        "You can fish for up to 4 days.\n"
        "Choose wisely! (enter 'rest' or 'fish')",
        font=("Arial", 14, "normal"),
    )
    screen.update()
    choice = screen.textinput("Your Choice", "Enter 'rest' or 'fish':")
    if choice not in ("rest", "fish"):
        prompt_daily_choice()
        return
    if choice == "rest":
        handle_rest_choice()
    else:
        handle_fish_choice()


def handle_rest_choice():
    global consecutiveNoRest, _scene_2_active
    consecutiveNoRest = 0
    hunterPen.food -= 1
    if not hunter_is_alive():
        show_survival_game_over()
        return
    run_transition_card(
        "Resting",
        "Walking to camp...",
        lambda: animate_walk_to_rest(start_rest_camp),
        900,
    )


def start_rest_camp():
    global _scene_2_active
    clear_hub_scene()
    signPen.clear()
    _scene_2_active = True
    updateScene_2()
    screen.ontimer(showSleepMessage, 2000)
    screen.ontimer(finish_rest_day, 5500)


def finish_rest_day():
    if not _scene_2_active:
        return
    begin_walk_from_rest()


def begin_walk_from_rest():
    clear_rest_scene()
    animate_walk_from_rest(after_return_to_hub)


def handle_fish_choice():
    global currentFishingAttempts, maxFishingPerDay, consecutiveNoRest, _fishing_animate_active, _fishing_return_scheduled
    consecutiveNoRest += 1
    currentFishingAttempts = 0
    maxFishingPerDay = 2
    _fishing_return_scheduled = False
    run_transition_card(
        "Fishing",
        "Walking to the river...",
        lambda: animate_walk_to_fish(start_fishing_scene),
        900,
    )


def start_fishing_scene():
    global _fishing_animate_active
    clear_hub_scene()
    signPen.clear()
    _fishing_animate_active = True
    animate()
    run_transition_card("Fishing Spot", "Click to cast your rod.", lambda: scene_3(), 1100)


def main():
    scene_1()
    draw_hunter_health_bar(150, 350)
    draw_hunter_food_bar(150, 280)
    screen.update()
    time.sleep(1)
    msgPen.penup()
    msgPen.goto(-200, 200)
    msgPen.color("black")
    msgPen.write(
        "You wake up in a forest.\n"
        "You are going to stay 5 days here, prepare you for the boss fight.\n"
        "There are two paths: one to rest, one to fish.\n",
        font=("Arial", 16, "normal"),
    )
    msgPen.goto(-200, 150)
    time.sleep(2)
    msgPen.write("Click anywhere to continue...", font=("Arial", 14, "italic"))

    def onIntroClick(x, y):
        msgPen.clear()
        screen.onclick(None)
        run_transition_card(
            "Frame 1 — Welcome",
            "Meet Hunter. Watch your Food and Heart bars.",
            begin_day_at_hub,
            2000,
        )

    screen.onclick(onIntroClick)
    screen.mainloop()


main()
print("Wish you great experience!")