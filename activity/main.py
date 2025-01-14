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
    """
    This function takes in two nodes, the old_head node will be the node that was previously the head of the list, the `node` will be the node that will replace the old head of the list.
  
    Parameters:
    old_head (ListNode): old head of the linked list
    node (ListNode): node to be set to the new head of the list
  
    Returns:
    ListNode: the new head of the list
    """
    pass

def get_last_two_nodes(head):
    """
    This function accepts the head of a linked list and returns the last two nodes in the linked list.
  
    Parameters:
    head (ListNode): the head of the linked list from which we want to find the last two nodes
  
    Returns:
    tuple(ListNode, ListNode): the last two nodes of the linked list, in the order in which they appear in the list
    """
    pass


def rotate_list(head, k):
    """
    This function accepts the head of a linked list, `head`, and the amount of rotations to perform on the list, `k`.

    Given the `head` and `k` rotations, return the new head of the linked list.
  
    Parameters:
    head (ListNode): the head of the linked list from which we want to find the last two nodes
    k (int): the number of times to rotate the linked list
  
    Returns:
    ListNode: the new head of the linked list after k rotations
    """
    pass