from activity.main import ListNode, is_equal, get_last_two_nodes
import pytest

def test_get_last_two_nodes_existing_list():
    #Arrange
    list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

    #Act
    resulting_previous, resulting_current = get_last_two_nodes(list)

    #Assert
    expected_previous = ListNode(4, ListNode(5, None))
    expected_current = ListNode(5, None)

    assert is_equal(resulting_previous, expected_previous)
    assert is_equal(resulting_current, expected_current)

def test_get_last_two_nodes_single_list():
    #Arrange
    list = ListNode(42,None)

    #Act
    resulting_previous, resulting_current = get_last_two_nodes(list)

     #Assert
    expected_previous = None
    expected_current = ListNode(42, None)

    assert is_equal(resulting_previous, expected_previous)
    assert is_equal(resulting_current, expected_current)

def test_get_last_two_nodes_list_with_two_values():
    #Arrange
    list = ListNode(42, ListNode(43, None))

    #Act
    resulting_previous, resulting_current = get_last_two_nodes(list)

    #Assert
    expected_current = ListNode(43, None)

    assert is_equal(resulting_previous, list)
    assert is_equal(resulting_current, expected_current)