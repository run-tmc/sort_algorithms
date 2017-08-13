# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:38:30 2017

@author: trevo
"""

class MaxHeap:
    length = 0
    array_list = []
    def __init__(self,length,array_list):
        self.length = length
        self.array_list = array_list

#Create swap function
def swap(maxheap,i,j):
    maxheap.array_list[i],maxheap.array_list[j] = maxheap.array_list[j],maxheap.array_list[i]
    
def heapify(maxheap,N):
    largest = N
    # Index of left child
    left = (2*N) + 1
    # Index of right child
    right = (2*N) + 2
    if ((left<maxheap.length) and (maxheap.array_list[left]>maxheap.array_list[largest])):
        largest = left
    if ((right<maxheap.length) and (maxheap.array_list[right]>maxheap.array_list[largest])):
        largest = right
    if (largest != N):
        swap(maxheap,largest,N)
        heapify(maxheap,largest)
    return maxheap
    
def createHeap(array_list, N):
    maxheap = MaxHeap(N, array_list)
    i = (int)((maxheap.length - 2)/2)
    while (i >= 0):
        maxheap = heapify(maxheap,i)
        i -=1
    return maxheap
    
def heapsort(array_list):
    N = len(array_list)
    #Create a heap
    heap = createHeap(array_list,N)
    # Repeat
    while (heap.length > 1):
        swap(heap, 0, (heap.length - 1))
        heap.length -= 1
        heapify(heap,0)
    return heap.array_list
    
array_list = [4,2,7]
print "Unsorted", array_list
array_list = heapsort(array_list)
print "Heap Sorted", array_list
