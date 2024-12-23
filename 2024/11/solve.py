def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def solve1(input: list[str]) -> str:
    stones = [int(x) for x in input[0].split()]
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                l = str(stone)[: len(str(stone)) // 2]
                r = str(stone)[len(str(stone)) // 2 :]
                new_stones.append(int(l))
                new_stones.append(int(r))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def solve2(input: list[str]) -> str:
    stones = [int(x) for x in input[0].split()]
    dict = {}
    for stone in stones:
        dict[stone] = dict.get(stone, 0) + 1
    for _ in range(75):
        new_dict = {}
        for stone, count in dict.items():
            if stone == 0:
                new_dict[1] = new_dict.get(1, 0) + count
            elif len(str(stone)) % 2 == 0:
                l = int(str(stone)[: len(str(stone)) // 2])
                r = int(str(stone)[len(str(stone)) // 2 :])
                new_dict[l] = new_dict.get(l, 0) + count
                new_dict[r] = new_dict.get(r, 0) + count
            else:
                new_dict[stone * 2024] = new_dict.get(stone * 2024, 0) + count
        dict = new_dict
    return sum(dict.values())


def main():
    example_input = read_input("input-example.txt")
    puzzle_input = read_input("input-puzzle.txt")
    # part 1
    example_output1 = solve1(example_input)
    print(f"Example output 1:\n{example_output1}\n")
    puzzle_output1 = solve1(puzzle_input)
    print(f"Puzzle output 1:\n{puzzle_output1}\n")
    # part 2
    example_output2 = solve2(example_input)
    print(f"Example output 2:\n{example_output2}\n")
    puzzle_output2 = solve2(puzzle_input)
    print(f"Puzzle output 2:\n{puzzle_output2}")


if __name__ == "__main__":
    main()
