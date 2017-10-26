#Charlie Goodrich
#10/25/17
#bouncingBall.py - makes a ball move around the screen

from ggame import *
def moveBall():
    ball.x += data["direction x"]
    ball.y += data["direction y"]
    
    if ball.y == 50 or ball.y == 500:
        data["direction y"] *= -1
    if ball.x == 50 or ball.x == 1000:
        data["direction x"] *= -1

if __name__ == "__main__":
    
    data = {}
    data["direction x"] = 10
    data["direction y"] = 10
    
    #Colors
    green = Color(0x00FF00, 1)
    greenOutline = LineStyle(1, green)
    black = Color(0x000000, 1)
    blackOutline = LineStyle(1, black)
    
    
    greenCircle = CircleAsset(50, greenOutline, green)
    background = RectangleAsset(1050, 600, blackOutline, black)
    
    Sprite(background)
    ball = Sprite(greenCircle, (50, 50))
    
    App().run(moveBall)
    

    
    
