import matplotlib.pyplot as plt
import numpy as np
import time
import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def run_comparison():
    try:
        input_size = int(input_size_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input size. Please enter an integer.")
        return
    
    x = np.arange(0, input_size+1)
    
    bubble_sort_times = [measure_sorting_time(bubble_sort, np.random.randint(1, 1000, n)) for n in x]
    selection_sort_times = [measure_sorting_time(selection_sort, np.random.randint(1, 1000, n)) for n in x]
    insertion_sort_times = [measure_sorting_time(insertion_sort, np.random.randint(1, 1000, n)) for n in x]
    merge_sort_times = [measure_sorting_time(merge_sort, np.random.randint(1, 1000, n)) for n in x]
    quick_sort_times = [measure_sorting_time(quick_sort, np.random.randint(1, 1000, n)) for n in x]

    plt.figure(figsize=(12, 8))
    plt.plot(x, bubble_sort_times, label='Bubble Sort')
    plt.plot(x, selection_sort_times, label='Selection Sort')
    plt.plot(x, insertion_sort_times, label='Insertion Sort')
    plt.plot(x, merge_sort_times, label='Merge Sort')
    plt.plot(x, quick_sort_times, label='Quick Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

def measure_sorting_time(sorting_function, arr):
    start_time = time.time()
    sorting_function(arr)
    return time.time() - start_time

# Create GUI
root = tk.Tk()
root.title("Sorting Algorithms Comparison")

# Input size entry
input_size_label = tk.Label(root, text="Enter maximum input size:")
input_size_label.pack()
input_size_entry = tk.Entry(root, width=50)
input_size_entry.pack()

# Run button
run_button = tk.Button(root, text="Run Comparison", command=run_comparison)
run_button.pack()

root.mainloop()
