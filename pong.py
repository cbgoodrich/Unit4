#Charlie Goodrich
#10/27/17
#pong.py - pong

from ggame import *

#CONSTANTS
WINDOW_X = 1000
WINDOW_Y = 526
RADIUS = 25
PADDLE_X = 20
PADDLE_Y = 80

def moveBall():
    
    ball.x += data["direction x"]
    ball.y += data["direction y"]
    
    if ball.y < 25 or ball.y > WINDOW_Y-25:
        data["direction y"] *= -1
    if ball.x < 25 or ball.x > WINDOW_X-25:
        data["direction x"] *= -1
        
def moveP1Up(event):
    if paddleLeft.y > 0:
        paddleLeft.y += PADDLE_Y

def moveP1Down(event):
    if paddleLeft.y < WINDOW_Y:
        paddleLeft.y -= PADDLE_Y




if __name__ == "__main__":
    
    data = {}
    data["direction x"] = 10
    data["direction y"] = 10
    
    green = Color(0x00FF00, 1)
    black = Color(0x000000, 1)
    
    background = RectangleAsset(WINDOW_X, WINDOW_Y, LineStyle(1, black), black)
    circle = CircleAsset(RADIUS, LineStyle(1, green), green)
    rectangle = RectangleAsset(PADDLE_X, PADDLE_Y, LineStyle(1, green), green)
    
    
    Sprite(background)
    ball = Sprite(circle, (WINDOW_X/2, WINDOW_Y/2))
    paddleLeft = Sprite(rectangle, (0, WINDOW_Y/2-PADDLE_Y/2))
    paddleRight = Sprite(rectangle, (WINDOW_X-PADDLE_X, WINDOW_Y/2-PADDLE_Y/2))
    App().run(moveBall)
    
