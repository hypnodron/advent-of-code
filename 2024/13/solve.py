# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///


def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def solve1(input: list[str]) -> str:
    machines: list[tuple[int, int], tuple[int, int], tuple[int, int]] = []
    input = input.copy()
    import re

    while input:
        button_a = tuple(
            int(x)
            for x in re.match(
                r"Button A: X\+(\d+), Y\+(\d+)", input.pop(0)
            ).groups()
        )
        button_b = tuple(
            int(x)
            for x in re.match(
                r"Button B: X\+(\d+), Y\+(\d+)", input.pop(0)
            ).groups()
        )
        prize = tuple(
            int(x)
            for x in re.match(r"Prize: X=(\d+), Y=(\d+)", input.pop(0)).groups()
        )
        machines.append((button_a, button_b, prize))
        input and input.pop(0)
    presses = []
    for machine in machines:
        (adx, ady), (bdx, bdy), (px, py) = machine
        machine_presses = []
        for i in range(100):
            ax, ay = adx * i, ady * i
            for j in range(100):
                bx, by = bdx * j, bdy * j
                if ax + bx == px and ay + by == py:
                    machine_presses.append((i, j))
                    break
                if ax + bx > px or ay + by > py:
                    break
        machine_presses.sort(key=lambda x: x[0] * 3 + x[1])
        if machine_presses:
            presses.append(machine_presses[0])
    return sum([x[0] * 3 + x[1] for x in presses if x])


def solve2(input: list[str]) -> str:
    machines: list[tuple[int, int], tuple[int, int], tuple[int, int]] = []
    import re

    while input:
        button_a = tuple(
            int(x)
            for x in re.match(
                r"Button A: X\+(\d+), Y\+(\d+)", input.pop(0)
            ).groups()
        )
        button_b = tuple(
            int(x)
            for x in re.match(
                r"Button B: X\+(\d+), Y\+(\d+)", input.pop(0)
            ).groups()
        )
        prize = tuple(
            int(x) + 10000000000000
            for x in re.match(r"Prize: X=(\d+), Y=(\d+)", input.pop(0)).groups()
        )
        machines.append((button_a, button_b, prize))
        input and input.pop(0)

    def matrix2d_inverse_vector_multiply(
        matrix: list[list[int]], vector: list[int]
    ) -> list[int]:
        (a, b), (c, d) = matrix
        (x, y) = vector
        return (
            (d * x + (-b * y)) / (a * d - b * c),
            (-c * x + (a * y)) / (a * d - b * c),
        )

    presses = []
    for machine in machines:
        (adx, ady), (bdx, bdy), (px, py) = machine
        matrix = [
            [adx, bdx],
            [ady, bdy],
        ]
        vector = [px, py]
        inverse_prize = matrix2d_inverse_vector_multiply(matrix, vector)
        if all([int(x) == x for x in inverse_prize]):
            presses.append([int(x) for x in inverse_prize])
    return sum([x[0] * 3 + x[1] for x in presses if x])


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
