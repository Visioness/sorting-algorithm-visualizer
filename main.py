from visualizers import Visualize
from algorithms import Algorithm
import random
import time


#input = input("Please provide the name of a sorting algorithm and a positive integer representing the length of the list you'd like to visualize being sorted.\nname, number: ").split(",")
input = ('selection sort', '10000')
sorting_algorithm = input[0].strip()
N = int(input[1].strip())
RANDOM_LIST = random.sample(range(N), N)
LIST_TO_SORT = RANDOM_LIST[:]


#Visualize.create_screen()
#Visualize.show_list(LIST_TO_SORT)

match(sorting_algorithm.lower()):
    case 'selection sort':
        start = time.perf_counter()
        #vis_time_elapsed = Visualize.selection_sort(LIST_TO_SORT)
        Algorithm.selection_sort(LIST_TO_SORT)
        time_elapsed = time.perf_counter() - start

    case 'insertion sort':
        start = time.perf_counter()
        #vis_time_elapsed = Visualize.insertion_sort(LIST_TO_SORT)
        Algorithm.insertion_sort(LIST_TO_SORT)
        time_elapsed = time.perf_counter() - start

    case 'bubble sort':
        start = time.perf_counter()
        #vis_time_elapsed = Visualize.bubble_sort(LIST_TO_SORT)
        Algorithm.bubble_sort(LIST_TO_SORT)
        time_elapsed = time.perf_counter() - start

    case 'merge sort':
        start = time.perf_counter()
        #vis_time_elapsed = Visualize.merge_sort(LIST_TO_SORT)
        Algorithm.merge_sort(LIST_TO_SORT)
        time_elapsed = time.perf_counter() - start


print(f'''Visualize elapsed time: {time_elapsed:.010f} seconds
Algorithm elapsed time: {time_elapsed:.010f} seconds
List length: {N}''')
