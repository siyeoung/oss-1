# -*- coding: utf-8 -*-
"""Untitled7 25304.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17rV4fItOWOSu4DiYJXES5NRDROb7OAlR
"""

x = int(input())
sum = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b

print("Yes") if sum == x else print("No")