# -*- coding: utf-8 -*-
"""Task 02 [Parrt-02].ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jISb8JDpAoZJQ96FIMlFx645d333t-us
"""

# Task 2   [part-2]

# read the file
f = open("input2.txt","r")
# generate a output file by running the code
f2 = open("output2.txt","w")

# read the array size of Alice
N = int(f.readline())
# read the array of Alice
array1 = f.readline().split(" ")
array1 = list(map(int, array1))     # Convert ['1','2'] to [1,2]

# read the array size of Bob
M = int(f.readline())
# read the array of Bob
array2 = f.readline().split(" ")
array2 = list(map(int, array2))     # Convert ['1','2'] to [1,2]

new = []
p1 = 0
p2 = 0

for i in range(N+M):
  if p1 < N and p2 < M:
    if (array1[p1]) < (array2[p2]):
      new.append(array1[p1])
      p1 += 1
    else:
      new.append(array2[p2])
      p2 += 1

if p2 < M:
  new.extend(array2[p2:])
elif p1 < N:
  new.extend(array2[p1:])

f2.write(" ".join(str(num) for num in new))

# Must Close the file
f2.close()