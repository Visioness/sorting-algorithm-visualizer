import time


class Algorithm():
    @classmethod
    def selection_sort(cls, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
    

    @classmethod
    def insertion_sort(cls, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    

    @classmethod
    def bubble_sort(cls, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    

    @classmethod
    def merge_sort(cls, arr):
        n = len(arr)
        if n > 1:
            mid = n // 2
            L = arr[:mid]
            R = arr[mid:]

            cls.merge_sort(L)
            cls.merge_sort(R)
            
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr


    @classmethod
    def quick_sort(cls, arr, start, end):
        low = start
        high = end - 1

        if start >= end:
            return
        
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
            
        # Changing pivot with the last element
        if index != end:
            arr[index], arr[end] = arr[end], arr[index]

        while True:
            while low <= high and arr[low] <= pivot:
                low = low + 1
            while low <= high and arr[high] >= pivot:
                high = high - 1
            
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
            else:
                break

        arr[low], arr[end] = arr[end], arr[low]
        
        cls.quick_sort(arr, start, low - 1)
        cls.quick_sort(arr, low + 1, end)