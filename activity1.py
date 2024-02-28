from turtle import Turtle, Screen

def SetPos(turta,x,y):
    turta.penup()
    turta.goto(x,y)
    turta.pendown()
    
def circle(turta, circle_color, border_color):
    turta.pencolor(border_color)
    turta.pensize(3)
    turta.begin_fill()
    turta.fillcolor(circle_color)
    turta.circle(50)
    turta.end_fill()

def square(turta, square_color, border_color):
    turta.pencolor(border_color) 
    turta.pensize(3) 
    turta.up()
    turta.down()
    turta.begin_fill() 
    turta.fillcolor(square_color)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()
    
def hexagon(turta, hexa_color, border_color):
    turta.pencolor(border_color)
    turta.pensize(3)
    turta.up()
    turta.down()
    turta.begin_fill()
    turta.fillcolor(hexa_color)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.end_fill()
    
def pattern(turta, hexa_color, circle_color, square_color, border_color):
    
    #set position for circle, square and hexagon 1
    
    SetPos(turta,0,0)  
    circle(turta, circle_color, border_color)
    SetPos(turta,90,0)   
    square(turta, square_color, border_color)
    SetPos(turta,-110,0)
    hexagon(turta, hexa_color, border_color)
   
    #set position for circle, square and hexagon 2

    SetPos(turta,90,-120)  
    circle(turta, circle_color, border_color)
    SetPos(turta,180,-120)  
    square(turta, square_color, border_color)
    SetPos(turta,-15,-120)
    hexagon(turta, hexa_color, border_color)

    #set position for circle, square and hexagon 3

    SetPos(turta,-90, 120)  
    circle(turta, circle_color, border_color)
    SetPos(turta,0,120)   
    square(turta, square_color, border_color)
    SetPos(turta,-200, 120)
    hexagon(turta, hexa_color, border_color)
   
def main():
    wind=Screen()  #sets up the window and turtle for drawing
    wind.bgcolor("light blue")  
    turtle =Turtle()   
    turtle.speed(5)
    hexa_color = input("Enter color for hexagon: ")
    circle_color = input("Enter color for circle: ")
    square_color = input("Enter color for square: ")
    border_color = input("Enter color for borders: ")
   
    pattern(turtle, hexa_color, circle_color, square_color, border_color)
    wind.exitonclick()   


main()