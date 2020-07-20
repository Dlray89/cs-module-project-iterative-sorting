# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    #loop through the array
    for i in range(len(arr)):
    # set current index
        current = i
    #loop through again to capmare each element
        for j in range(i + 1, len(arr)):
        # if the arr current index is high than the compare array
            if arr[current] > arr[j]:
            #set new current to the next index
                current = j
        # swap here if true
        arr[i], arr[current] = arr[current], arr[i]
        

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    """
    an optimized version of bubble sort algorithm
    """
    #travesre through arr
    for i in range(len(arr)):
        #compare each element to the first arr
        for j in range(len(arr) - i - 1):

            #keep track of swapping
            swapped = True
            #sort in ascending order
            if arr[j] > arr[j + 1]:
                # swap fi element is greater t the rear position
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                swapped = False

                # if there is no swap in the last swap then array is sorted
                if swapped:
                    break


    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    maximum = len(arr)


    # init the count array
    count = [0] * maximum

    #store count of ea
    # ch element in count array
    for j in range(maximum):
        count[j] += 1
    
    i = 0
    for j in range(maximum):
        for x in range(count[i]):
            arr[i] = j
            i += 1



    return arr
