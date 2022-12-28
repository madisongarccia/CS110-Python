import random   #Import module for generating random numbers
import time     #Import module for getting the current time

maxvalue = 100000

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # to change direction of sort, change direction of comparison
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def insertion_sort(array):
    for slot in range(1, len(array)):
        value = array[slot]
        test_slot = slot - 1
        while test_slot > -1 and array[test_slot] > value:
            array[test_slot + 1] = array[test_slot]
            test_slot = test_slot - 1
        array[test_slot + 1] = value
    return array

def bubble_sort(array):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        index -= 1
    return array

def main():
    List1 = [random.randrange(1, maxvalue+1, 1) for i in range(0,maxvalue+1)]
    startTime=time.time()
    merge_sort(List1)
    endTime=time.time()
    elapsedTime=endTime-startTime
    print('selection sort:' , elapsedTime)

    List2=[random.randrange(1, maxvalue+1, 1) for i in range(0,maxvalue+1)]
    startTime=time.time()
    insertion_sort(List2)
    endTime=time.time()
    elapsedTime=endTime-startTime
    print('insertion sort:' , elapsedTime)

    List3=[random.randrange(1, maxvalue+1, 1) for i in range(0,maxvalue+1)]
    startTime=time.time()
    bubble_sort(List3)
    endTime=time.time()
    elapsedTime=endTime-startTime
    print('bubble sort:' , elapsedTime)

    #ADD CODE to compare the three list-sorting functions
    #  See Canvas assignment for details.

main()
