def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    import re

    return sum(
        [
            int(x) * int(y)
            for x, y in re.findall(r"mul\((\d+),(\d+)\)", "".join(input_lines))
        ]
    )


def solve2(input_lines: list[str]) -> str:
    import re

    matches = re.findall(
        r"((mul\()(\d+),(\d+)\)|don't\(\)|do\(\))", "".join(input_lines)
    )
    sum = 0
    enabled = True
    for match in matches:
        match match:
            case (_, "mul(", x, y) if enabled:
                sum += int(x) * int(y)
            case ("don't()", *_):
                enabled = False
            case ("do()", *_):
                enabled = True
    return sum


def main():
    example_input_lines = read_input("input-example.txt")
    puzzle_input_lines = read_input("input-puzzle.txt")
    # part 1
    example_output1 = solve1(example_input_lines)
    print(f"Example output 1:\n{example_output1}\n")
    puzzle_output1 = solve1(puzzle_input_lines)
    print(f"Puzzle output 1:\n{puzzle_output1}\n")
    # part 2
    example_output2 = solve2(read_input("input-example2.txt"))
    print(f"Example output 2:\n{example_output2}\n")
    puzzle_output2 = solve2(puzzle_input_lines)
    print(f"Puzzle output 2:\n{puzzle_output2}")


if __name__ == "__main__":
    main()
