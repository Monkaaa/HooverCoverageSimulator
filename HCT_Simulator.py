from tkinter import *
from tkinter import ttk

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

    x= e.x
    y= e.y

    cell_x = x // cell_size
    cell_y = y // cell_size

    pixel_x = x % cell_size
    pixel_y = y % cell_size

    if not cells[cell_y][cell_x][pixel_y][pixel_x]:
        cells[cell_y][cell_x][pixel_y][pixel_x] = True
        cell_percent = calc_percentage(x, y)

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


def calc_percentage(current_x, current_y):
    total_cell_pixels = cell_size * cell_size
    current_cell = cells[current_y//cell_size][current_x//cell_size]

    total_touched_pixels = 0

    for pixel_row in current_cell:
        for pixel in pixel_row:
            if pixel:
                total_touched_pixels += 1

    cell_percent_filled = total_touched_pixels / total_cell_pixels * 100

    cell_percentages[current_y//cell_size][current_x//cell_size] = int(cell_percent_filled)

    display_cell_percent(current_x, current_y)


def create_labels():
    for y in range(len(cell_percentages)):
        row_labels = []
        for x in range(len(cell_percentages[0])):
            percent = cell_percentages[y][x]
            label = ttk.Label(canvas, text=f"{percent}%")
            label.place(x=x * cell_size + (cell_size//2), y=y * cell_size + (cell_size//2), anchor="center")
            row_labels.append(label)
        labels.append(row_labels)


def display_cell_percent(current_x, current_y):
    print(cell_percentages[current_y//cell_size][current_x//cell_size])




root = Tk()

# initialising variable values
last_pos = None
canvas_width = 1920
canvas_height = 1080
cell_size = 200

percent_filled = 0

cells = []

labels = []

# initialising list using a list comprehension
cell_percentages = [[0 for column in range(canvas_width//cell_size)] for row in range(canvas_height//cell_size)]

# creating base canvas
canvas = Canvas(root, bg='grey', width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0, sticky=(N, W, E, S))

# drawing visual grid
draw_grid()

# call event
canvas.bind('<Motion>', draw_on_mouse)

# initialise 2d data structure to false
initialise_pixel_status()

create_labels()

root.mainloop()


