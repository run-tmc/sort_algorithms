# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:58:57 2017

@author: trevo
"""

"""Quicksort"""
"""Best and Average Runtime Complexity => O(NLogN)"""
"""Worst Runtime Complexity => O(N^2) when pivot value is lowest or highest value"""
"""Space Complexity: In-place => O(1)"""

def quicksort(array_list,start,end):
    # Check if two or more elements
    if (start<end):
        # Create partition point
        pvt_pt = partition(array_list,start,end)
        # Sort right half
        quicksort(array_list,start,(pvt_pt-1))
        # Sort left half
        quicksort(array_list,(pvt_pt+1),end)
        
def partition(array_list,start,end):
    top = end
    pivot = array_list[top]
    bottom = start - 1
    for k in range(start,top):
        if (array_list[k]<=pivot):
            bottom += 1
            swap(array_list,k,bottom)
    swap(array_list,top,(bottom+1))
    return (bottom+1)
    
def swap(array_list,start,end):
    array_list[start],array_list[end] = array_list[end],array_list[start]

array_list = [4,2,7]
print"Inital Array", array_list
quicksort(array_list,0,(len(array_list)-1))
print "Sorted Array", array_list



