'''This program visualizes Sorting Algorithms depending on the chosen algorithm and list size.
Algorithms: Selection Sort, Insertion Sort, Bubble Sort, Merge Sort, Quick Sort, Heap Sort
Sizes: 10, 30, 50, 80, 100, 200 
'''
from app import VisualizerApp
from visualizers import Visualize

# Creates the Visualizer App to be able to execute screen related functions
app = VisualizerApp()

# Creating the screen
screen = app.create_screen()

# Getting screen to be able to execute visualization on the same screen
Visualize.get_screen(screen)

# Creates the first menu and waits for the click to go to the next page
app.setup()
