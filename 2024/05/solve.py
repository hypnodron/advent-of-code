def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append(line.strip())
    separator = input.index("")
    orderings = [x.split("|") for x in input[:separator]]
    lists = [x.split(",") for x in input[separator + 1 :]]
    before_map = {}
    for ordering in orderings:
        before_map.setdefault(ordering[0], []).append(ordering[1])
    after_map = {}
    for ordering in orderings:
        after_map.setdefault(ordering[1], []).append(ordering[0])

    def compare(a, b):
        if a in before_map:
            if b in before_map[a]:
                return -1
        if a in after_map:
            if b in after_map[a]:
                return 1
        return 0

    from functools import cmp_to_key

    sorted_lists = [sorted(list, key=cmp_to_key(compare)) for list in lists]
    good_lists = [
        list
        for list, sorted_list in zip(lists, sorted_lists)
        if list == sorted_list
    ]
    medians = [x[len(x) // 2] for x in good_lists]
    return sum([int(x) for x in medians])


def solve2(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append(line.strip())
    separator = input.index("")
    orderings = [x.split("|") for x in input[:separator]]
    lists = [x.split(",") for x in input[separator + 1 :]]
    before_map = {}
    for ordering in orderings:
        before_map.setdefault(ordering[0], []).append(ordering[1])
    after_map = {}
    for ordering in orderings:
        after_map.setdefault(ordering[1], []).append(ordering[0])

    def compare(a, b):
        if a in before_map:
            if b in before_map[a]:
                return -1
        if a in after_map:
            if b in after_map[a]:
                return 1
        return 0

    from functools import cmp_to_key

    sorted_lists = [sorted(list, key=cmp_to_key(compare)) for list in lists]
    bad_lists_sorted = [
        sorted_list
        for list, sorted_list in zip(lists, sorted_lists)
        if list != sorted_list
    ]
    medians = [x[len(x) // 2] for x in bad_lists_sorted]
    return sum([int(x) for x in medians])


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
