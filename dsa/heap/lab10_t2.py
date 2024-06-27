import heapq

def max_product(nums):
    # Use a max heap to keep track of the largest numbers
    max_heap = [-num for num in nums]  # Negate values to simulate max heap
    heapq.heapify(max_heap)
    
    # Extract the two largest numbers
    first_max = -heapq.heappop(max_heap)  # Get the largest number
    second_max = -heapq.heappop(max_heap)  # Get the second largest number
    
    # Calculate the maximum product
    return (first_max - 1) * (second_max - 1)

# Example usage:
print(max_product([3, 4, 5, 2]))  # Output: 12
print(max_product([1, 5, 4, 5]))  # Output: 16
print(max_product([3, 7]))  # Output: 12
