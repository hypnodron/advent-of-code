def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def print_grid(grid: list[list[str]], coords=True):
    if coords:
        print(" ", "".join(str(x % 10) for x in range(len(grid[0]))), sep="")
    for y, row in enumerate(grid):
        s = "".join(row)
        if coords:
            s = f"{y % 10}{s}"
        print(s)


def solve1(input: list[str], part: str) -> str:
    grid = [list(line) for line in input]
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    def bfs(
        start_pos: tuple[int, int],
        start_direction: str,
        tracking_grid: list[list[str]],
    ) -> tuple[int, bool]:
        from heapq import heappush, heappop

        queue = [(0, start_pos, start_direction)]
        costs = {}
        found_end = False
        min_end_cost = float("inf")
        while queue:
            cost, pos, direction = heappop(queue)
            x, y = pos
            state = (pos, direction)
            if state in costs and costs[state] < cost:
                continue
            for direct, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if tracking_grid[ny][nx] not in [".", "E"]:
                    continue
                new_cost = cost + 1
                if direct != direction:
                    new_cost += 1000
                new_state = ((nx, ny), direct)
                if tracking_grid[ny][nx] == "E":
                    found_end = True
                    min_end_cost = min(min_end_cost, new_cost)
                    continue
                if new_state not in costs or new_cost < costs[new_state]:
                    costs[new_state] = new_cost
                    heappush(queue, (new_cost, (nx, ny), direct))
                    tracking_grid[ny][nx] = direct
        return min_end_cost, found_end

    tracking_grid = []
    for row in grid:
        tracking_row = []
        for val in row:
            tracking_row.append(val)
        tracking_grid.append(tracking_row)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = (x, y)
                break
    cost, found = bfs(start, ">", tracking_grid)
    return cost


def solve2(input: list[str], part: str) -> str:
    grid = [list(line) for line in input]
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    def bfs(
        start_pos: tuple[int, int],
        start_direction: str,
        tracking_grid: list[list[str]],
    ) -> tuple[int, bool, list[list[str]]]:
        from heapq import heappush, heappop
        from copy import deepcopy

        queue = [(0, start_pos, start_direction, deepcopy(tracking_grid))]
        costs = {}
        found_end = False
        min_end_cost = float("inf")
        best_paths = []
        while queue:
            cost, pos, direction, current_grid = heappop(queue)
            x, y = pos
            state = (pos, direction)
            if state in costs and costs[state] < cost:
                continue
            for direct, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if current_grid[ny][nx] not in [".", "E"]:
                    continue
                new_cost = cost + 1
                if direct != direction:
                    new_cost += 1000
                new_state = ((nx, ny), direct)
                if current_grid[ny][nx] == "E":
                    found_end = True
                    if new_cost < min_end_cost:
                        min_end_cost = new_cost
                        best_paths = [deepcopy(current_grid)]
                    elif new_cost == min_end_cost:
                        best_paths.append(deepcopy(current_grid))
                    continue
                if new_state not in costs or new_cost <= costs[new_state]:
                    new_grid = deepcopy(current_grid)
                    new_grid[ny][nx] = direct
                    costs[new_state] = new_cost
                    heappush(queue, (new_cost, (nx, ny), direct, new_grid))
        return cost, found_end, best_paths

    tracking_grid = []
    for row in grid:
        tracking_row = []
        for val in row:
            tracking_row.append(val)
        tracking_grid.append(tracking_row)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = (x, y)
                break
    cost, found, best_paths = bfs(start, ">", tracking_grid)
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for path in best_paths:
                if path[y][x] in ["^", "v", "<", ">"]:
                    count += 1
                    break
    return count + 2


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
