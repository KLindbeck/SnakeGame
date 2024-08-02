#tkinter in graphic library
import tkinter
#random will be used for food spawn
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile:
        def __init__(self, x,y):
            self.x = x
            self.y = y

#game Window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize game
snake = Tile(5*TILE_SIZE,5*TILE_SIZE)
food = Tile(10*TILE_SIZE,10*TILE_SIZE)
snake_body = [] #multiple snake tiles
velocityX = 0
velocityY = 0
game_over = False
score = 0

def change_direction(e): # E means Event

        global velocityX, velocityY, game_over
        if (game_over):
            return

        if (e.keysym == "Up" and velocityY !=1):
            velocityX = 0
            velocityY = -1
        elif (e.keysym == "Down"and velocityY !=-1):
            velocityX = 0
            velocityY = 1
        elif (e.keysym == "Left" and velocityX != 1):
            velocityX = -1
            velocityY = 0
        elif (e.keysym == "Right" and velocityX !=-1):
            velocityX = 1
            velocityY = 0
def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
        return

    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return

    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

    if(snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1)* TILE_SIZE
        food.y = random.randint(0, ROWS-1)* TILE_SIZE
        score += 10


        #update snake body
    for i in range(len(snake_body) - 1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, score
    move()

    canvas.delete("all")

    # Draw Food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")

    #Drawing of the Snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "green")

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "green")
    # Draw every 10 frames
    window.after(100, draw)

    if(game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font= "Terminal 40", text = f"GAME OVER:{score}", fill= "white")
    else:
        canvas.create_text(500,20, font= "Terminal 15", text= f"SCORE: {score}", fill= "white" )


draw()
window.bind("<KeyRelease>", change_direction) #when you press on any key and then let go
window.mainloop() #used for listening to window events like key presses




# by 찻주전자