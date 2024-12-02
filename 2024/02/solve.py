def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append([int(x) for x in line.split()])
    flags = []
    for line in input:
        diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        inc = diffs[0] > 0
        flag = all(1 <= abs(diff) <= 3 and (diff > 0) == inc for diff in diffs)
        flags.append(flag)
    return sum(flags)


def solve2(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append([int(x) for x in line.split()])
    flags = []
    for line in input:
        flag = False
        for i in range(len(line)):
            line_updated = line[:i] + line[i + 1 :]
            diffs = [
                line_updated[i + 1] - line_updated[i]
                for i in range(len(line_updated) - 1)
            ]
            inc = diffs[0] > 0
            flag = all(
                1 <= abs(diff) <= 3 and (diff > 0) == inc for diff in diffs
            )
            if flag:
                break
        flags.append(flag)
    return sum(flags)


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
