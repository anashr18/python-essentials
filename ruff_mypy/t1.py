import os
from typing import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)


data = (1.234, 2.3, 4.0)
data = (1, 2, 4)
sum_even_numbers(data)
