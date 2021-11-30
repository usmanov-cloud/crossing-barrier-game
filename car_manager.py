import turtle
from turtle import Turtle
import random

COLORS = ["red", "indigo", "yellow", "green", "blue", "purple"] # colors of different cars
STARTING_MOVE_DISTANCE = 5 # the distance the Turtle is going to move on each refresh
MOVE_INCREMENT = 8 # the speed of the cars when the levels goes up

Name = turtle.textinput("Personal Detail", "Name")
class CarManager:
    '''
    CarManager is going to generate all the random cars and move them across the screen.
    Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
    '''

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        '''
       
        Create cars that are 20px high by 40px wide that are randomly generated along the Y-axis and move to the left edge of the screen. 
        This method is going to create cars somewhere along the Y axis with a given dimension.
        '''
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square") # shape of our turtle to square
            new_car.shapesize(stretch_wid=1, stretch_len=2) # it allows to stretch the width and the length. Length to be twice the original size and width to be the original width.
            new_car.penup()# our new car is going to draw and is going to pen up
            new_car.color(random.choice(COLORS))# Random colors for our new cars
            random_y = random.randint(-250, 250)# Where our new cars should go on the screen on the Y axis. remember our screen is 600x600, so our Y axis is positive 300 and negative -300. 
            new_car.goto(300, random_y)# we now tell our newly generated cars to go 300px on the X axis and random_y we defined above on the y-axis.
            self.all_cars.append(new_car)# we can append our cars to our list of all cars in our CarManager Class

    def move_cars(self):
        '''
        This method moves all the cars. this method will go through our list of cars and it's going to move it by the move distance.
        '''
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        '''
        This method increases the speed of the game when the game levels up.
        '''
        self.car_speed += MOVE_INCREMENT
