from turtle import speed, forward, left, right, penup, pendown, goto, setheading, mainloop, backward

def sierpinski_triangle(length, level):
    """
    Draws a Sierpinski Triangle fractal.

    Args:
    length (float): The length of the sides of the triangle.
    level (int): The current level of recursion depth.
    """
    if level == 0:
        for _ in range(3):
            forward(length)
            left(120)
    else:
        sierpinski_triangle(length/2, level-1)
        forward(length/2)
        sierpinski_triangle(length/2, level-1)
        backward(length/2)
        left(60)
        forward(length/2)
        right(60)
        sierpinski_triangle(length/2, level-1)
        left(60)
        backward(length/2)
        right(60)

def draw_sierpinski(length, level):
    """
    Sets up the environment and starts drawing the Sierpinski Triangle.

    Args:
    length (float): The length of the sides of the triangle.
    level (int): The depth of recursion for the fractal.
    """
    speed(0)
    penup()
    goto(-length/2, -length/2)
    pendown()
    sierpinski_triangle(length, level)

# User input for the length of the side and the recursion depth
side_length = int(input("Enter the length of the side of the Sierpinski Triangle: "))
recursion_depth = int(input("Enter the recursion depth for the Sierpinski Triangle: "))

# Drawing the Sierpinski Triangle
draw_sierpinski(side_length, recursion_depth)

# Prevent the window from closing immediately
mainloop()
