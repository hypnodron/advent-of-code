def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def print_grid(grid: list[list[str]]):
    print(" ", "".join(str(x % 10) for x in range(len(grid[0]))), sep="")
    for y, row in enumerate(grid):
        print(f"{y % 10}", "".join(row), sep="")


def solve1(input: list[str], part: str) -> str:
    separator_index = input.index("")
    grid = [list(line) for line in input[:separator_index]]
    instructions = "".join(input[separator_index + 1 :])
    directions = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                current_position = [x, y]
                break
    for instruction in instructions:
        dx, dy = directions[instruction]
        boxes_to_move = []
        x, y = current_position
        ex, ey = x + dx, y + dy
        while True:
            if grid[ey][ex] == "O":
                boxes_to_move.append((ex, ey))
                ex, ey = ex + dx, ey + dy
            elif grid[ey][ex] == "#":
                can_move = False
                break
            elif grid[ey][ex] == ".":
                can_move = True
                break
        if not can_move:
            continue
        for bx, by in boxes_to_move:
            grid[by + dy][bx + dx] = "O"
        grid[y][x] = "."
        nx, ny = x + dx, y + dy
        grid[ny][nx] = "@"
        current_position = [nx, ny]
    return sum(
        x + y * 100
        for y in range(len(grid))
        for x in range(len(grid[y]))
        if grid[y][x] == "O"
    )


def solve2(input: list[str], part: str) -> str:
    separator_index = input.index("")
    small_grid = [list(line) for line in input[:separator_index]]
    grid = []
    for small_row in small_grid:
        row = []
        for char in small_row:
            if char == "#":
                row += ["#"] * 2
            elif char == ".":
                row += ["."] * 2
            elif char == "@":
                row += ["@", "."]
            elif char == "O":
                row += ["[", "]"]
        grid.append(row)
    instructions = "".join(input[separator_index + 1 :])
    directions = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                current_position = [x, y]
                break

    def recursively_add_vert_boxes_to_move(
        box_side: tuple[int, int],
        direction: str,
        boxes_to_move: list[tuple[tuple[int, int], tuple[int, int]]],
    ) -> bool:
        x, y = box_side
        assert direction in ("v", "^")
        assert grid[y][x] in ("[", "]")
        if grid[y][x] == "[":
            current_box = ((x, y), (x + 1, y))
        elif grid[y][x] == "]":
            current_box = ((x - 1, y), (x, y))
        if current_box in boxes_to_move:
            return True
        boxes_to_move.append(current_box)
        for x, y in current_box:
            if direction == "v":
                ny = y + 1
            elif direction == "^":
                ny = y - 1
            if grid[ny][x] in ("[", "]"):
                can_move = recursively_add_vert_boxes_to_move(
                    (x, ny), direction, boxes_to_move
                )
                if not can_move:
                    return False
            elif grid[ny][x] == "#":
                return False
        return True

    for instruction in instructions:
        dx, dy = directions[instruction]
        boxes_to_move: list[tuple[tuple[int, int], tuple[int, int]]] = []
        x, y = current_position
        if instruction in ("v", "^"):
            assert dx == 0
            if grid[y + dy][x] in ("[", "]"):
                can_move = recursively_add_vert_boxes_to_move(
                    (x, y + dy), instruction, boxes_to_move
                )
                assert len(boxes_to_move) == len(set(boxes_to_move))
            elif grid[y + dy][x] == ".":
                can_move = True
            else:
                can_move = False
        elif instruction in (">", "<"):
            bx, by = x + dx, y
            assert dy == 0
            while True:
                if grid[by][bx] in ("[", "]"):
                    boxes_to_move.append(
                        tuple(
                            sorted(
                                ((bx, by), (bx + dx, by)), key=lambda x: x[0]
                            )
                        )
                    )
                    bx, by = bx + dx * 2, by
                elif grid[by][bx] == "#":
                    can_move = False
                    break
                elif grid[by][bx] == ".":
                    can_move = True
                    break
        if not can_move:
            continue
        assert len(boxes_to_move) == len(set(boxes_to_move))
        boxes_to_move = list(
            reversed(
                sorted(
                    sorted(boxes_to_move, key=lambda x: x[0][1]),
                    key=lambda x: x[0][0],
                )
            )
        )
        for box_to_move in boxes_to_move:
            (bx1, by1), (bx2, by2) = box_to_move
            assert by1 == by2 and bx2 == bx1 + 1
            grid[by1][bx1] = "."
            grid[by2][bx2] = "."
        for box_to_move in boxes_to_move:
            (bx1, by1), (bx2, by2) = box_to_move
            grid[by1 + dy][bx1 + dx] = "["
            grid[by2 + dy][bx2 + dx] = "]"
        grid[y][x] = "."
        grid[y + dy][x + dx] = "@"
        current_position = [x + dx, y + dy]
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "]":
                    assert grid[y][x - 1] == "[", (x, y)
                if grid[y][x] == "[":
                    assert grid[y][x + 1] == "]", (x, y)
    return sum(
        x + y * 100
        for y in range(len(grid))
        for x in range(len(grid[y]))
        if grid[y][x] == "["
    )


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
