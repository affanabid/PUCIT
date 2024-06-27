n = input()
# for i in range(n):
strengths = list(map(int, input().split()))

array = strengths[:]
for i in range(1, len(array)):
    key = array[i]
    j = i - 1

    while j >= 0 and array[j] > key:
        array[j+1] = array[j]
        j -= 1
    
    array[j+1] = key

mx1 = array[-1]
mx2 = array[-2]

adv = [0] * len(strengths)

for  i in range(len(strengths)):
    if mx1 == strengths[i]:
        diff = strengths[i] - mx2
    else:
        diff = strengths[i] - mx1
    adv[i] = diff

print(adv)

