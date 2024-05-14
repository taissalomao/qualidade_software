import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from number.number import NumberAscOrder
from custom_stack.custom_stack_class import CustomStack

def test_sort_with_numbers():
    stack = CustomStack(6)
    numbers = [5, 3, 6, 2, 1, 4]
    for number in numbers:
        stack.push(number)
    
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == sorted(numbers)

def test_sort_empty_stack():
    stack = CustomStack(6)
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == []

def test_sort_invalid_input():
    with pytest.raises(TypeError):
        NumberAscOrder.sort("not a stack")

def test_sort_with_duplicates():
    stack = CustomStack(6)
    numbers = [3, 2, 3, 1, 2, 1]
    for number in numbers:
        stack.push(number)
    
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 1, 2, 2, 3, 3]

def test_sort_reverse_order():
    stack = CustomStack(6)
    numbers = [6, 5, 4, 3, 2, 1]
    for number in numbers:
        stack.push(number)
    
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 2, 3, 4, 5, 6]

def test_sort_with_duplicates_and_reverse_order():
    stack = CustomStack(6)
    numbers = [6, 5, 6, 4, 5, 3]
    for number in numbers:
        stack.push(number)
    
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [3, 4, 5, 5, 6, 6]

def test_sort_empty_stack_after_sorting():
    stack = CustomStack(6)
    sorted_numbers = NumberAscOrder.sort(stack)
    assert stack.isEmpty()