def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def solve1(input: list[str], part: str) -> str:
    import re

    robots = []
    for line in input:
        px, py, vx, vy = re.match(
            r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line
        ).groups()
        robots.append(([int(px), int(py)], (int(vx), int(vy))))
    if part == "example":
        w, h = 11, 7
    elif part == "puzzle":
        w, h = 101, 103
    for _ in range(100):
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % w
            robot[0][1] = (robot[0][1] + robot[1][1]) % h
    robot_positions = [robot[0] for robot in robots]
    quadrant_sums = {"tl": 0, "tr": 0, "bl": 0, "br": 0}
    for y in range(h):
        for x in range(w):
            mid_x = w // 2
            mid_y = h // 2
            if x < mid_x and y < mid_y:
                quadrant_sums["tl"] += robot_positions.count([x, y])
            elif x < mid_x and y > mid_y:
                quadrant_sums["bl"] += robot_positions.count([x, y])
            elif x > mid_x and y < mid_y:
                quadrant_sums["tr"] += robot_positions.count([x, y])
            elif x > mid_x and y > mid_y:
                quadrant_sums["br"] += robot_positions.count([x, y])
    product = 1
    for quadrant in quadrant_sums.values():
        product *= quadrant
    return product


def solve2(input: list[str], part: str) -> str:
    if part == "example":
        return
    import re

    robots = []
    for line in input:
        px, py, vx, vy = re.match(
            r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line
        ).groups()
        robots.append(([int(px), int(py)], (int(vx), int(vy))))
    if part == "example":
        w, h = 11, 7
    elif part == "puzzle":
        w, h = 101, 103
    tree_step = None
    for step in range(10000):
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % w
            robot[0][1] = (robot[0][1] + robot[1][1]) % h
        robot_positions = [robot[0] for robot in robots]
        grid = [["."] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                count = robot_positions.count([x, y])
                if count > 0:
                    grid[y][x] = str(count)
        row_strs = ["".join(row) for row in grid]
        if any(["1111111111111111111111111111111" in row for row in row_strs]):
            tree_step = step + 1
            break
    return tree_step


def main():
    example_input = read_input("input-example.txt")
    puzzle_input = read_input("input-puzzle.txt")
    # part 1
    example_output1 = solve1(example_input, "example")
    print(f"Example output 1:\n{example_output1}\n")
    puzzle_output1 = solve1(puzzle_input, "puzzle")
    print(f"Puzzle output 1:\n{puzzle_output1}\n")
    # part 2
    example_output2 = solve2(example_input, "example")
    print(f"Example output 2:\n{example_output2}\n")
    puzzle_output2 = solve2(puzzle_input, "puzzle")
    print(f"Puzzle output 2:\n{puzzle_output2}")


if __name__ == "__main__":
    main()
