import pylab
from time import sleep
from random import randint
from heapq import *

a = 0
b = 100

def fillarray(array):
	return[randint(a,b) for i in range(len(array))]

def heapsort(array):
	imgidx = 0
	heap = []
	sortedarray = []
	for element in array:
		heappush(heap, element)
	for i in range(len(heap)):
		sortedarray.append(heappop(heap))
		pylab.plot(range(len(sortedarray)),sortedarray,'k.',markersize=6)
		pylab.savefig("heapsort/img" +'%04d' %imgidx +".png")
		pylab.clf()
		imgidx = imgidx + 1
		print('Sorted: {} Unsorted Heap: {}'.format(sortedarray,heap))
	return sortedarray

array = [9,8,7,6,5,4,3,2,1]#*100
array = fillarray(array)
print(array)
array = heapsort(array)
print(array)
