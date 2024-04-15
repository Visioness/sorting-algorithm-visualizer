from visualizers import Visualize
from algorithms import Algorithm
from turtle import *
import random
import time


class VisualizerApp():
    def __init__(self):
        self.algorithms = ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']
        self.sizes = [10, 20, 40, 80, 100, 200]
        self.menu_elements = {'Sorting Algorithm': self.algorithms, 'List Size': self.sizes}
        self.current_page = 1
        self.selected = [None, None]
    
    def setup(self):
        self.create_menu('Sorting Algorithm')
        self.screen.onscreenclick(self.button_clicked)
        self.screen.mainloop()
    

    def create_screen(self):
        self.screen = Screen()
        self.screen.colormode(255)
        self.screen.title('Sorting Algorithms')
        self.screen.setup(width=1600, height=900, starty=0)
        self.screen.bgcolor('#212A3E')
        self.screen.tracer(0)
        return self.screen


    def create_menu(self, page):
        element = 'Sorting Algorithm' if page == 'Sorting Algorithm' else 'List Size'
        self.turtle = Turtle('turtle')
        self.turtle.penup()
        self.turtle.pensize(4)
        self.turtle.goto(0, 300)
        self.turtle.hideturtle()
        self.turtle.color('#9EB8D9')
        self.turtle.write('SORTING ALGORITHM VISUALIZER', align='center', font=('Times New Roman', 35, 'bold'))

        self.turtle.goto(0, 150)
        self.turtle.color('#9EB8D9')
        self.turtle.write(f'Choose {element}', align='center', font=('Times New Roman', 28, 'italic'))
        
        for i, value in enumerate(self.menu_elements[element]):
            if i % 3 == 0:
                x = -350
            elif i % 3 == 1:
                x = 0
            else:
                x = 350

            if i < 3:
                y = 0
            else:
                y = -200
            
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
            self.turtle.write(f'{value}', align='center', font=('Times New Roman', 24, 'italic'))

    
    def button_clicked(self, x, y):
        if self.current_page == 1:
            for i in range(6):
                if self.check_click(x, y, i):
                    self.selected[0] = i
                    self.screen.clear()
                    self.create_screen()
                    self.current_page = 2
                    self.create_menu('List Size')
                    self.screen.onscreenclick(self.button_clicked)

        
        elif self.current_page == 2:
            for i in range(6):
                if self.check_click(x, y, i):
                    self.selected[1] = i
                    self.current_page = 0
                    self.start_visualize()

        else:
            pass


    def check_click(self, x, y, index):
        x1 = -350 + (index % 3) * 350
        y1 = 0 if index < 3 else -200

        return x1 - 120 < x < x1 + 120 and y1 - 12 < y < y1 + 48
    

    def start_visualize(self):
        N = self.sizes[self.selected[1]]
        RANDOM_LIST = random.sample(range(N), N)
        LIST_TO_SORT = RANDOM_LIST[:]
        if N <= 80:
            self.screen.clear()
            self.create_screen()
            Visualize.show_list(LIST_TO_SORT)
        vis_time_elapsed = 0
        match(self.algorithms[self.selected[0]].lower()):
            case 'selection sort':
                if N <= 80:
                    vis_start = time.perf_counter()
                    Visualize.selection_sort(LIST_TO_SORT)
                    vis_time_elapsed = time.perf_counter() - vis_start
                
                alg_start = time.perf_counter()
                sorted_list = Algorithm.selection_sort(LIST_TO_SORT)
                alg_time_elapsed = time.perf_counter() - alg_start

            case 'insertion sort':
                if N <= 80:
                    vis_start = time.perf_counter()
                    Visualize.insertion_sort(LIST_TO_SORT)
                    vis_time_elapsed = time.perf_counter() - vis_start
                
                alg_start = time.perf_counter()
                sorted_list = Algorithm.insertion_sort(LIST_TO_SORT)
                alg_time_elapsed = time.perf_counter() - alg_start

            case 'bubble sort':
                if N <= 80:
                    vis_start = time.perf_counter()
                    Visualize.bubble_sort(LIST_TO_SORT)
                    vis_time_elapsed = time.perf_counter() - vis_start
                
                alg_start = time.perf_counter()
                sorted_list = Algorithm.bubble_sort(LIST_TO_SORT)
                alg_time_elapsed = time.perf_counter() - alg_start

            case 'merge sort':
                if N <= 80:
                    vis_start = time.perf_counter()
                    Visualize.merge_sort(LIST_TO_SORT)
                    vis_time_elapsed = time.perf_counter() - vis_start
                
                alg_start = time.perf_counter()
                sorted_list = Algorithm.merge_sort(LIST_TO_SORT)
                alg_time_elapsed = time.perf_counter() - alg_start

            case 'quick sort':
                if N <= 80:
                    vis_start = time.perf_counter()
                    Visualize.quick_sort(LIST_TO_SORT, 0, len(LIST_TO_SORT) - 1)
                    vis_time_elapsed = time.perf_counter() - vis_start
                
                alg_start = time.perf_counter()
                sorted_list = Algorithm.quick_sort(LIST_TO_SORT, 0, len(LIST_TO_SORT) - 1)
                alg_time_elapsed = time.perf_counter() - alg_start

            case 'heap sort':
                if N <= 80:
                    vis_start = time.perf_counter()
                    Visualize.heap_sort(LIST_TO_SORT)
                    vis_time_elapsed = time.perf_counter() - vis_start
                
                alg_start = time.perf_counter()
                sorted_list = Algorithm.heap_sort(LIST_TO_SORT)
                alg_time_elapsed = time.perf_counter() - alg_start

        print(f'''Visualize elapsed time: {vis_time_elapsed:.010f} seconds
Algorithm elapsed time: {alg_time_elapsed:.010f} seconds
List length: {N}''')