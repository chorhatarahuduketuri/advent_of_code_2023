from settings import PUZZLE_INPUT_PATH


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


print("day 1, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
