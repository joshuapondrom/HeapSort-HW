import matplotlib.pyplot as plot
from time import sleep
from random import randint
from heapq import *

plot.ion()
plot.show()

a = 0
b = 100

def display(array):
	plot.clf()
	sleep(0.1)
	plot.bar(range(len(array)),array)
	plot.draw()
	sleep(0.1)

def fillarray(array):
	return[randint(a,b) for i in range(len(array))]

def heapsort(array):
	heap = []
	sortedarray = []
	for element in array:
		heappush(heap, element)
	for i in range(len(heap)):
		sortedarray.append(heappop(heap))
		print('Sorted: {} Unsorted Heap: {}'.format(sortedarray,heap))
		display(sortedarray)
	return sortedarray

array = [9,8,7,6,5,4,3,2,1]#*100
display(array)
sleep(2)
array = fillarray(array)
print(array)
array = heapsort(array)
print(array)
sleep(2)
