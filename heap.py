import pylab
from time import sleep
from random import randint
from heapq import *

a = 0
b = 100
n = 100
img = 1

def fillarray(array):
	return[randint(a,b) for i in range(len(array))]

def swap(array, first, second):
	array[first], array[second] = array[second], array[first]

def heapify(array, end, i):
	global img
	pylab.plot(range(len(array)),array,'k.',markersize=6)
	pylab.savefig("heapsort/img" + '%04d' %img + ".png")
	pylab.clf()
	img = img + 1

	left = 2 * i + 1
	right = 2 * (i + 1)
	maxvalue = i
	if left < end and array[i] < array[left]:
		maxvalue = left
	if right < end and array[maxvalue] < array[right]:
		maxvalue = right
	if maxvalue != i:
		swap(array, i, maxvalue)
		heapify(array, end, maxvalue)	

def heapsort(array):
	end = len(array)
	start = end // 2 - 1
	for i in range(start, -1, -1):
		heapify(array, end, i)
	for i in range(end-1, 0, -1):
		swap(array, i, 0)
		heapify(array, i, 0)
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
