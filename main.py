from visualizers import Visualize
from algorithms import Algorithm
import random
import time


#input = input("Please provide the name of a sorting algorithm and a positive integer representing the length of the list you'd like to visualize being sorted.\nname, number: ").split(",")
input = ('heap sort', '80')
sorting_algorithm = input[0].strip()
N = int(input[1].strip())
RANDOM_LIST = random.sample(range(N), N)
LIST_TO_SORT = RANDOM_LIST[:]

if N <= 80:
    screen = Visualize.create_screen()
    Visualize.show_list(LIST_TO_SORT)

vis_time_elapsed = 0
match(sorting_algorithm.lower()):
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

screen.exitonclick()
screen.mainloop()