from turtle import Screen
from scoreboard import Scoreboard
import time
import snake
import food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake game')
scoreboard = Scoreboard()
food = food.Food()
snake1 = snake.Snake()
game_is_on = True
screen.listen()
screen.onkey(snake1.up,'Up')
screen.onkey(snake1.down,"Down")
screen.onkey(snake1.left,"Left")
screen.onkey(snake1.right,"Right")
counter = 0
while game_is_on:
    screen.update()
    time.sleep(.09)
    snake1.move()
    # detect collision with food
    if snake1.head.distance(food) < 15:
        food.refresh()
        snake1.extend()
        scoreboard.add_point()
    # detect collision with wall
    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        scoreboard.reset()
        snake1.reset()
    for body_part in snake1.segments[1:]:
        if snake1.head.distance(body_part) < 10:
            scoreboard.reset()
            snake1.reset()
        counter += 1

    # detect collision with tail
    # if head collides with any segment in the tail

print(f"you lose with score: {scoreboard.score}")



screen.exitonclick()
