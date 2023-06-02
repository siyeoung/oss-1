# -*- coding: utf-8 -*-
"""py0518.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W59D4wJiQz6fA5mwEDRwBruTuZplFaJi
"""

#인덱싱 / 슬라이싱
alist = [10,20,30,40,50]

temp = alist[1]
blist = alist[0:3]
clist = alist[:3]
dlist = alist[3:]
elist = alist[:]

alist = [10,20,30,40,50]

print(min(alist))
print(max(alist))
print(sum(alist))

alist = [1,21,5,6,45,22,30]
blist = sorted(alist)
print(blist)

alist = [1,21,5,6,45,22,30]
blist = sorted(alist, reverse = True)
print(blist)

import matplotlib.pyplot as plt
import random

numbers = []
for i in range(10):
  numbers.append(random.randint(1,10))

plt.plot(numbers, 'g--')
plt.ylabel('random numbers')
plt.show()

import matplotlib.pyplot as plt
import random

numbers = []
for i in range(1, 11):
  numbers.append(i*i)

plt.plot(numbers, 'g--')
plt.ylabel('random numbers')
plt.show()

import statistics as sta

sample = [2,3,3,4,5,5,5,5,5,5,6,6,6,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8]

print(f'입력 리스트 = {sample}')
print(f'평균 = {sta.mean(sample)}')
print(f'중간값 = {sta.median(sample)}')
print(f'최빈값 = {sta.mode(sample)}')
print(f'표준편차 = {sta.stdev(sample)}')

s = "You said some winds blow forever and i didn't understand"
slist = s.split()
print(slist)

remove_word = ['some', 'forever']

for word in slist:
  if word in remove_word:
    slist.remove(word)

print(slist)

phone_book = {'홍길동': 1234, '이순신' : 1235, '강감찬': 1236}

phoneNumber = phone_book['홍길동']
phone_book['홍길동'] = 9999
print(phone_book)

phone_book = {'홍길동': 1234, '이순신' : 1235, '강감찬': 1236}

aList = [10,20,30,40,50]

print(aList[0])
print(phone_book['강감찬'])
keyList = phone_book.keys()
valueList = phone_book.values()