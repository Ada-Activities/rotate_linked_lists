class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# DO NOT MODIFY - This function is used to print a linked list, and can be used for testing.
def stringify_list(head):
    result = ''
    while head:
        result += f'{head.value}'
        if head.next:
            result += ' -> '
        head = head.next
    return result

# DO NOT MODIFY - This function is used to test if two linked lists are equal.
def is_equal(list1, list2):
    while list1:
        if not list2:
            return False
        if list1.value != list2.value:
            return False
        list1 = list1.next
        list2 = list2.next
    if list2 != None:
        return False
    return True
    

def add_first(old_head, node):
    if not old_head:
        return None
    node.next = old_head
    return node

def get_last_two_nodes(head):
    previous = None
    current = head

    while current.next:
        previous = current
        current = current.next

    return previous, current


def rotate_list(head, k):
    # if the list does not exist, return None
    if not head:
        return None

    # if k < 0, raise an error
    if k < 0:
        raise ValueError("k must be greater than or equal to 0")
    
    # if k is 0 or if the list has one element, return the head of the list
    elif k == 0 or head.next is None:
        return head

    # loop k times
    for i in range(k):
        # set the new tail and new head to the last two nodes of the list
        new_tail, new_head = get_last_two_nodes(head)
        # the new tail's next reference will now be set to None
        new_tail.next = None
        # the head of the list is set to the old tail (new head)
        head = add_first(head, new_head)
    # after making k rotations, return the new head of the list
    return head