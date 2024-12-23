def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def solve1(input: list[str]) -> str:
    grid = [[int(x) for x in line] for line in input]
    heads = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                heads.append((x, y))
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def recursive_dfs(
        tracking_grid: list[list[int | str]], head: tuple[int, int], count: int
    ) -> int:
        x, y = head
        if tracking_grid[y][x] != ".":
            return 0
        if grid[y][x] == 9:
            tracking_grid[y][x] = 9
            return 1
        next_val = grid[y][x] + 1
        next_count = count
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid[0])
                and 0 <= ny < len(grid)
                and grid[ny][nx] == next_val
            ):
                next_count += recursive_dfs(tracking_grid, (nx, ny), count)
        if next_count > count:
            tracking_grid[y][x] = grid[y][x]
        return next_count

    counts = []
    for head in heads:
        tracking_grid = [
            ["." for _ in range(len(grid[0]))] for _ in range(len(grid))
        ]
        count = recursive_dfs(tracking_grid, head, 0)
        counts.append(count)
    return sum(counts)


def solve2(input: list[str]) -> str:
    grid = [[int(x) for x in line] for line in input]
    heads = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                heads.append((x, y))
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def recursive_dfs(
        tracking_grid: list[list[int | str]], head: tuple[int, int], count: int
    ) -> int:
        x, y = head
        if grid[y][x] == 9:
            tracking_grid[y][x] = 9
            return 1
        next_val = grid[y][x] + 1
        next_count = count
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid[0])
                and 0 <= ny < len(grid)
                and grid[ny][nx] == next_val
            ):
                next_count += recursive_dfs(tracking_grid, (nx, ny), count)
        if next_count > count:
            tracking_grid[y][x] = grid[y][x]
        return next_count

    counts = []
    for head in heads:
        tracking_grid = [
            ["." for _ in range(len(grid[0]))] for _ in range(len(grid))
        ]
        count = recursive_dfs(tracking_grid, head, 0)
        counts.append(count)
    return sum(counts)


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
