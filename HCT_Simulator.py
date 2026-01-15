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


def initialise_pixel_status():
    # going over a row of cells
    for row_of_cells in range(canvas_height//cell_size):
        # initialising list which will hold data for all cells in current row
        cell_row = []
        # going over each cell in current row
        for cell_in_row in range(canvas_width//cell_size):
            # initialising list which will hold data for each individual cell in current row
            cell = []
            # going over each pixel in current cell
            for row_of_pixels in range(cell_size):
                # initialising list which will hold data for each pixel in current row of the current cell
                pixel_row = []
                # going over each pixel in current row of current cell
                for pixel_in_row in range(cell_size):
                    # add current pixels 'data' to pixel row
                    pixel_row.append(False)
                # all of current cells current row of pixel data has been set it can now be appended to the cell list
                cell.append(pixel_row)
            # all of current cells data has been set and can be appended to the cell_row before moving onto next cell in row
            cell_row.append(cell)
        cells.append(cell_row)


root = Tk()

# initialising variable values
last_pos = None
canvas_width = 1920
canvas_height = 1080
cell_size = 80

cells = []

# creating base canvas
canvas = Canvas(root, bg='grey', width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0, sticky=(N, W, E, S))

# drawing visual grid
draw_grid()

# call event
canvas.bind('<Motion>',draw_on_mouse)

# initialise 2d data structure to false
initialise_pixel_status()

root.mainloop()

######

