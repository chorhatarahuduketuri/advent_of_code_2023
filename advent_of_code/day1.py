print(
    sum([int(x) for x in [decoded_line[0][0]+decoded_line[-1][0]
     for decoded_line
     in [
        [
            number
            for number
            in [
            [
                letter
                for letter
                in code.split(maxsplit=-1)
                if letter.isnumeric()
            ]
            for code
            in line.strip()
        ]
            if number
        ]
        for
        line in open('../puzzle_inputs/puzzle_input_1.txt')
    ]]])
)
