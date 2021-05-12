'''
The Time Complexity of Quick Sort Algorithm is : O(n log n)
The Time Complexity of Quick Sort Algorithm is :  O(log n)
'''


array = [5,4,2,6,8,-1]

def Quicksort(array):
    
    if len(array)<=1:
        return array
    else:
        pivot = array.pop()
        
    left_array =[]
    right_array = []
    for item in array:
        if item < pivot:
            left_array.append(item)
        else:
            right_array.append(item)
    
    return Quicksort(left_array)+[pivot]+Quicksort(right_array)

result=Quicksort(array)
print("Quick Sort Technique:",result)
