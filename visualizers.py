from blocks import Block
from turtle import *
import time

VALUE, BLOCK = 0, 1
class Visualize():
    START_X = -650
    blocks = []

    @classmethod
    def create_screen(cls):
        cls.screen = Screen()
        cls.screen.title('Sorting Algorithms')
        cls.screen.setup(width=1600, height=900, starty=0)
        cls.screen.bgcolor('black')
        cls.screen.tracer(0)
    

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
