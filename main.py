# FIRST WE HAVE TO IMPORT FILES 
# TURTLE / TIME / SNAKE / SCOREBOARD / SCREEN 

from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

food=Food()
snake=Snake()
scoreboard=Scoreboard()

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    # COLLISION
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.incerease_score()

    if snake.head.xcor() > 280 or snake.head.xcor()<-200 or snake.head.ycor() > 280 or snake.head.ycor()< -280 :
        game_is_on= False
        scoreboard.game_over()
     
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()    
    
screen.exitonclick()



