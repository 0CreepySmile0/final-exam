import turtle
import random


class Artwork:
    def __init__(self, choice):
        self.__choice = choice
        self.__side = random.randint(3, 5)
        self.__size = random.randint(50, 150)
        self.__orientation = random.randint(0, 90)
        self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.__border = random.randint(1, 10)
        self.__reduction = 0.618

    def draw_polygon(self, side):
        turtle.penup()
        turtle.goto(self.__location[0], self.__location[1])
        turtle.setheading(self.__orientation)
        turtle.color(self.__color)
        turtle.pensize(self.__border)
        turtle.pendown()
        for _ in range(side):
            turtle.forward(self.__size)
            turtle.left(360/side)
        turtle.penup()

    def get_new_location(self):
        turtle.penup()
        turtle.forward(self.__size * (1 - self.__reduction) / 2)
        turtle.left(90)
        turtle.forward(self.__size * (1 - self.__reduction) / 2)
        turtle.right(90)
        self.__location[0] = turtle.pos()[0]
        self.__location[1] = turtle.pos()[1]

    def adjust_size(self):
        self.__size *= self.__reduction

    def draw_artwork(self):
        if self.__choice == 1:
            for i in range(random.randint(25, 50)):
                Artwork(1).draw_polygon(3)
        elif self.__choice == 2:
            for i in range(random.randint(25, 50)):
                Artwork(2).draw_polygon(4)
        elif self.__choice == 3:
            for i in range(random.randint(25, 50)):
                Artwork(3).draw_polygon(5)
        elif self.__choice == 4:
            for i in range(random.randint(25, 50)):
                Artwork(4).draw_polygon(random.randint(3, 5))
        elif self.__choice == 5:
            for i in range(random.randint(25, 50)):
                n = Artwork(5)
                for j in range(2):
                    n.draw_polygon(3)
                    n.get_new_location()
                    n.adjust_size()
                    n.draw_polygon(3)
        elif self.__choice == 6:
            for i in range(random.randint(25, 50)):
                n = Artwork(6)
                for j in range(2):
                    n.draw_polygon(4)
                    n.get_new_location()
                    n.adjust_size()
                    n.draw_polygon(4)
        elif self.__choice == 7:
            for i in range(random.randint(25, 50)):
                n = Artwork(7)
                for j in range(2):
                    n.draw_polygon(5)
                    n.get_new_location()
                    n.adjust_size()
                    n.draw_polygon(5)
        elif self.__choice == 8:
            for i in range(random.randint(25, 50)):
                n = Artwork(8)
                side = random.randint(3, 5)
                for j in range(2):
                    n.draw_polygon(side)
                    n.get_new_location()
                    n.adjust_size()
                    n.draw_polygon(side)


choice = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
Artwork(choice).draw_artwork()
turtle.done()
