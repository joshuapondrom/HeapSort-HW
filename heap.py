import pylab
from time import sleep
from random import randint
from heapq import *

#lowest val
a = 0
#highest val
b = 100
#number of elements
n = 100
#for storing visualization
img = 1

def fillarray(array):
	return[randint(a,b) for i in range(len(array))]

def swap(array, first, second):
	array[first], array[second] = array[second], array[first]

def maxheapify(array, end, i):
	#visualization vv
	global img
	pylab.plot(range(len(array)),array,'k.',markersize=6)
	pylab.savefig("heapsort/img" + '%04d' %img + ".png")
	pylab.clf()
	img = img + 1
	#visualization ^^

	left = 2 * i + 1
	right = 2 * (i + 1)
	maxvalue = i
	if left < end and array[i] < array[left]:
		maxvalue = left
	if right < end and array[maxvalue] < array[right]:
		maxvalue = right
	if maxvalue != i:
		swap(array, i, maxvalue)
		maxheapify(array, end, maxvalue)	

def heapsort(array):
	#Invariant: array is a unsorted list
	end = len(array)
	# '//' is integer division in python
	start = end // 2 - 1
	#This loop makes the array into a max heap
	for i in range(start, -1, -1):
		maxheapify(array, end, i)
	#Array is a max heap right now
	#This loop goes through the elements of the heap and puts them
	# at the end, then does not heapify the elements taken out
	for i in range(end-1, 0, -1):
		#Invariant: array[0] is the maximum value of a heap
		#           which is array[0] through array[i]
		swap(array, i, 0)
		#Invariant: maximum value of heap is now moved out
		#	    of the heap and into the sorted section
		maxheapify(array, i, 0)
		#Invariant: array[0] through array[i] now satisfies
		#           heap conditions
	#Invariant: Heap is now empty and there is a fully sorted list
	return array

#def heapsort(array):
#	imgidx = 0
#	heap = []
#	sortedarray = []
#	for element in array:
#		heappush(heap, element)
#	for i in range(len(heap)):
#		sortedarray.append(heappop(heap))
#		pylab.plot(range(len(sortedarray)),sortedarray,'k.',markersize=6)
#		pylab.savefig("heapsort/img" +'%04d' %imgidx +".png")
#		pylab.clf()
#		imgidx = imgidx + 1
#		print('Sorted: {} Unsorted Heap: {}'.format(sortedarray,heap))
#	return sortedarray

array = [0]*n
array = fillarray(array)
print(array)
heapsort(array)
print(array)
