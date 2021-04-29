'''
The Time Complexity of Bubble Sort Algorithm is O(n2)
The Space Complexity of Bubble Sort Algorithm is O(1)
'''


array = [5,4,2,6,8,-1]
print(" Sorting Techniques")

def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range (i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                
    print("Bubble Sort Technique:",array)
    
bubbleSort(array)
