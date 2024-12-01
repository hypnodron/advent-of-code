def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append([int(x) for x in line.strip().split()])
    list_a, list_b = zip(*input)
    list_a, list_b = sorted(list_a), sorted(list_b)
    diff_sum_list = [abs(b - a) for a, b in zip(list_a, list_b)]
    diff_sum = sum(diff_sum_list)
    return diff_sum


def solve2(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append([int(x) for x in line.strip().split()])
    list_a, list_b = zip(*input)
    list_b_counts = {}
    for b in list_b:
        list_b_counts[b] = list_b_counts.get(b, 0) + 1
    sim_list = [a * list_b_counts.get(a, 0) for a in list_a]
    return sum(sim_list)


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
