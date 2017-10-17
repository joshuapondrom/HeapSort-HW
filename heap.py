import matplotlib.pyplot as plt
from time import sleep
from random import randint
from heapq import *

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []

a = 0
b = 100

def display(array):
	xs.append(range(len(array)))
	ys.append(array)
	#plot.bar(range(len(array)),array)

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
array = fillarray(array)
print(array)
array = heapsort(array)
print(array)
ax1.clear()
ax1.plot(xs,ys)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
