"""
The Time Complexity of Selection Sort is O(n2)
The Space Complexity of Selection Sort is O(1)
"""

array = [5,4,2,6,8,-1]
print(" Sorting Techniques")

def selectionSort(array):
    for i in range(0,len(array)):
        min_index = i 
        for j in range(i+1,len(array)):
            if array[min_index]>array[j]:
                min_index = j 
        array[i],array[min_index] = array[min_index],array[i]
        
print("Selection Sort Technique:",array)
