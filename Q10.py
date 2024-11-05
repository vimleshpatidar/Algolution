l = [10,20,3,5,6,45,78]
k = int(input("enter a number"))

def min(l):
    min = float('inf')
    for i in l:
        if i<min:
            min = i
    return min

product = 1

for i in range(k):
    n = min(l)
    product *= n
    l.remove(n)

print(product)