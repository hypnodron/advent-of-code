def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = [[int(x) for x in line.strip()] for line in input_lines]
    disk = []
    count = 0
    for i, x in enumerate(input[0]):
        if i % 2 == 0:
            for j in range(x):
                disk.append(count)
            count += 1
        else:
            for j in range(x):

                disk.append(".")
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != ".":
            j = disk.index(".")
            if j >= i:
                break
            disk[j] = disk[i]
            disk[i] = "."
    return sum([x * i for i, x in enumerate(disk) if x != "."])


def solve2(input_lines: list[str]) -> str:
    input = [[int(x) for x in line.strip()] for line in input_lines]
    disk = []
    count = 0
    for i, x in enumerate(input[0]):
        if i % 2 == 0:
            disk.append((x, count))
            count += 1
        else:
            disk.append((x, "."))
    i = len(disk) - 1
    while i >= 0:
        if disk[i][1] != ".":
            found = [
                (j, x)
                for j, x in enumerate(disk)
                if x[1] == "." and x[0] >= disk[i][0]
            ]
            if not found:
                i -= 1
                continue
            j, x = found[0]
            if j >= i:
                i -= 1
                continue
            file = disk[i]
            empty = disk[j]
            disk[i] = (file[0], ".")
            disk[j] = (empty[0] - file[0], ".")
            disk.insert(j, file)
        else:
            i -= 1
    raw_disk = []
    for size, content in disk:
        for i in range(size):
            raw_disk.append(content)
    return sum([x * i for i, x in enumerate(raw_disk) if x != "."])


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
