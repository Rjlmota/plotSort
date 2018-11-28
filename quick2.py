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
  pivot = arr[random.randint(low, high)]
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
#arr = randomize(1000)
#bucketSort(arr)
#print(arr)


arr = [x for x in range(100, 1001, 100)]
arr.append(10000)
for i in range(100000, 1000001, 100000): arr.append(i)


## PRIMEIRA QUESTÃO
'''
data = randomize(100)
print("RANDOM::")
print(data)
print("SORTED::QUICKSORT")
print(data)
'''
'''
data = randomize(100000, 'random')
print(data)
start_time = time.clock()
quicksort(data, 0, len(data)-1)
end_time = time.clock()
print(end_time - start_time, end = '\n')
print(data)
'''


#Segunda questão

'''
print("length\trandom\tsorted\treversed\n")
for i in arr:
  #True random
  total_time = 0
  print(str(i), end = '\t')
  for j in range(5):
    data = randomize(i)
    start_time = time.time()
    quicksort(data, 0, len(data)-1)
    end_time = time.time()
    total_time += end_time - start_time  
  print(total_time/5, end = '\t')

  #Sorted
  data = randomize(i, 'sorted')
  start_time = time.time()
  quicksort(data, 0, len(data)-1)
  end_time = time.time()
  print(end_time - start_time, end = '\t')
  
  #Reverse Sorted
  data = randomize(i, 'reversed')
  start_time = time.time()
  quicksort(data, 0, len(data)-1)
  end_time = time.time()
  print(end_time - start_time, end='\n')

'''
'''
print("length\trandom\tsorted\treversed\n")


for i in arr:
  #True random
  total_time = 0
  print(str(i), end = '\t')
  for j in range(5):
    data = randomize(i)
    start_time = time.time()
    quicksort(data, 0, len(data)-1)
    end_time = time.time()
    total_time += end_time - start_time  
  print(total_time/5, end = '\t')

  #Sorted
  data = randomize(i, 'sorted')
  start_time = time.time()
  quicksort(data, 0, len(data)-1)
  end_time = time.time()
  print(end_time - start_time, end = '\t')
  
  #Reverse Sorted
  data = randomize(i, 'reversed')
  start_time = time.time()
  quicksort(data, 0, len(data)-1)
  end_time = time.time()
  print(end_time - start_time, end='\n')

'''
'''
for i in range(100000, 1000000, 100000):
  #True random
  print(str(i), end ='\t')
  data = randomize(i)
  start_time = time.clock()
  quicksort(data, 0, len(data)-1)
  end_time = time.clock()
  print(end_time - start_time, end = '\t')

  #Sorted
  data = randomize(i, 'sorted')
  start_time = time.clock()
  quicksort(data, 0, len(data)-1)
  end_time = time.clock()
  print(end_time - start_time, end = '\t')
  
  #Reverse Sorted
  data = randomize(i, 'reversed')
  start_time = time.clock()
  quicksort(data, 0, len(data)-1)
  end_time = time.clock()
  print(end_time - start_time, end='\n')




#Terceira questão
print("random\tsorted\treversed\n")
for i in range(1000, 1000000, 1000):
  #True random
  data = randomize(i)
  start_time = time.clock()
  heapsort(data, 0, len(data)-1)
  end_time = time.clock()
  print(end_time - start_time, end = '\t')

  #Sorted
  data = randomize(i, 'sorted')
  start_time = time.clock()
  heapsort(data, 0, len(data)-1)
  end_time = time.clock()
  print(end_time - start_time, end = '\t')
  
  #Reverse Sorted
  data = randomize(i, 'reversed')
  start_time = time.clock()
  heapsort(data, 0, len(data)-1)
  end_time = time.clock()
  print(end_time - start_time, end='\n')
'''


print("length\tuniform\tnrandom\tlowCap\tunbalanced\n")
#for i in range(1000, 1000000, 1000):
for i in arr:
  print(str(i), end='\t')
  
  #uniform
  total_time = 0
  for j in range(5):
    data = randomize(i, 'uniform')
    start_time = time.time()
    bucketSort(data)
    end_time = time.time()
    total_time += end_time - start_time
  print(total_time/5, end='\t')
  
  #not uniform

  total_time = 0
  for j in range(5):
    data = randomize(i, 'random')
    start_time = time.time()
    bucketSort(data)
    end_time = time.time()
    total_time += end_time - start_time
  print(total_time/5, end='\t')
  

  '''  
  data = randomize(i, 'lowCap')
  start_time = time.time()
  bucketSort(data)
  end_time = time.time()
  print(end_time - start_time, end='\t')
  
  data = randomize(i, 'lowCap2')
  start_time = time.time()
  bucketSort(data)
  end_time = time.time()
  print(end_time - start_time, end='\t')

  data = randomize(i, 'lowCap3')
  start_time = time.time()
  bucketSort(data)
  end_time = time.time()
  print(end_time - start_time, end='\t')
' '''
  
  data = randomize(i, 'lowCap')
  start_time = time.time()
  bucketSort(data)
  end_time = time.time()
  print(end_time - start_time, end='\t')
  
  
  data = randomize(i, 'lowCapMax2')
  start_time = time.time()
  bucketSort(data)
  end_time = time.time()
  print(end_time - start_time, end='\n')

  '''

arr = np.random.uniform(0, 1000, 100000)
print(arr)
bucketSort(arr)
print(arr)
'''