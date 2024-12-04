def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append(line.strip())
    needle = "XMAS"

    def make_direction_search(dy, dx):
        def direction_search(y, x):
            if (0 <= y + dy * (len(needle) - 1) < len(input)) and (
                0 <= x + dx * (len(needle) - 1) < len(input[0])
            ):
                for i in range(len(needle)):
                    if input[y + dy * i][x + dx * i] != needle[i]:
                        return False
                return True
            return False

        return direction_search

    from itertools import product

    count = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == needle[0]:
                for dy, dx in product([-1, 0, 1], [-1, 0, 1]):
                    direction_search = make_direction_search(dy, dx)
                    if direction_search(y, x):
                        count += 1

    return count


def solve2(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append(line.strip())

    needle = "MAS"

    def make_direction_search(dy, dx):

        def direction_search(y_, x_):
            y = y_ + dy * -1
            x = x_ + dx * -1
            if (
                (0 <= y < len(input))
                and (0 <= x < len(input[0]))
                and (0 <= y + dy * (len(needle) - 1) < len(input))
                and (0 <= x + dx * (len(needle) - 1) < len(input[0]))
            ):
                for i in range(len(needle)):
                    if input[y + dy * i][x + dx * i] != needle[i]:
                        return False
                return True
            return False

        return direction_search

    from itertools import product

    count = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == needle[1]:
                top_right = make_direction_search(-1, 1)
                bottom_right = make_direction_search(1, 1)
                bottom_left = make_direction_search(1, -1)
                top_left = make_direction_search(-1, -1)
                count += (
                    (top_right(y, x) and bottom_right(y, x))
                    + (bottom_right(y, x) and bottom_left(y, x))
                    + (bottom_left(y, x) and top_left(y, x))
                    + (top_left(y, x) and top_right(y, x))
                )

    return count


def main():
    example_input_lines = read_input("input-example.txt")
    puzzle_input_lines = read_input("input-puzzle.txt")
    # part 1
    example_output1 = solve1(example_input_lines)
    print(f"Example output 1:\n{example_output1}\n")
    puzzle_output1 = solve1(puzzle_input_lines)
    print(f"Puzzle output 1:\n{puzzle_output1}\n")
    # part 2
    example_output2 = solve2(example_input_lines)
    print(f"Example output 2:\n{example_output2}\n")
    puzzle_output2 = solve2(puzzle_input_lines)
    print(f"Puzzle output 2:\n{puzzle_output2}")


if __name__ == "__main__":
    main()
