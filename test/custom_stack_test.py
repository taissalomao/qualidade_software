import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException

def test_initialization_of_stack():
    stack = CustomStack(3)
    assert stack.size() == 0
    assert stack.isEmpty() == True

def test_push_to_stack():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.size() == 1
    assert stack.top() == 1

def test_pop_from_stack():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.pop() == 1
    assert stack.isEmpty() == True

def test_top_of_stack():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.top() == 1
    stack.push(2)
    assert stack.top() == 2

def test_stack_full_exception_case():
    stack = CustomStack(1)
    stack.push(1)
    with pytest.raises(StackFullException):
        stack.push(2)

def test_stack_empty_exception_case_pop():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_stack_empty_exception_case_top():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.top()
