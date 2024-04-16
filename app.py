'''Visualizer App Class to create screen, algorithm and size menus,
checks click events and lets the main function work right after choosing size.'''
from visualizers import Visualize
from algorithms import Algorithm
from turtle import *
import random
import time


class VisualizerApp():
    def __init__(self):
        # Creating an empty list for menu elements; we will reassign this later
        self.LIST_TO_SORT = []

        # Storing algorithms and sizes as lists in a dictionary to be able to use them later on
        self.menu_elements = {
            'Sorting Algorithms': [
                ('Selection Sort', (Visualize.selection_sort, Algorithm.selection_sort, [self.LIST_TO_SORT,])),
                ('Insertion Sort', (Visualize.insertion_sort, Algorithm.insertion_sort, [self.LIST_TO_SORT,])),
                ('Bubble Sort', (Visualize.bubble_sort, Algorithm.bubble_sort, [self.LIST_TO_SORT,])),
                ('Merge Sort', (Visualize.merge_sort, Algorithm.merge_sort, [self.LIST_TO_SORT,])),
                ('Quick Sort', (Visualize.quick_sort, Algorithm.quick_sort, [self.LIST_TO_SORT, 0, len(self.LIST_TO_SORT) - 1])),
                ('Heap Sort', (Visualize.heap_sort, Algorithm.heap_sort, [self.LIST_TO_SORT,]))
            ],
            'List Sizes': [10, 30, 50, 80, 100, 200]
        }

        # Setting the current menu page to 1, which is the Algorithms menu
        self.current_page = 1
        self.selected = [None, None]

    # Executing the first menu and waiting for clicks on buttons
    def setup(self):
        self.create_menu('Sorting Algorithms')
        self.screen.onscreenclick(self.check_click)
        self.screen.mainloop()
    
    # Creating a screen and adjusting its features
    def create_screen(self):
        self.screen = Screen()
        self.screen.colormode(255)
        self.screen.title('Sorting Algorithms')
        self.screen.setup(width=1600, height=900, starty=0)
        self.screen.bgcolor('#212A3E')
        self.screen.update()

        # Disabling the tracer to control and update the screen manually
        self.screen.tracer(0)
        return self.screen

    # Creating the menu for the given parameter
    def create_menu(self, page):
        # Creating a turtle to handle drawings and texts on the screen
        self.turtle = Turtle('turtle')
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.speed(8)
        self.turtle.pensize(4)
        self.turtle.goto(0, 300)
        self.turtle.color('#9EB8D9')
        self.turtle.write('SORTING ALGORITHM VISUALIZER', align='center', font=('Times New Roman', 35, 'bold'))

        self.turtle.goto(0, 150)
        self.turtle.color('#9EB8D9')
        self.turtle.write(f'Choose {page}', align='center', font=('Times New Roman', 28, 'italic'))
        
        # Button naming and drawing borders around them
        for i, value in enumerate(self.menu_elements[page]):
            x = -350 + (i % 3) * 350
            y = 0 if i < 3 else -200
            
            self.turtle.goto(x - 120, y - 12)
            self.turtle.pendown()
            self.turtle.color('#6096B4')
            for j in range(2):
                self.turtle.forward(240)
                self.turtle.left(90)
                self.turtle.forward(60)
                self.turtle.left(90)

            self.turtle.penup()
            self.turtle.goto(x, y)
            self.turtle.color('#93BFCF')
            text = f'{value[0]}' if page == 'Sorting Algorithms' else f'{value}'
            self.turtle.write(text, align='center', font=('Times New Roman', 24, 'italic'))

    # Checking click events
    def check_click(self, x, y):
        # If already on page 1(algorithm menu) and any button clicked, the program goes for the next page
        if self.current_page == 1:
            for i in range(6):
                if self.button_clicked(x, y, i):
                    # Assigning i as the selected algorithm
                    self.selected[0] = i
                    self.screen.clear()
                    self.create_screen()
                    self.current_page = 2
                    self.create_menu('List Sizes')
                    self.screen.onscreenclick(self.check_click)
                    break

        # If on page 2(size menu) and any button clicked, the program starts visualizing
        elif self.current_page == 2:
            for i in range(6):
                if self.button_clicked(x, y, i):
                    # Assigning i as the selected size
                    self.selected[1] = i
                    self.start_visualize()
                    
                    # Right after the visualization, wait for a click to shut the program down
                    self.screen.exitonclick()
                    break

    # Checking if clicks are on buttons
    def button_clicked(self, x, y, index):
        x1 = -350 + (index % 3) * 350
        y1 = 0 if index < 3 else -200

        return x1 - 120 < x < x1 + 120 and y1 - 12 < y < y1 + 48
    
    # Executing visualization based on chosen algorithm and size
    def start_visualize(self):
        # Creating N sized random list and assigning it to already defined LIST_TO_SORT 
        N = self.menu_elements['List Sizes'][self.selected[1]] 
        self.LIST_TO_SORT = random.sample(range(N), N)
        
        # Recreating screen and showing the random list
        self.screen.clear()
        self.create_screen()
        Visualize.show_array(self.LIST_TO_SORT)

        # Sorting Algorithm and Size info on top left
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.color('#9EB8D9')
        turtle.goto(-750, 380)
        turtle.write(f'{self.menu_elements["Sorting Algorithms"][self.selected[0]][0]} - {N}', font=('Times New Roman', 32, 'italic'))

        # Getting functions and parameters for the chosen algorithm
        visualize_func, algorithm_func, parameters = self.menu_elements['Sorting Algorithms'][self.selected[0]][1]
        
        # Reassigning list to prevent sorting an empty list 
        parameters[0] = self.LIST_TO_SORT
        if len(parameters) > 2:
            parameters[2] = len(self.LIST_TO_SORT) - 1
        
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
        self.screen.update()
