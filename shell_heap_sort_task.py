import random
import timeit


def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n / 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(int(gap), n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= int(gap) and arr[j - int(gap)] > temp:
                arr[j] = arr[j - int(gap)]
                j -= int(gap)

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap /= 2


# function build Max Heap where value
# of each child is always smaller
# than value of their parent
def buildMaxHeap(arr, n):
    for i in range(n):
        # if child is bigger than parent
        if arr[i] > arr[int((i - 1) / 2)]:
            j = i
            # swap child and parent until
            # parent is smaller
            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j], arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],arr[j])
                j = int((j - 1) / 2)

def heapSort(arr, n):
    buildMaxHeap(arr, n)
    for i in range(n - 1, 0, -1):
        # swap value of first indexed
        # with last indexed
        arr[0], arr[i] = arr[i], arr[0]
        # maintaining heap property
        # after each swapping
        j, index = 0, 0

        while True:
            index = 2 * j + 1
            # if left child is smaller than
            # right child point index variable
            # to right child
            if (index < (i - 1) and
                    arr[index] < arr[index + 1]):
                index += 1
            # if parent is smaller than child
            # then swapping parent with child
            # having higher value
            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]

            j = index
            if index >= i:
                break

def generate_files(size):
    # Open the file for writing

    f1 = open('random_list' + str(size) + '.txt', 'w')
    f2 = open('normal_list' + str(size) + '.txt', 'w')
    f3 = open('reverse_list' + str(size) + '.txt', 'w')

    numbers = []
    for i in range(0, size):
        numbers.append(i)
    random.shuffle(numbers)

    for i in numbers:
        f1.writelines(str(i) + "\n")
    f1.close()

    for i in range(0, size):
        f2.writelines(str(i) + "\n")
    f2.close()

    for i in range(0, size).__reversed__():
        f3.writelines(str(i) + "\n")
    f3.close()

    # The reason why we used a list comprehension
    # is that we wanted to convert the numbers to
    # strings so that they can be written to disk

    # Close the file


if __name__ == '__main__':
    generate_files(25)
    generate_files(50)
    generate_files(200)
    generate_files(500)

    f1 = open('random_list500.txt', 'r')
    f2 = open('normal_list500.txt', 'r')
    f3 = open('reverse_list500.txt', 'r')

    arr1 = []
    arr2 = []
    arr3 = []

    for l in f1.readlines():
        arr1.append(int(l))

    for l in f2.readlines():
        arr2.append(int(l))

    for l in f3.readlines():
        arr3.append(int(l))


    # Shell Sorting Report

    print("Shell Sort on Random 500 Integers: ")
    start = timeit.default_timer()
    shellSort(arr1)
    end = timeit.default_timer()
    print("Time Taken to sort (seconds): ", end-start)
    for i in arr1:
        print(arr1[i], end=" ")
    print()

    print("\nShell Sort on Normal 500 Integers: ")
    start = timeit.default_timer()
    shellSort(arr2)
    end = timeit.default_timer()
    print("Time Taken to sort (seconds): ", end - start)
    for i in arr2:
        print(arr2[i], end=" ")
    print()

    print("\nShell Sort on Reverse 500 Integers: ")
    start = timeit.default_timer()
    shellSort(arr3)
    end = timeit.default_timer()
    print("Time Taken to sort (seconds): ", end - start)
    for i in arr3:
        print(arr3[i], end=" ")
    print()

    # Heap Sorting Report

    print("\nHeap Sort on Random 500 Integers: ")
    start = timeit.default_timer()
    heapSort(arr1, len(arr1))
    end = timeit.default_timer()
    print("Time Taken to sort (seconds): ", end - start)
    for i in arr1:
        print(arr1[i], end=" ")
    print()

    print("\nHeap Sort on Normal 500 Integers: ")
    start = timeit.default_timer()
    heapSort(arr2, len(arr2))
    end = timeit.default_timer()
    print("Time Taken to sort (seconds): ", end - start)
    for i in arr2:
        print(arr2[i], end=" ")
    print()

    print("\nHeap Sort on Reverse 500 Integers: ")
    start = timeit.default_timer()
    heapSort(arr3, len(arr3))
    end = timeit.default_timer()
    print("Time Taken to sort (seconds): ", end - start)
    for i in arr3:
        print(arr3[i], end=" ")
    print()

