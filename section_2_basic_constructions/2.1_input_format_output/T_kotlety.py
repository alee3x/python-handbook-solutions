n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

x1 = ((m - k2) * n) // (k1 - k2)
x2 = n - x1

print(x1, x2)
