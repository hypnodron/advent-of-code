import math


def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def solve1(input: list[str], part: str) -> str:
    separator_index = input.index("")
    registers = input[:separator_index]
    program = input[separator_index + 1]
    registers = [int(register.split(": ")[1]) for register in registers]
    registers = dict(zip(["A", "B", "C"], registers))
    program = program.removeprefix("Program: ")
    program = [int(instruction) for instruction in program.split(",")]
    opcode_map = {
        0: "adv",
        1: "bxl",
        2: "bst",
        3: "jnz",
        4: "bxc",
        5: "out",
        6: "bdv",
        7: "cdv",
    }
    instruction_pointer = 0

    def combo_operand(operand: int) -> int:
        if operand <= 3:
            return operand
        match operand:
            case 4:
                return registers["A"]
            case 5:
                return registers["B"]
            case 6:
                return registers["C"]

    output = []
    while instruction_pointer < len(program):
        opcode = opcode_map[program[instruction_pointer]]
        operand = program[instruction_pointer + 1]
        next_instruction_pointer = instruction_pointer + 2
        match opcode:
            case "adv":
                result = int(registers["A"] / (2 ** combo_operand(operand)))
                registers["A"] = result
            case "bxl":
                registers["B"] = registers["B"] ^ operand
            case "bst":
                registers["B"] = combo_operand(operand) % 8
            case "jnz":
                if registers["A"] != 0:
                    next_instruction_pointer = operand
            case "bxc":
                registers["B"] = registers["B"] ^ registers["C"]
            case "out":
                output.append(combo_operand(operand) % 8)
            case "bdv":
                result = int(registers["A"] / (2 ** combo_operand(operand)))
                registers["B"] = result
            case "cdv":
                result = int(registers["A"] / (2 ** combo_operand(operand)))
                registers["C"] = result
        instruction_pointer = next_instruction_pointer
    return ",".join(str(x) for x in output)


def solve2(input: list[str], part: str) -> str:
    def combo_operand(operand: int, registers: dict[str, int]) -> int:
        if operand <= 3:
            return operand
        match operand:
            case 4:
                return registers["A"]
            case 5:
                return registers["B"]
            case 6:
                return registers["C"]

    def run_program(program: list[int], registers: dict[str, int]) -> list[int]:
        output = []
        instruction_pointer = 0
        while instruction_pointer < len(program):
            if len(output) > len(program):
                break
            opcode = opcode_map[program[instruction_pointer]]
            operand = program[instruction_pointer + 1]
            next_instruction_pointer = instruction_pointer + 2
            match opcode:
                case "adv":
                    result = int(
                        registers["A"]
                        / (2 ** combo_operand(operand, registers))
                    )
                    registers["A"] = result
                case "bxl":
                    registers["B"] = registers["B"] ^ operand
                case "bst":
                    registers["B"] = combo_operand(operand, registers) % 8
                case "jnz":
                    if registers["A"] != 0:
                        next_instruction_pointer = operand
                case "bxc":
                    registers["B"] = registers["B"] ^ registers["C"]
                case "out":
                    output.append(combo_operand(operand, registers) % 8)
                case "bdv":
                    result = int(
                        registers["A"]
                        / (2 ** combo_operand(operand, registers))
                    )
                    registers["B"] = result
                case "cdv":
                    result = int(
                        registers["A"]
                        / (2 ** combo_operand(operand, registers))
                    )
                    registers["C"] = result
            instruction_pointer = next_instruction_pointer
        return output

    separator_index = input.index("")
    registers = input[:separator_index]
    program = input[separator_index + 1]
    registers = [int(register.split(": ")[1]) for register in registers]
    registers = dict(zip(["A", "B", "C"], registers))
    program = program.removeprefix("Program: ")
    program = [int(instruction) for instruction in program.split(",")]
    opcode_map = {
        0: "adv",
        1: "bxl",
        2: "bst",
        3: "jnz",
        4: "bxc",
        5: "out",
        6: "bdv",
        7: "cdv",
    }
    # with the help of the internet
    candidates = [0]
    nums_to_try = list(range(8))
    for i in range(len(program) - 1, -1, -1):
        target = program[i:]
        new_candidates = []
        for num in candidates:
            attempts = [num * 8 + x for x in nums_to_try]
            valid = [
                y
                for y in attempts
                if target == run_program(program, {**registers, "A": y})
            ]
            new_candidates.extend(valid)
        candidates = new_candidates
    return str(min(candidates))


def main():
    example_input = read_input("input-example.txt")
    puzzle_input = read_input("input-puzzle.txt")
    # part 1
    example_output1 = solve1(example_input, "example")
    print(f"Example output 1:\n{example_output1}\n")
    puzzle_output1 = solve1(puzzle_input, "puzzle")
    print(f"Puzzle output 1:\n{puzzle_output1}\n")
    # part 2
    example_output2 = solve2(read_input("input-example2.txt"), "example")
    print(f"Example output 2:\n{example_output2}\n")
    puzzle_output2 = solve2(puzzle_input, "puzzle")
    print(f"Puzzle output 2:\n{puzzle_output2}")


if __name__ == "__main__":
    main()
