import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3

# Colors
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

# Snake class
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

# Food class
class Food:
    def __init__(self):
        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Move snake
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

# Direction control
def change_direction(new_direction):
    global direction

    if new_direction == "left" and direction != "right":
        direction = new_direction
    elif new_direction == "right" and direction != "left":
        direction = new_direction
    elif new_direction == "up" and direction != "down":
        direction = new_direction
    elif new_direction == "down" and direction != "up":
        direction = new_direction

# Collision check
def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Game over with Restart button
def game_over():
    canvas.delete("all")

    canvas.create_text(WIDTH/2, HEIGHT/2 - 30,
                       text="GAME OVER", fill="red", font=("Arial", 30))

    restart_button = tk.Button(window, text="Restart",
                               font=("Arial", 12),
                               command=restart_game,
                               bg="green", fg="white")

    canvas.create_window(WIDTH/2, HEIGHT/2 + 20, window=restart_button)

# Restart game
def restart_game():
    global snake, food, score, direction

    score = 0
    direction = "down"
    label.config(text="Score: 0")

    canvas.delete("all")

    snake = Snake()
    food = Food()

    next_turn(snake, food)

# Main window
window = tk.Tk()
window.title("Snake Game")

score = 0
direction = "down"

label = tk.Label(window, text="Score: {}".format(score), font=("Arial", 14))
label.pack()

canvas = tk.Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

# Controls
window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('<Up>', lambda event: change_direction("up"))
window.bind('<Down>', lambda event: change_direction("down"))

# Optional: press R to restart
window.bind('<r>', lambda event: restart_game())

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()