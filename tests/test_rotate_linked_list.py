from activity.main import ListNode, is_equal, rotate_list
import pytest

def test_rotate_list_twice():
    #Arrange
    list = ListNode(5, ListNode(3, ListNode(4, ListNode(2))))
    k = 2

    #Act
    resulting_list = rotate_list(list, k)

    # Assert
    expected_list = ListNode(4, ListNode(2, ListNode(5, ListNode(3))))
    assert is_equal(resulting_list, expected_list)

def test_rotate_list_eight_times():
    # Arrange
    list = ListNode(22, ListNode(100, ListNode(55, ListNode(94, ListNode(7)))))
    k = 8

    # Act
    resulting_list = rotate_list(list, k)

    # Assert
    expected_list = ListNode(55, ListNode(94, ListNode(7, ListNode(22, ListNode(100)))))
    assert is_equal(resulting_list, expected_list)

def test_rotate_list_no_rotation():
    # Arrange
    list = ListNode(3, ListNode(5, ListNode(7)))
    k = 0

    # Act
    resulting_list = rotate_list(list, k)

    # Assert
    expected_list = ListNode(3, ListNode(5, ListNode(7)))
    assert is_equal(resulting_list, expected_list)

def test_rotate_list_single_rotation():
    # Arrange
    list = ListNode(3, ListNode(5, ListNode(7)))
    k = 1

    # Act
    resulting_list = rotate_list(list, k)

    # Assert
    expected_list = ListNode(7, ListNode(3, ListNode(5)))
    assert is_equal(resulting_list, expected_list)