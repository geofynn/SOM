import math
from math import exp

a = float(input())
b = float(input())
c = (a ** 2) + (b ** 2)
print(c)

n = 100
a = 0.0
b = 1.0
h = (b - a) / n
area = 0.5*h*( exp(-(a ** 2)) + exp(-(b ** 2)))
for i in range(n):
    x = a + i * h
    area = area + (h * exp(-(x ** 2)))

print('Der Wert der Approximation ist', area)
