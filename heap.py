from time import sleep
from random import randint
from heapq import *

a = 0
b = 100

def fillarray(array):
	return[randint(a,b) for i in range(len(array))]

def heapsort(array):
	heap = []
	for element in array:
		heappush(heap,element)
	return [heappop(heap) for i in range(len(heap))]

array = [0]
sleep(2)
array = fillarray(array)
print(array)
array = heapsort(array)
print(array)
sleep(2)
