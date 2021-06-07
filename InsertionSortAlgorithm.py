'''
 The time complexity of Insertion sort is : O(n²)
 The Space complexity of Insertion sort is : O(1)
'''


array = [5,4,2,6,8,-1]

def Insertionsort(array):
    for i in range(1,len(array)):
        current_value = array[i]
        position = i 
    while(position>0 and current_value<array[position-1]):
        array[position],array[position-1]=array[position-1],array[position]
        position = position-1 
    print("Insertion Sort Technique:",array)
    
Insertionsort(array)
