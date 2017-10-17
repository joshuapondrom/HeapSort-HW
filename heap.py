import sys
from time import sleep
from random import randint
from heapq import *

#If there is system arguments, first is min value, second is max
# third is the amount of elements in list, if there is none
# defualt to 0, 100, and 10 respectively
if(len(sys.argv) == 3):
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	n = int(sys.argv[3])
else:
	a = 0
	b = 100
	n = 10

#Fills our array with random values
def fillarray(array):
	return[randint(a,b) for i in range(len(array))]


def heapsort(array):
	#Initializes a blank heap
	heap = []
	for element in array:
		#Pushes every element in heap
		heappush(heap,element)
	#Returns a list of all elements popped off heap
	return [heappop(heap) for i in range(len(heap))]

#Initializes a array of size n
array = [0]*n
#Fills our array with random values
array = fillarray(array)
print(array) #Unsorted
array = heapsort(array)
print(array) #Sorted
