n = int(input())

q = ["Howard", "Rajesh", "Penny", "Leonard", "Sheldon"]

def enqueue(q, element):
    return q.insert(0, element)

def dequeue(q):
    return q.pop()

for i in range(n):
    drinker = dequeue(q)
    enqueue(q, drinker)
    enqueue(q, drinker)

print(drinker)
    

