from typing import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)


data = (1.234, 2.3, 4.0)  # mypy will not raise error
data = (1, 2, 4)  # mypy will not raise error
sum_even_numbers(data)


# context in type inference
def foo(arg: list[int]):
    return "".join(str(i) for i in arg)


foo([])  # empty list [] type inferred as list[int]
a: list[int] = []
foo(a)


variable = "example"
print(variable.trim())  # type: ignore[attr-defined]
