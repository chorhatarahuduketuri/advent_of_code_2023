import pytest

from advent_of_code import day_1

input_1_day_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

input_2_day_1 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

output_day_1_star_1 = 142
output_day_1_star_2 = 281

day_1_star_1_test_input = [(input_1_day_1, output_day_1_star_1)]
day_1_star_2_test_input = [(input_2_day_1, output_day_1_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_1_star_1_test_input)
def test_day_1_star_1(puzzle_input, output):
    assert day_1.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_1_star_2_test_input)
def test_day_1_star_2(puzzle_input, output):
    assert day_1.compute_star_2(puzzle_input) == output
