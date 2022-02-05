# https://stackabuse.com/python-linked-lists/

class ListNode:
    def __init__(self, data):  # constructor to initiate this object

        self.data = data # store data
        self.next = None #store reference (next item)
        return

    def has_value(self, value):     #method to compare the value with the node data
        if self.data == value:
            return True
        else:
            return False

node_01 = ListNode(15)
node_02 = ListNode(8.2)
node_03 = ListNode("Berlin")

print(node_01, node_02, node_03)
print(node_01)


class SingleLinkedList:
    def __init__(self): #constructor to initiate this object
        self.head = None
        self.tail = None
        return



# Adding to the list is done via add_list_item().
# This method requires a node as an additional parameter.
# To maek sure it is a proper node(an instance of class ListNode)
# the parameter is first verified using the built in Python function
# isinstance(). If successful, the node will be added at the end
# of the list. If item is not a ListNode, then one is created.


# In case the list is (still) empty the new node becomes
# the head of the list.
# If a node is already in the list, then the value
# of tail is adjusted accordingly.

    def add_list_item(self, item):
        # add an item at the end of the list
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return