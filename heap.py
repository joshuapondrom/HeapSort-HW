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
	#Blank array to store sorted list
	sortedarray =[]
	#Loop through every element in original list
	for element in array:
		#Put all elements into a heap
		heappush(heap, element)
	#Loop for length of our heap
	for i in range(len(heap)):
		#Add top element of heap to the sorted array
		#Heappop also heapifies after popping the element
		sortedarray.append(heappop(heap))
	#Returns our sorted list
	return sortedarray
		
#Initializes a array of size n
array = [0]*n
#Fills our array with random values
array = fillarray(array)
print(array) #Unsorted
array = heapsort(array)
print(array) #Sorted
