# Pavlo Yatluk
# dz_13
# 2. Додайте до завд 1 код алгоритму сортування з функцією, яка - б обраховувала
# середній час роботи алгоритму сортування.

import time
import random

l = []
n = int(input())
for i in range(n):

    my_list = []
    for i in range(0, 5000):
        my_list.append(random.randint(1, 1000))
    print("Sorting List:", my_list)

    cur_time = time.time()
    length = len(my_list)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if my_list[jIndex] > my_list[jIndex + 1]:
               my_list[jIndex], my_list[jIndex + 1] = my_list[jIndex + 1], my_list[jIndex]
               swapped = True
        if not swapped:
            break

    a = time.time() - cur_time
    l.append(a)

print(l)
print(sum(l)/len(l))


















