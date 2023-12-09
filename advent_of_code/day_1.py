from settings import PUZZLE_INPUT_PATH
import re


def compute_star_1(puzzle_input):
    return sum(
        [
            int(x)
            for x in [
                decoded_line[0][0] + decoded_line[-1][0]
                for decoded_line in [
                    [
                        number
                        for number in [
                            [
                                letter
                                for letter in code.split(maxsplit=-1)
                                if letter.isnumeric()
                            ]
                            for code in line.strip()
                        ]
                        if number
                    ]
                    for line in puzzle_input.strip().split()
                ]
            ]
        ]
    )


def compute_star_2(puzzle_input):
    """The lookahead assertion ?=(...) matches, but doesn't consume any of the string, so it doesn't hide overlaps"""
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    return sum(
        [
            int(
                (numbers[x[0]] if numbers.get(x[0]) else x[0])
                + (numbers[x[-1]] if numbers.get(x[-1]) else x[-1])
            )
            for x in [
                re.findall(
                    r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
                )
                for line in puzzle_input.strip().split()
            ]
        ]
    )


print("day 1, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
print("day 1, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
