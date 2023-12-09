import pytest

from advent_of_code import day_1

input_1_day_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
output_day_1_star_1 = 142

day_1_star_1_test_input = [(input_1_day_1, output_day_1_star_1)]


@pytest.mark.parametrize("puzzle_input, output", day_1_star_1_test_input)
def test_day_1_star_1(puzzle_input, output):
    assert day_1.compute_star_1(puzzle_input) == output
