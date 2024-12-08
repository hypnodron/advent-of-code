def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = [list(line.strip()) for line in input_lines]
    antennas = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != ".":
                antennas.setdefault(input[y][x], []).append((x, y))
    antinodes = set()
    for antenna, positions in antennas.items():
        for pos in positions:
            for other_pos in positions:
                if pos == other_pos:
                    continue
                dx = pos[0] - other_pos[0]
                dy = pos[1] - other_pos[1]
                anti_x = pos[0] + dx * -2
                anti_y = pos[1] + dy * -2
                if 0 <= anti_x < len(input[0]) and 0 <= anti_y < len(input):
                    antinodes.add((anti_x, anti_y))
    return len(antinodes)


def solve2(input_lines: list[str]) -> str:
    input = [list(line.strip()) for line in input_lines]
    antennas = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != ".":
                antennas.setdefault(input[y][x], []).append((x, y))
    antinodes = set()
    for antenna, positions in antennas.items():
        for pos in positions:
            for other_pos in positions:
                if pos == other_pos:
                    continue
                dx = pos[0] - other_pos[0]
                dy = pos[1] - other_pos[1]
                anti_x = pos[0]
                anti_y = pos[1]
                while 0 <= anti_x < len(input[0]) and 0 <= anti_y < len(input):
                    antinodes.add((anti_x, anti_y))
                    anti_x += dx
                    anti_y += dy
                while 0 <= anti_x < len(input[0]) and 0 <= anti_y < len(input):
                    antinodes.add((anti_x, anti_y))
                    anti_x -= dx
                    anti_y -= dy
    return len(antinodes)


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
