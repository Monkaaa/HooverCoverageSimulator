from tkinter import *

def draw_grid():
    # draw vertical lines
    for x in range(0, canvas_width + 1, cell_size):
        canvas.create_line(x, 0, x, canvas_height, fill='white')

    # draw horizontal lines
    for y in range(0, canvas_height + 1, cell_size):
        canvas.create_line(0, y, canvas_width, y, fill='white')


# e is automatically passed by Tkinter when the even occurs
def draw_on_mouse(e):
    # access global variable as we cannot return values from this function
    global last_pos

    x = e.x
    y = e.y

    if last_pos != None:
        canvas.create_line(last_pos[0], last_pos[1], x, y, fill='white')

    last_pos = (x, y)


root = Tk()

# initialising variable values
last_pos = None
canvas_width = 1920
canvas_height = 1080
cell_size = 80


# creating base canvas
canvas = Canvas(root, bg='grey', width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0, sticky=(N, W, E, S))

# drawing visual grid
draw_grid()

# call event
canvas.bind('<Motion>',draw_on_mouse)

root.mainloop()

######

