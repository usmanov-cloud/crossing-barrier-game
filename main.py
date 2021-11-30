import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Candidate No : 22113381
# Name: Lawal uthman
screen = Screen() # Created Screen Object from Turtle Module
screen.bgpic('image/lane.gif')
screen.title('Crossing Game')
screen.setup(width=600, height=600) # Setup The Screen to be 600x600 pixels
screen.tracer(0) # Turned off the tracer by making the tracer to be Zero


player = Player() # created new player from our player class
car_manager = CarManager()# created car manager from CarManager Class and we can now use it inside our game loop so that every refresh of the screen, every 0.1 sec to get the car manager to create a new car
scoreboard = Scoreboard()# created scoreboard from our Scoreboard class

screen.listen() # getting our screen to listen to event
screen.onkey(player.go_up, "Up") #getting the screen to listen to key stroke. setting our player to go up whenever the up key is pressed.

game_is_on = True
while game_is_on:
    '''
    We trying to get the screen to update at every 0.1 sec.
    So within the while loop the code is going to run every 0.1 sec.
    Anything we put inside this loop is going to refresh every 0.1 sec.
    '''
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.mainloop()
