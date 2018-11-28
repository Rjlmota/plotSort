import random
import time
import sys
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

  elif(spec == 'lowCapMax'):
    for i in range(size):
      arr.append(random.randint(0, 10))

  return arr

def partition(arr, low, high):
  pivot = arr[int((low+high)/2)]
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

## PRIMEIRA QUESTÃO
'''
data = randomize(100)
print("RANDOM::")
print(data)
print("SORTED::QUICKSORT")
print(data)
'''
'''
data = randomize(10000, 'random')
start_time = time.clock()
quicksort(data, 0, len(data)-1)
end_time = time.clock()
print(end_time - start_time, end = '\n')
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
#Terceira questão
'''
'''
arr = [x for x in range(100, 1000, 100)]
arr.append(10000)
for i in range(100000, 1000001, 100000): arr.append(i)

'''
print("length\trandom\tsorted\treversed\n")
for i in arr:
  #True random
  print(i, end='\t')
  total_time = 0
  for j in range(5):
    data = randomize(i)
    start_time = time.time()
    heapsort(data)
    end_time = time.time()
    total_time += end_time - start_time
  print(total_time/5, end = '\t')

  #Sorted
  data = randomize(i, 'sorted')
  start_time = time.time()
  heapsort(data)
  end_time = time.time()
  print(end_time - start_time, end = '\t')
  
  #Reverse Sorted
  data = randomize(i, 'reversed')
  start_time = time.time()
  heapsort(data)
  end_time = time.time()
  print(end_time - start_time, end='\n')


'''
print("length\tuniform\tnotUniform\tlowCap\tlowCap2\n")
for i in arr:
  print(str(i), end = '\t')
  #uniform
  data = randomize(i, 'random')
  start_time = time.clock()
  countingsort(data, len(data))
  end_time = time.clock()
  print(end_time - start_time, end='\t')

  #not uniform
  data = randomize(i, 'notUniform')
  start_time = time.clock()
  countingsort(data, len(data))
  end_time = time.clock()
  print(end_time - start_time, end='\t')
    
  data = randomize(i, 'lowCap')
  start_time = time.clock()
  countingsort(data, int(len(data)/4))
  end_time = time.clock()
  print(end_time - start_time, end='\t')

  data = randomize(i, 'lowCap2')
  start_time = time.clock()
  countingsort(data, int(len(data)/8))
  end_time = time.clock()
  print(end_time - start_time, end='\n')
'''