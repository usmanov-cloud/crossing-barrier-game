from turtle import Turtle


STARTING_POSITION = (0, -280) # The Starting position of the Turtle on our Screen 
MOVE_DISTANCE = 10 # The distance the Turtle is going to move
FINISH_LINE_Y = 280 # The finish line of the Turtle on Y axis i.e the end


class Player(Turtle): #Player class inherit from the Turtle class, right now our Player class can do everything our Turtle class can do as well.
    '''
    The player Class is going to be the Turtle which we will
     control to cross the road.
    
    When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
    '''

    def __init__(self):
        super().__init__()
        self.shape("turtle") # setting the shape of our player to turtle
        self.penup()# turtle won't draw on the screen
        self.go_to_start() # the starting position of our turtle 
        self.setheading(90) # making the turtle to face north which is 90 degrees




    def go_up(self):
        '''
        A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
        '''
        self.forward(MOVE_DISTANCE)


    def go_to_start(self):
        '''
        This method returns the player back to the starting position.
        '''
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        '''
        This method is going to return True if the turtle is at the finish line and False while it is not
        '''
        if self.ycor() > FINISH_LINE_Y:
            return True

        else:
            return False
