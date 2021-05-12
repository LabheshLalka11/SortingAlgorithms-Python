'''
The Time Complexity  of Merge Sort is :  O(n*Log n) 
The Space Complexity of Merge Sort is : O(n)
'''



array = [5,4,2,6,8,-1]

def MergeSort(array):
    if len(array)<=1:
        return array 
    else:
        mid = len(array)//2
        l_array = array[:mid]
        r_array = array[mid:]
        
        MergeSort(l_array)
        MergeSort(r_array)
        
        
        i = 0
        j = 0
        k = 0
        
        while i < len(l_array) and j < len(r_array):
            if l_array[i]<r_array[j]:
                array[k] = l_array[i]
                i = i +1
            else:
                array[k] = r_array[j]
                j = j+1
            
            k = k+1
            
        while i<len(l_array):
            array[k] = l_array[i]
            i = i+1 
            k = k+1 
        
        while j<len(r_array):
            array[k] = r_array[j]
            j = j+1 
            k = k+1 
        
MergeSort(array)
print("Merge Sort Technique:",array) 
        
