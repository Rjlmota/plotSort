import random
import time
import sys
import math
import numpy as np

sys.setrecursionlimit(10000)

def randomize(size, spec = 'random'):
  arr = []
  if(spec == 'random'):
    for i in range(size):
      arr.append(random.randint(0, size))

  elif(spec == 'sorted'):
    for i in range(size):
      arr.append(i)

  elif(spec == 'reversed'):
    for i in reversed(range(size)):
      arr.append(i)


  elif(spec == 'uniform'):
    arr = np.random.uniform(0, size/2, size)


  elif(spec == 'notUniform'):
    for i in (range(size)):
      if (random.uniform(0, 1) > 0.5):
        arr.append(random.randint(0, int(size/2)))
      else:
        arr.append(random.randint(0, size))

  elif(spec == 'lowCap'):
    for i in range(size):
      arr.append(random.randint(0, int(size/4)))

  elif(spec == 'lowCap2'):
    for i in range(size):
      arr.append(random.randint(0, int(size/8)))

  elif(spec == 'lowCap3'):
    for i in range(size):
      arr.append(random.randint(0, int(size/16)))

  elif(spec == 'lowCapMax'):
    for i in range(size):
      arr.append(random.randint(0, 10000))

  elif(spec == 'lowCapMax2'):
    for i in range(size):
      if(random.uniform(0, 1) > 0.9):
        arr.append(random.randint(int(size/4), size))
      else:
        arr.append(random.randint(0, int(size/4)))




  return arr

def countingsort( aList, k):
  counter = [0] * ( k + 1 )
  for i in aList:
    counter[i] += 1

  ndx = 0;
  for i in range( len( counter ) ):
    while 0 < counter[i]:
      aList[ndx] = i
      ndx += 1
      counter[i] -= 1

def partition(arr, low, high):
  pivot = arr[high]
  i = (low-1) #Index of smaller element
  
  for j in range(low, high):
    if(arr[j] <= pivot):
      i+=1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1

def quicksort(arr, low, high):
  if(low < high):
    pi = partition(arr, low, high)

    ##print(arr)
    quicksort(arr, low, pi-1)
    quicksort(arr, pi+1, high)


def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapsort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 




def insertionSort(array):
  for i in range(1, len(array)):
    tmp = 0
    tmp = array[i]
    position = i
    while position > 0 and array[position - 1] > tmp:
      array[position] = array[position - 1]
      position -= 1
    array[position] = tmp

def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result
 
def re_hashing(i, code ):
  return int(i/code[0]*(code[1]-1))


def bucketSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        insertionSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
    ndx += 1
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapsort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 



def countingsort( aList, k):
  counter = [0] * ( k + 1 )
  for i in aList:
    counter[i] += 1

  ndx = 0;
  for i in range( len( counter ) ):
    while 0 < counter[i]:
      aList[ndx] = i
      ndx += 1
      counter[i] -= 1


arr = [x for x in range(100, 1000, 100)]
arr.append(10000)
for i in range(100000, 1000001, 100000): arr.append(i)



print("Random array: ")
arr = randomize(100, 'random')
print(arr)
print("\n------\n------\n")
print("Quicksorted:")
quicksort(arr, 0, 99)
print(arr)
