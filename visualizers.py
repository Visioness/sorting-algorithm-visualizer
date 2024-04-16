'''Visualizing anything related with the chosen array.
'''
from blocks import Block
from turtle import *
import time

# VALUE, BLOCK values to zip array items and their blocks(turtles) on the screen, in some situations
VALUE, BLOCK = 0, 1
class Visualize():
    # Delays for the sleep functions
    DELAY = 0.02
    START_X = -750
    
    # Creating a list where each array item is represented as a turtle block
    blocks = []
    screen = None
    
    # Width of each block in pixels
    width = None

    # Wid and len coefs for each block
    wid_coef = None
    len_coef = None

    # Space between blocks in pixels
    space = 4


    # Getting screen from Visualizer App
    @classmethod
    def get_screen(cls, screen):
        cls.screen = screen
    

    # Calculating wid_coef and len coef, then showing the array in the screen 
    @classmethod
    def show_array(cls, arr):
        n = len(arr)
        cls.width = (1500 - (n - 1) * cls.space) / n
        cls.interval = cls.space + cls.width
        cls.wid_coef = cls.width / 20
        cls.len_coef = 800 / (n + 1) / 20
        cls.START_X += cls.width / 2

        # Appending blocks list n times, with the freshly created Block
        for i in range(n):
            cls.blocks.append(Block(len_coef=(cls.len_coef + arr[i] * cls.len_coef), xcor=(cls.START_X + cls.interval * i), wid_coef=cls.wid_coef))
        cls.screen.update()

    
    # VISUALIZATIONS 
    # Changing color of the current block, changing block length and block positions to create a similar effect with the algorithms

    # Visualising Selection Sort
    @classmethod
    def selection_sort(cls, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                cls.blocks[j].color('red')
                cls.screen.update()
                time.sleep(cls.DELAY)
                if arr[j] < arr[min_index]:
                    min_index = j
                cls.blocks[j].color('white')

            arr[min_index], arr[i] = arr[i], arr[min_index]
            cls.blocks[min_index], cls.blocks[i] = cls.blocks[i], cls.blocks[min_index]
            cls.blocks[min_index].setx(cls.START_X + cls.interval * min_index)
            cls.blocks[i].setx(cls.START_X + cls.interval * i)
            cls.screen.update()


    # Visualising Insertion Sort
    @classmethod
    def insertion_sort(cls, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            block_key = cls.blocks[i]
            block_key.color('red')
            cls.screen.update()
            j = i - 1

            while j >= 0 and key < arr[j]:
                cls.blocks[j].setx(cls.START_X + cls.interval * (j + 1))
                cls.blocks[j + 1].setx(cls.START_X + cls.interval * j)
                cls.blocks[j], cls.blocks[j + 1] = cls.blocks[j + 1], cls.blocks[j]
                cls.screen.update()
                time.sleep(cls.DELAY)
                arr[j + 1] = arr[j]
                j -= 1

            block_key.color('white')
            arr[j + 1] = key
    

    # Visualising Bubble Sort
    @classmethod
    def bubble_sort(cls, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                cls.blocks[j].color('red')
                cls.screen.update()
                time.sleep(cls.DELAY)

                if arr[j] > arr[j + 1]:
                    cls.blocks[j].setx(cls.START_X + cls.interval * (j + 1))
                    cls.blocks[j + 1].setx(cls.START_X + cls.interval * j)
                    cls.blocks[j], cls.blocks[j + 1] = cls.blocks[j + 1], cls.blocks[j]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    cls.blocks[j + 1].color('white')

                else:
                    cls.blocks[j].color('white')

                cls.screen.update()
    

    # Visualising Merge Sort
    @classmethod
    def merge_sort(cls, arr, offset=0):
        n = len(arr)
        if n > 1: 
            mid = n // 2
            
            # Left and right halves
            L = list(zip(arr[:mid], cls.blocks[offset:offset + mid]))
            R = list(zip(arr[mid:], cls.blocks[offset + mid:offset + n]))

            # Applying Merge Sort recursively on the left and right halves
            cls.merge_sort(L, offset)
            cls.merge_sort(R, offset + mid)
            
            i = j = k = 0
            while k < n:
                if not (j < len(R)) or i < len(L) and L[i][VALUE] < R[j][VALUE]:
                    L[i][BLOCK].color('red')
                    cls.blocks[k + offset] = L[i][BLOCK]
                    arr[k] = L[i][VALUE]
                    i += 1

                else:
                    R[j][BLOCK].color('red')
                    cls.blocks[k + offset] = R[j][BLOCK]
                    arr[k] = R[j][VALUE]
                    j += 1

                cls.screen.update()
                time.sleep(cls.DELAY)
                cls.blocks[k + offset].setx(cls.START_X + cls.interval * (k + offset))
                cls.blocks[k + offset].color('white')
                k += 1
                cls.screen.update()


    # Visualising Quick Sort
    @classmethod
    def quick_sort(cls, arr, start, end):
        if start >= end:
            return
        
        low = start
        high = end - 1
        mid = (start + end) // 2

        # Median of three method for the pivot
        if arr[start] <= arr[mid] <= arr[end] or arr[end] <= arr[mid] <= arr[start]:
            pivot = arr[mid]
            index = mid
        elif arr[mid] <= arr[start] <= arr[end] or arr[end] <= arr[start] <= arr[mid]:
            pivot = arr[start]
            index = start
        elif arr[start] <= arr[end] <= arr[mid] or arr[mid] <= arr[end] <= arr[start]:
            pivot = arr[end]
            index = end
        
        # Visualising pivot selection
        for i in [start, mid, end]:
            cls.blocks[i].color('orange')
        cls.screen.update()
        time.sleep(cls.DELAY)

        # Coloring current portion
        for i in range(start, end + 1):
            cls.blocks[i].color('grey')

        # Changing pivot with the last element
        cls.blocks[index].color('yellow')
        cls.screen.update()
        time.sleep(cls.DELAY)
        if index != end:
            cls.blocks[index].setx(cls.START_X + cls.interval * end)
            cls.blocks[end].setx(cls.START_X + cls.interval * index)
            cls.blocks[index], cls.blocks[end] = cls.blocks[end], cls.blocks[index]
            arr[index], arr[end] = arr[end], arr[index]
            cls.screen.update()

        while True:
            # Coloring lower values as green
            cls.blocks[low].color('green')
            cls.screen.update()
            while low <= high and arr[low] <= pivot:
                cls.blocks[low + 1].color('green')
                time.sleep(cls.DELAY)
                cls.screen.update()
                low = low + 1

            # Coloring higher values as purple        
            cls.blocks[high].color('purple')
            cls.screen.update()
            while low <= high and arr[high] >= pivot:
                cls.blocks[high - 1].color('purple')
                time.sleep(cls.DELAY)
                cls.screen.update()
                high = high - 1

            # If there's a lower value between highers or a higher value between lowers, they will change positions
            if low <= high:
                time.sleep(cls.DELAY)
                cls.blocks[low].setx(cls.START_X + cls.interval * high)
                cls.blocks[high].setx(cls.START_X + cls.interval * low)
                cls.blocks[low].color('purple')
                cls.blocks[high].color('green')
                cls.screen.update()
                cls.blocks[low], cls.blocks[high] = cls.blocks[high], cls.blocks[low]
                arr[low], arr[high] = arr[high], arr[low]

            # Recolor the remaining purple or green blocks back to the white
            else:
                cls.blocks[low].color('white')
                cls.blocks[high].color('white')
                break
        
        # Repositioning the pivot back to the correct position
        cls.blocks[low].setx(cls.START_X + cls.interval * end)
        cls.blocks[end].setx(cls.START_X + cls.interval * low)
        cls.blocks[low], cls.blocks[end] = cls.blocks[end], cls.blocks[low]
        arr[low], arr[end] = arr[end], arr[low]
        time.sleep(cls.DELAY)
        cls.blocks[low].color('white')
        cls.screen.update()

        # Applying Quick Sort recursively on the left and right portion
        cls.quick_sort(arr, start, low - 1)
        cls.quick_sort(arr, low + 1, end)


    # Visualizing Heap Sort
    @classmethod
    def heap_sort(cls, arr):
        n = len(arr)
        # Heapifying non-leaf elements
        for i in range(n//2, -1, -1):
            cls.heapify(arr, n, i)
        cls.screen.update()

        # Repositioning the MAX value as the last element, then heapify remaining to find the next MAX value
        for i in range(n-1, 0, -1):
            cls.blocks[i].setx(cls.START_X + cls.interval * 0)
            cls.blocks[0].setx(cls.START_X + cls.interval * i)
            cls.blocks[0].color('white')
            cls.blocks[i], cls.blocks[0] = cls.blocks[0], cls.blocks[i]
            cls.screen.update()
            arr[i], arr[0] = arr[0], arr[i]
            cls.heapify(arr, i, 0)

    # Transforming into a Max Heap
    @classmethod
    def heapify(cls, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        # Coloring current subtree
        if r < n:
            for j in [i, l, r]:
                cls.blocks[j].color('orange')
            cls.screen.update()

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r
        
        # Coloring the largest of the subtree
        if r < n:
            cls.blocks[largest].color('red')
            cls.screen.update()
            time.sleep(cls.DELAY)

        # If largest is not the root, then change the positions
        if largest != i:
            cls.blocks[largest].setx(cls.START_X + cls.interval * i)
            cls.blocks[i].setx(cls.START_X + cls.interval * largest)
            cls.blocks[i], cls.blocks[largest] = cls.blocks[largest], cls.blocks[i]
            cls.screen.update()
            time.sleep(cls.DELAY)
            arr[i], arr[largest] = arr[largest], arr[i]

        # Coloring subtree back to the white
        if r < n:
            for j in [i, l, r]:
                cls.blocks[j].color('white')
            cls.screen.update()

        # Applying heapify recursively to the root
        if largest != i:
            cls.heapify(arr, n, largest)
