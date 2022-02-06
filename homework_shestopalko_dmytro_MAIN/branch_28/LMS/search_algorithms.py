# Linear search is one of the simplest searching algorithms, and the easiest to understand.
# We can think of it as a ramped-up version of our own implementation of Python's in operator.
#
# The algorithm consists of iterating over an array and returning the index
# of the first occurrence of an item once it is found:

def LinearSearch(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1

print(LinearSearch([1,2,3,4,5,2,1], 2))


# Linear search is not often used in practice, because the same efficiency
# can be achieved by using inbuilt methods or existing operators,
# and it is not as fast or efficient as other search algorithms.
#
# Linear search is a good fit for when we need to find the first occurrence
# of an item in an unsorted collection because unlike most other search algorithms,
# it does not require that a collection be sorted before searching begins.




# Binary search follows a divide and conquer methodology.
# It is faster than linear search but requires that the array be sorted before the algorithm is executed.

# Assuming that we're searching for a value val in a sorted array,
# the algorithm compares val to the value of the middle element of the array, which we'll call mid.
# If mid is the element we are looking for (best case), we return its index.
# If not, we identify which side of mid val is more likely to be on based on whether val is smaller or greater than mid,
# and discard the other side of the array.
# We then recursively or iteratively follow the same steps, choosing a new value for mid,
# comparing it with val and discarding half of the possible matches in each iteration of the algorithm.

# Since a good search algorithm should be as fast and accurate as possible,
# let's consider the iterative implementation of binary search:

def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first<= last) and (index == -1):
        mid = (first+last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


print(BinarySearch([10,20,30,40,50], 50))

# One drawback of binary search is that if there are multiple occurrences of an element in the array, it does not return the index of the first element, but rather the index of the element closest to the middle:


# Jump Search is similar to binary search in that it works on a sorted array,
# and uses a similar divide and conquer approach to search through it.
#
# It can be classified as an improvement of the linear search algorithm since it depends on linear search
# to perform the actual comparison when searching for a value.
#
# Given a sorted array, instead of searching through the array elements incrementally,
# we search in jumps. So in our input list lys,
# if we have a jump size of jump our algorithm will consider elements in the order lys[0], lys[0+jump],
# lys[0+2jump], lys[0+3jump] and so on.
#
# With each jump, we store the previous value we looked at and its index.
# When we find a set of values where lys[i]<element<lys[i+jump], we perform a linear search with lys[i]
# as the left-most element and lys[i+jump] as the right-most element in our search set:

