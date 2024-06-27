from collections import Counter
import heapq

def frequency_sort(s: str) -> str:
    freq = Counter(s)
    
    max_heap = []
    for char, count in freq.items():
        data = (-count, char)
        max_heap.append(data)

    heapq.heapify(max_heap)
    
    result = ''
    while max_heap:
        count, char = heapq.heappop(max_heap)
        f = char * -count
        result  += str(f)
    
    return result

s1 = "tree"
s2 = "cccaaa"
s3 = "Aabb"
print(frequency_sort(s1))  
print(frequency_sort(s2))  
print(frequency_sort(s3))  
