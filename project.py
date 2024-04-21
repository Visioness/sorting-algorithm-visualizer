'''
This program visualizes Sorting Algorithms depending on the chosen algorithm and list size.

Algorithms: Selection Sort, Insertion Sort, Bubble Sort, Merge Sort, Quick Sort, Heap Sort
Sizes: 10, 30, 50, 80, 100, 200 
'''
from visualizers import Visualize
from algorithms import Algorithm
from turtle import *
import random
import time


# Assigning screen global variable as None
screen = None

# Creating an empty list for menu elements; we will reassign this later
LIST_TO_SORT = []

# Storing algorithms and sizes as lists in a dictionary to be able to use them later on
menu_elements = {
    'Sorting Algorithms': [
        ('Selection Sort', (Visualize.selection_sort, Algorithm.selection_sort, [LIST_TO_SORT,])),
        ('Insertion Sort', (Visualize.insertion_sort, Algorithm.insertion_sort, [LIST_TO_SORT,])),
        ('Bubble Sort', (Visualize.bubble_sort, Algorithm.bubble_sort, [LIST_TO_SORT,])),
        ('Merge Sort', (Visualize.merge_sort, Algorithm.merge_sort, [LIST_TO_SORT,])),
        ('Quick Sort', (Visualize.quick_sort, Algorithm.quick_sort, [LIST_TO_SORT, 0, len(LIST_TO_SORT) - 1])),
        ('Heap Sort', (Visualize.heap_sort, Algorithm.heap_sort, [LIST_TO_SORT,]))
    ],
    'List Sizes': [10, 30, 50, 80, 100, 200]
}

# Setting the current menu page to 1, which is the Algorithms menu
current_page = 1
selected = [None, None]


def main():
    global screen
    # Creating the screen
    screen = create_screen()

    # Getting screen to be able to execute visualization on the same screen
    Visualize.get_screen(screen)

    # Creates the first menu and waits for the click to go to the next page
    setup(screen)


# Creating a screen and adjusting its features
def create_screen():
    screen = Screen()
    screen.colormode(255)
    screen.title('Sorting Algorithms')
    screen.setup(width=1600, height=900, starty=0)
    screen.bgcolor('#212A3E')
    screen.update()

    # Disabling the tracer to control and update the screen manually
    screen.tracer(0)

    return screen


# Executing the first menu and waiting for clicks on buttons
def setup(screen):
    create_menu('Sorting Algorithms')
    screen.onscreenclick(check_click)
    screen.mainloop()


# Creating the menu for the given parameter
def create_menu(page):
    # Creating a turtle to handle drawings and texts on the screen
    turtle = Turtle('turtle')
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(8)
    turtle.pensize(4)
    turtle.goto(0, 300)
    turtle.color('#9EB8D9')
    turtle.write('SORTING ALGORITHM VISUALIZER', align='center', font=('Times New Roman', 35, 'bold'))

    turtle.goto(0, 150)
    turtle.color('#9EB8D9')
    turtle.write(f'Choose {page}', align='center', font=('Times New Roman', 28, 'italic'))
    
    # Button naming and drawing borders around them
    for i, value in enumerate(menu_elements[page]):
        x = -350 + (i % 3) * 350
        y = 0 if i < 3 else -200
        
        turtle.goto(x - 120, y - 12)
        turtle.pendown()
        turtle.color('#6096B4')
        for j in range(2):
            turtle.forward(240)
            turtle.left(90)
            turtle.forward(60)
            turtle.left(90)

        turtle.penup()
        turtle.goto(x, y)
        turtle.color('#93BFCF')
        text = f'{value[0]}' if page == 'Sorting Algorithms' else f'{value}'
        turtle.write(text, align='center', font=('Times New Roman', 24, 'italic'))


# Checking click events
def check_click(x, y):
    global current_page
    # If already on page 1(algorithm menu) and any button clicked, the program goes for the next page
    if current_page == 1:
        for i in range(6):
            if button_clicked(x, y, i):
                # Assigning i as the selected algorithm
                selected[0] = i
                screen.clear()
                create_screen()
                current_page = 2
                create_menu('List Sizes')
                screen.onscreenclick(check_click)
                break

    # If on page 2(size menu) and any button clicked, the program starts visualizing
    elif current_page == 2:
        for i in range(6):
            if button_clicked(x, y, i):
                # Assigning i as the selected size
                selected[1] = i
                start_visualize()
                
                # Right after the visualization, wait for a click to shut the program down
                screen.exitonclick()
                break


# Checking if clicks are on buttons
def button_clicked(x, y, index):
    x1 = -350 + (index % 3) * 350
    y1 = 0 if index < 3 else -200

    return x1 - 120 < x < x1 + 120 and y1 - 12 < y < y1 + 48


# Executing visualization based on chosen algorithm and size
def start_visualize():
    global LIST_TO_SORT
    # Creating N sized random list and assigning it to already defined LIST_TO_SORT 
    N = menu_elements['List Sizes'][selected[1]] 
    LIST_TO_SORT = random.sample(range(N), N)
    speeds = [0.2, 0.12, 0.05, 0.03, 0.01, 0]
    Visualize.DELAY = speeds[selected[1]]
    # Recreating screen and showing the random list
    screen.clear()
    create_screen()
    Visualize.show_array(LIST_TO_SORT)

    # Sorting Algorithm and Size info on top left
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.color('#9EB8D9')
    turtle.goto(-750, 380)
    turtle.write(f'{menu_elements["Sorting Algorithms"][selected[0]][0]} - {N}', font=('Times New Roman', 32, 'italic'))

    # Getting functions and parameters for the chosen algorithm
    visualize_func, algorithm_func, parameters = menu_elements['Sorting Algorithms'][selected[0]][1]
    
    # Reassigning list to prevent sorting an empty list 
    parameters[0] = LIST_TO_SORT
    if len(parameters) > 2:
        parameters[2] = len(LIST_TO_SORT) - 1
    
    # Visualizing and time counter
    vis_start = time.perf_counter()
    visualize_func(*parameters)
    vis_time_elapsed = time.perf_counter() - vis_start

    # Default algorithm and time counter
    alg_start = time.perf_counter()
    algorithm_func(*parameters)
    alg_time_elapsed = time.perf_counter() - alg_start
    
    # Showing the results on the top left
    turtle.goto(-750, 280)
    turtle.write(f'Visualize elapsed time: {vis_time_elapsed:.06f} seconds\nAlgorithm elapsed time: {alg_time_elapsed:.06f} seconds', font=('Times New Roman', 22, 'italic'))
    screen.update()


if __name__ == '__main__':
    main()