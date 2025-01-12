import turtle
import time
import random

# Configurare initiala a ferestrei
window = turtle.Screen()
window.title("Snake Game - Turtle Edition")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Configurare Snake
snake = []
for i in range(3):
    segment = turtle.Turtle("square")
    segment.color("green")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

# Configurare Mancare
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0, 100)

# Configurare Obstacole
obstacles = []
for _ in range(5):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("grey")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-280, 280) // 20 * 20, random.randint(-280, 280) // 20 * 20)
    obstacles.append(obstacle)

# Configurare Scor
score = 0
high_score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Control
direction = "stop"
def go_up():
    global direction
    if direction != "down":
        direction = "up"
def go_down():
    global direction
    if direction != "up":
        direction = "down"
def go_left():
    global direction
    if direction != "right":
        direction = "left"
def go_right():
    global direction
    if direction != "left":
        direction = "right"

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Functii auxiliare
def move():
    if direction == "up":
        x, y = snake[0].pos()
        snake[0].goto(x, y + 20)
    elif direction == "down":
        x, y = snake[0].pos()
        snake[0].goto(x, y - 20)
    elif direction == "left":
        x, y = snake[0].pos()
        snake[0].goto(x - 20, y)
    elif direction == "right":
        x, y = snake[0].pos()
        snake[0].goto(x + 20, y)

def check_collision():
    global score, high_score, direction
    head = snake[0]

    # Coliziune cu marginile
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        reset_game()

    # Coliziune cu corpul
    for segment in snake[1:]:
        if head.distance(segment) < 20:
            reset_game()

    # Coliziune cu obstacole
    for obstacle in obstacles:
        if head.distance(obstacle) < 20:
            reset_game()

def reset_game():
    global score, high_score, direction
    time.sleep(1)
    for segment in snake:
        segment.goto(1000, 1000)
    snake.clear()
    for i in range(3):
        segment = turtle.Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(-20 * i, 0)
        snake.append(segment)
    direction = "stop"
    score = 0
    update_score()

def update_score():
    global high_score
    if score > high_score:
        high_score = score
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Joc principal
while True:
    window.update()

    if direction != "stop":
        # Muta corpul sarpelui
        for i in range(len(snake) - 1, 0, -1):
            x, y = snake[i - 1].pos()
            snake[i].goto(x, y)
        move()

        # Verifica coliziuni
        check_collision()

        # Coliziune cu mancarea
        if snake[0].distance(food) < 20:
            score += 10
            update_score()

            # Adauga segment nou
            segment = turtle.Turtle("square")
            segment.color("green")
            segment.penup()
            snake.append(segment)

            # Muta mancarea
            food.goto(random.randint(-280, 280) // 20 * 20, random.randint(-280, 280) // 20 * 20)

        time.sleep(0.1)
