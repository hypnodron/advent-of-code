def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def solve1(input_lines: list[str]) -> str:
    input = [
        (int(result), [int(number) for number in numbers.split()])
        for result, numbers in (
            line.strip().split(": ") for line in input_lines
        )
    ]
    from itertools import product

    good_results = []
    for result, numbers in input:
        for operators in product(["+", "*"], repeat=len(numbers) - 1):
            acc = numbers[0]
            for operator, number in zip(operators, numbers[1:]):
                if operator == "+":
                    acc += number
                else:
                    acc *= number
            if result == acc:
                good_results.append(result)
                break
    return sum(good_results)


def solve2(input_lines: list[str]) -> str:
    input = [
        (int(result), [int(number) for number in numbers.split()])
        for result, numbers in (
            line.strip().split(": ") for line in input_lines
        )
    ]
    from itertools import product

    good_results = []
    for result, numbers in input:
        for operators in product(["+", "*", "||"], repeat=len(numbers) - 1):
            acc = numbers[0]
            for operator, number in zip(operators, numbers[1:]):
                if operator == "||":
                    acc = int(f"{acc}{number}")
                elif operator == "+":
                    acc += number
                else:
                    acc *= number
            if result == acc:
                good_results.append(result)
                break
    return sum(good_results)


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
