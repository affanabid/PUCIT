import matplotlib.pyplot as plt
import numpy as np
import time

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

# Take input size from user
n = int(input("Enter the maximum input size (n): "))

# Initialize arrays to store input sizes and corresponding times
input_sizes = []
bubble_sort_times = []
selection_sort_times = []

# Loop through input sizes from 1 to n
for i in range(1, n+1):
    # Generate a random array of size i
    arr = np.random.randint(1, 100, i)
    
    # Measure time complexity for Bubble Sort
    start_time = time.time()
    bubble_sort(arr.copy())
    bubble_sort_time = time.time() - start_time
    
    # Measure time complexity for Selection Sort on the same array
    start_time = time.time()
    selection_sort(arr.copy())
    selection_sort_time = time.time() - start_time
    
    # Append input size and time taken to the arrays
    input_sizes.append(i)
    bubble_sort_times.append(bubble_sort_time)
    selection_sort_times.append(selection_sort_time)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the time complexity of Bubble Sort and Selection Sort
ax.plot(input_sizes, bubble_sort_times, 'bo-', label='Bubble Sort')
ax.plot(np.array(input_sizes) + 0.1, selection_sort_times, 'ro-', label='Selection Sort')

# Add labels and title
ax.set_xlabel('Input Size (n)')
ax.set_ylabel('Time (s)')
ax.set_title('Time Complexity Comparison of Bubble Sort and Selection Sort')
ax.legend()

# Display the plot
plt.show()
