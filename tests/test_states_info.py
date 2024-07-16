import pytest

from packaging_demo.states_info import is_city_capitol_of_state

print(is_city_capitol_of_state("Boise", "Idaho"))


@pytest.mark.parametrize(
    argnames="city_name, state, is_capitol",
    argvalues=[
        ("Juneau", "Alaska", True),
        ("Phoenix", "Arizona", True),
        ("Denver", "Colorado", True),
        ("Newyork", "Idaho", False),
    ],
)
def test__is_city_capitol_of_state_true_for_correct_city_state_pair(city_name: str, state: str, is_capitol: bool):
    assert is_city_capitol_of_state(city_name, state) == is_capitol


def test__is_city_capitol_of_state_false_for_correct_city_state_pair():
    assert not is_city_capitol_of_state("Newyork", "Idaho")
