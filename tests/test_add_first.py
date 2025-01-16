from activity.main import ListNode, is_equal, add_first
import pytest

def test_add_first_existing_list():
    #Arrange
    list = ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))
    new_node = ListNode(1, None)

    #Act
    resulting_list = add_first(list, new_node)

    #Assert
    expected_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    assert is_equal(resulting_list, expected_list)

def test_add_first_empty_list():
    #Arrange
    list = None
    new_node = ListNode(42, None)

    #Act
    resulting_list = add_first(list, new_node)

    #Assert
    assert resulting_list is None

def test_add_first_single_list():
    #Arrange
    list = ListNode(64, None)
    new_node = ListNode(32, None)

    #Act
    resulting_list = add_first(list, new_node)

    #Assert
    expected_list = ListNode(32, ListNode(64, None))
    assert is_equal(resulting_list, expected_list)