from blocks import Block
from turtle import *
import time

VALUE, BLOCK = 0, 1
class Visualize():
    START_X = -650
    blocks = []
    SPEED = 0.02

    @classmethod
    def create_screen(cls):
        cls.screen = Screen()
        cls.screen.title('Sorting Algorithms')
        cls.screen.setup(width=1600, height=900, starty=0)
        cls.screen.bgcolor('black')
        cls.screen.tracer(0)
    
        return cls.screen

    @classmethod
    def show_list(cls, arr):
        for i in range(len(arr)):
            cls.blocks.append(Block(len_coef=arr[i], xcor=(cls.START_X + 15 * i)))
            cls.screen.update()


    @classmethod
    def selection_sort(cls, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                cls.blocks[j].color('red')
                cls.screen.update()
                time.sleep(0.02)
                if arr[j] < arr[min_index]:
                    min_index = j
                cls.blocks[j].color('white')

            arr[min_index], arr[i] = arr[i], arr[min_index]
            cls.blocks[min_index], cls.blocks[i] = cls.blocks[i], cls.blocks[min_index]
            cls.blocks[min_index].setx(cls.START_X + 15 * min_index)
            cls.blocks[i].setx(cls.START_X + 15 * i)
            cls.screen.update()


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
                cls.blocks[j].setx(cls.START_X + 15 * (j + 1))
                cls.blocks[j + 1].setx(cls.START_X + 15 * j)
                cls.blocks[j], cls.blocks[j + 1] = cls.blocks[j + 1], cls.blocks[j]
                cls.screen.update()
                time.sleep(0.02)
                arr[j + 1] = arr[j]
                j -= 1

            block_key.color('white')
            arr[j + 1] = key
    

    @classmethod
    def bubble_sort(cls, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                cls.blocks[j].color('red')
                cls.screen.update()
                time.sleep(0.02)

                if arr[j] > arr[j + 1]:
                    cls.blocks[j].setx(cls.START_X + 15 * (j + 1))
                    cls.blocks[j + 1].setx(cls.START_X + 15 * j)
                    cls.blocks[j], cls.blocks[j + 1] = cls.blocks[j + 1], cls.blocks[j]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    cls.blocks[j + 1].color('white')

                else:
                    cls.blocks[j].color('white')

                cls.screen.update()
    

    @classmethod
    def merge_sort(cls, arr, offset=0):
        n = len(arr)
        if n > 1: 
            mid = n // 2
            
            L = list(zip(arr[:mid], cls.blocks[offset:offset + mid]))
            R = list(zip(arr[mid:], cls.blocks[offset + mid:offset + n]))

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
                time.sleep(0.02)
                cls.blocks[k + offset].setx(cls.START_X + 15 * (k + offset))
                cls.blocks[k + offset].color('white')
                k += 1
                cls.screen.update()


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
        
        # Pivot selection
        for i in [start, mid, end]:
            cls.blocks[i].color('orange')
        cls.screen.update()
        time.sleep(cls.SPEED)

        # Coloring current portion
        for i in range(start, end + 1):
            cls.blocks[i].color('grey')

        # Changing pivot with the last element
        cls.blocks[index].color('yellow')
        cls.screen.update()
        time.sleep(cls.SPEED)
        if index != end:
            cls.blocks[index].setx(cls.START_X + 15 * end)
            cls.blocks[end].setx(cls.START_X + 15 * index)
            cls.blocks[index], cls.blocks[end] = cls.blocks[end], cls.blocks[index]
            arr[index], arr[end] = arr[end], arr[index]
            cls.screen.update()

        while True:
            cls.blocks[low].color('green')
            cls.screen.update()
            while low <= high and arr[low] <= pivot:
                cls.blocks[low + 1].color('green')
                time.sleep(cls.SPEED)
                cls.screen.update()
                low = low + 1
            
            cls.blocks[high].color('purple')
            cls.screen.update()
            while low <= high and arr[high] >= pivot:
                cls.blocks[high - 1].color('purple')
                time.sleep(cls.SPEED)
                cls.screen.update()
                high = high - 1

            if low <= high:
                time.sleep(cls.SPEED)
                cls.blocks[low].setx(cls.START_X + 15 * high)
                cls.blocks[high].setx(cls.START_X + 15 * low)
                cls.blocks[low].color('purple')
                cls.blocks[high].color('green')
                cls.screen.update()
                cls.blocks[low], cls.blocks[high] = cls.blocks[high], cls.blocks[low]
                arr[low], arr[high] = arr[high], arr[low]

            else:
                cls.blocks[low].color('white')
                cls.blocks[high].color('white')
                break

        cls.blocks[low].setx(cls.START_X + 15 * end)
        cls.blocks[end].setx(cls.START_X + 15 * low)
        cls.blocks[low], cls.blocks[end] = cls.blocks[end], cls.blocks[low]
        arr[low], arr[end] = arr[end], arr[low]
        time.sleep(cls.SPEED)
        cls.blocks[low].color('white')
        cls.screen.update()

        cls.quick_sort(arr, start, low - 1)
        cls.quick_sort(arr, low + 1, end)
