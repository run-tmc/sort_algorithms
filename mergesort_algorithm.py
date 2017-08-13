# -*- coding: utf-8 -*-
"""
Created on Mon May 08 20:50:32 2017

@author: trevo
"""

"""Mergesort Function"""
"""Best, Average, Worst Runtime Complexity => O(NLogN)"""
"""Space Complexity => O(N)"""
# Function arguments are the array_list to sort; start array index; end array index
def merge_sort(array_list,start,end):
    # Initialize mid_point array index to zero(0)
    mid_point = 0
    # Check index value are valid
    if (start<end):
        # Determine array mid point index value
        mid_point = (start+end)/2
        # Create left branch sub arrays
        merge_sort(array_list,start,mid_point)
        # Create right branch sub array
        merge_sort(array_list,(mid_point + 1),end)
        merge_subarrays(array_list, start, mid_point, end)
        
# Function arguments are the sub array to sort; start sub array index; 
# mid point sub array index; end sub array index
def merge_subarrays(sub_array,start, mid_point, end):
    # Initialize variable "N" to the length of the sub array
    N = len(sub_array)
    # Initialize temporary array list with zero based on the length of the sub array
    temp = [0]*N
    lt = start
    rt = end
    m = mid_point+1
    k=lt
    while ((lt<=mid_point) and (m<=rt)):
        if (sub_array[lt]<=sub_array[m]):
            temp [k]=sub_array[lt]
            lt+=1
        else:
            temp [k]=sub_array[m]
            m+=1
        k+=1
        
    while (lt<=mid_point):
        temp[k]=sub_array[lt]
        k+=1
        lt+=1
            
    while (m<=rt):
        temp[k]=sub_array[m]
        k+=1
        m+=1
    # Update array with sorted sub_list
    for sort_index in range(start,(end+1)):
        sub_array[sort_index]=temp[sort_index]
    print sub_array

merge_sort([4,2,7],0,2)
     