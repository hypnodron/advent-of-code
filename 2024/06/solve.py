from typing import TypedDict


def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = []
    for line in input_lines:
        input.append(list(line.strip()))
    for y in range(len(input)):
        for x in range(len(input[y])):
            if (
                input[y][x] == "^"
                or input[y][x] == "v"
                or input[y][x] == "<"
                or input[y][x] == ">"
            ):
                guard_x = x
                guard_y = y
                guard_direction = input[y][x]
                break
    input[guard_y][guard_x] = "."
    visited = set()
    visited.add((guard_y, guard_x))
    while True:
        # go forward
        if (
            guard_direction == "^"
            and guard_y > 0
            and input[guard_y - 1][guard_x] == "."
        ):
            guard_y -= 1
            visited.add((guard_y, guard_x))
            continue
        elif (
            guard_direction == "v"
            and guard_y < len(input) - 1
            and input[guard_y + 1][guard_x] == "."
        ):
            guard_y += 1
            visited.add((guard_y, guard_x))
            continue
        elif (
            guard_direction == "<"
            and guard_x > 0
            and input[guard_y][guard_x - 1] == "."
        ):
            guard_x -= 1
            visited.add((guard_y, guard_x))
            continue
        elif (
            guard_direction == ">"
            and guard_x < len(input[guard_y]) - 1
            and input[guard_y][guard_x + 1] == "."
        ):
            guard_x += 1
            visited.add((guard_y, guard_x))
            continue
        # exit area if guard is at the edge and facing the edge
        if (
            (guard_y == 0 and guard_direction == "^")
            or (guard_y == len(input) - 1 and guard_direction == "v")
            or (guard_x == 0 and guard_direction == "<")
            or (guard_x == len(input[guard_y]) - 1 and guard_direction == ">")
        ):
            visited.add((guard_y, guard_x))
            break
        # turn right
        if guard_direction == "^":
            guard_direction = ">"
            continue
        elif guard_direction == ">":
            guard_direction = "v"
            continue
        elif guard_direction == "v":
            guard_direction = "<"
            continue
        elif guard_direction == "<":
            guard_direction = "^"
            continue
    return len(visited)


def solve2(input_lines: list[str]):
    input = []
    for line in input_lines:
        input.append(list(line.strip()))

    from typing import NamedTuple

    deltas = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }
    directions = list(deltas.keys())

    def simulate_guard(
        map: list[list[str]],
        init_guard_y: int,
        init_guard_x: int,
        init_guard_direction: str,
    ):
        guard_y, guard_x, guard_direction = (
            init_guard_y,
            init_guard_x,
            init_guard_direction,
        )
        visited = set()
        while True:
            # detect loop
            if (guard_y, guard_x, guard_direction) in visited:
                return True, len(visited), visited
            visited.add((guard_y, guard_x, guard_direction))
            dx, dy = deltas[guard_direction]
            new_guard_x, new_guard_y = guard_x + dx, guard_y + dy
            # exit area if out of bounds
            if not (
                0 <= new_guard_y < len(map)
                and 0 <= new_guard_x < len(map[new_guard_y])
            ):
                return False, len(visited), visited
            # move to new position if possible
            if map[new_guard_y][new_guard_x] != "#":
                guard_x, guard_y = new_guard_x, new_guard_y
            else:
                # turn right
                guard_direction = directions[
                    (directions.index(guard_direction) + 1) % len(directions)
                ]

    for y in range(len(input)):
        for x in range(len(input[y])):
            if (
                input[y][x] == "^"
                or input[y][x] == "v"
                or input[y][x] == "<"
                or input[y][x] == ">"
            ):
                guard_x, guard_y, guard_direction = x, y, input[y][x]
                break

    loop_count = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == ".":
                # create a deep copy of the map
                map_copy = [row[:] for row in input]
                # add an obstacle
                map_copy[y][x] = "#"
                loop_detected, _, _ = simulate_guard(
                    map_copy, guard_y, guard_x, guard_direction
                )
                if loop_detected:
                    loop_count += 1

    return loop_count


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
