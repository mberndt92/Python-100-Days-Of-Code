import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CARS = 30


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def random_position(self):
        start_x = 300
        start_y = random.randint(-250, 250)
        return start_x, start_y

    def generate_car(self, position):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.goto(position)
        return car

    def tick(self):
        self.spawn_new_cars()
        self.move_cars()

    def spawn_new_cars(self):
        should_spawn_new_car = random.randint(0,100)
        if should_spawn_new_car >= 80:
            self.cars.append(self.generate_car(self.random_position()))

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)
            # Problem - we are never clearing cars out!

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
