def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def solve1(input: list[str]) -> str:
    map = [list(line) for line in input]

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def recursive_dfs(
        plant: str, head: tuple[int, int], visited: set[tuple[int, int]]
    ):
        if head in visited:
            return
        visited.add(head)
        x, y = head
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= ny < len(map)
                and 0 <= nx < len(map[ny])
                and map[ny][nx] == plant
            ):
                recursive_dfs(plant, (nx, ny), visited)

    regions_by_plant: dict[str, list[set[tuple[int, int]]]] = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] not in regions_by_plant:
                regions_by_plant[map[y][x]] = []
            all_region_points = [
                point
                for region in regions_by_plant[map[y][x]]
                for point in region
            ]
            if (x, y) in all_region_points:
                continue
            regions_by_plant[map[y][x]].append(set())
            recursive_dfs(map[y][x], (x, y), regions_by_plant[map[y][x]][-1])

    def calculate_perimeter(plant: str, region: set[tuple[int, int]]) -> int:
        perimeter = 0
        for x, y in region:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                    perimeter += 1
                elif map[ny][nx] != plant:
                    perimeter += 1
        return perimeter

    price = 0
    for plant, regions in regions_by_plant.items():
        for region in regions:
            price += len(region) * calculate_perimeter(plant, region)
    return price


def solve2(input: list[str]) -> str:
    map = [list(line) for line in input]

    directions = {"d": (0, 1), "r": (1, 0), "u": (0, -1), "l": (-1, 0)}

    def recursive_dfs(
        plant: str, head: tuple[int, int], visited: set[tuple[int, int]]
    ):
        if head in visited:
            return
        visited.add(head)
        x, y = head
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if (
                0 <= ny < len(map)
                and 0 <= nx < len(map[ny])
                and map[ny][nx] == plant
            ):
                recursive_dfs(plant, (nx, ny), visited)

    regions_by_plant: dict[str, list[set[tuple[int, int]]]] = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] not in regions_by_plant:
                regions_by_plant[map[y][x]] = []
            all_region_points = [
                point
                for region in regions_by_plant[map[y][x]]
                for point in region
            ]
            if (x, y) in all_region_points:
                continue
            regions_by_plant[map[y][x]].append(set())
            recursive_dfs(map[y][x], (x, y), regions_by_plant[map[y][x]][-1])

    def calculate_sides(plant: str, region: set[tuple[int, int]]) -> int:
        edges: dict[str, list[tuple[int, int]]] = {}
        for x, y in region:
            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                    edges.setdefault(direction, []).append((x, y))
                elif map[ny][nx] != plant:
                    edges.setdefault(direction, []).append((x, y))
        edges = {
            direction: sorted(
                sorted(
                    points,
                    key=lambda p: p[0] if direction in ("u", "d") else p[1],
                ),
                key=lambda p: p[0] if direction in ("l", "r") else p[1],
            )
            for direction, points in edges.items()
        }
        sides = 0
        for direction, points in edges.items():
            while points:
                point = points.pop(0)
                if direction in ("u", "d"):
                    while points and points[0] == (point[0] + 1, point[1]):
                        point = points.pop(0)
                else:
                    while points and points[0] == (point[0], point[1] + 1):
                        point = points.pop(0)
                sides += 1
        return sides

    price = 0
    for plant, regions in regions_by_plant.items():
        for region in regions:
            price += len(region) * calculate_sides(plant, region)
    return price


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
