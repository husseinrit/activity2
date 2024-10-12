from turtle import Screen, Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def get_color(character):
    if character == '0':
        return 'black'
    elif character == '1':
        return 'white'
    elif character == '2':
        return 'red'
    elif character == '3':
        return 'yellow'
    elif character == '4':
        return 'orange'
    elif character == '5':
        return 'green'
    elif character == '6':
        return 'yellowgreen'
    elif character == '7':
        return 'sienna'
    elif character == '8':
        return 'tan'
    elif character == '9':
        return 'gray'
    elif character == 'A':
        return 'darkgray'
    else:
        return None
    
def draw_color_pixel(color_string, turta):
    turta.pendown()
    turta.pencolor('black')
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(PIXEL_SIZE)
        turta.left(90)
    turta.end_fill()
    turta.penup()
    turta.forward(PIXEL_SIZE)

def draw_pixel(color_string, turta):
    color = get_color(color_string) 
    if color:
        draw_color_pixel(color, turta)
        return True
    return False

def draw_line_from_string(color_string, turta):
    for code in color_string:
        if not draw_pixel(code, turta):
            draw_pixel('0', turta)  # Draw black block for invalid color
            draw_pixel('1', turta)  # Draw white block for invalid color
            return False
    return True

def draw_shape_from_string(turta):
    while True:
        color_string = input("Enter string of color codes: ")

        if color_string == "":
            print("Empty string entered, no more pixels will be outputted")
            break
        
        result = draw_line_from_string(color_string, turta)

        if result is False:
            print("Invalid input, program closing")
            break

def main(turta):
    initialization(turta)
    draw_shape_from_string(turta)

screen = Screen()
turta = Turtle()
main(turta)
screen.exitonclick()

