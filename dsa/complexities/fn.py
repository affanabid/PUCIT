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
        input_sizes = list(map(int, input_sizes_entry.get().split()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input sizes. Please enter integers separated by spaces.")
        return
    
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []
    merge_sort_times = []
    quick_sort_times = []

    for n in input_sizes:
        arr = np.random.randint(1, 1000, n)
        
        start_time = time.time()
        bubble_sort(arr.copy())
        bubble_sort_times.append(time.time() - start_time)
        
        start_time = time.time()
        selection_sort(arr.copy())
        selection_sort_times.append(time.time() - start_time)
        
        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_sort_times.append(time.time() - start_time)
        
        start_time = time.time()
        merge_sort(arr.copy())
        merge_sort_times.append(time.time() - start_time)
        
        start_time = time.time()
        quick_sort(arr.copy())
        quick_sort_times.append(time.time() - start_time)

    # Plotting the time complexities
    plt.figure(figsize=(12, 8))
    plt.plot(input_sizes, bubble_sort_times, 'bo-', label='Bubble Sort')
    plt.plot(input_sizes, selection_sort_times, 'ro-', label='Selection Sort')
    plt.plot(input_sizes, insertion_sort_times, 'go-', label='Insertion Sort')
    plt.plot(input_sizes, merge_sort_times, 'yo-', label='Merge Sort')
    plt.plot(input_sizes, quick_sort_times, 'mo-', label='Quick Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create GUI
root = tk.Tk()
root.title("Sorting Algorithms Comparison")

# Input sizes entry
input_sizes_label = tk.Label(root, text="Enter input sizes separated by spaces:")
input_sizes_label.pack()
input_sizes_entry = tk.Entry(root, width=50)
input_sizes_entry.pack()

# Run button
run_button = tk.Button(root, text="Run Comparison", command=run_comparison)
run_button.pack()

root.mainloop()
