# Implement binary search using recursion.

list_test = [2, 3, 4, 10, 40]
element = 7
low = 0
high = len(list_test) - 1

def recursion_search(list_test, low, high, element):

    if high >= low: # main condition of the search
        middle = (high + low) // 2
        if list_test[middle] == element: # checking if the element is in the middle of the list
            return middle

        elif list_test[middle] > element: # if element is smaller then the middle - it is in the left part of the list
            return recursion_search(list_test, low, middle - 1, element)
        else:
            return recursion_search(list_test, middle + 1, high, element) # and the opposite

    else:
        print("The element is not in the list") # if element is not in the list




result = recursion_search(list_test, low, high, element)

print(result)


