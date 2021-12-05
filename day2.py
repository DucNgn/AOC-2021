class Day2:
    def __init__(self) -> None:
        filename = "day2_input.txt"
        self.moves = self.read_input(filename)

    def read_input(self, filename):
        input_file = open(filename, "r")
        inputs = input_file.read().split("\n")
        input_file.close()
        return inputs

    def part1(self):
        res = self.dive()
        print(f"Answer for Day 2 - Part 1: {res}")

    def part2(self):
        res = self.dive_with_aim()
        print(f"Answer for Day 2 - Part 2: {res}")

    def dive(self):
        horizontal = depth = 0
        for move in self.moves:
            [direction, num] = move.split()
            num = int(num)

            if direction == "down":
                depth += num
            elif direction == "up":
                depth -= num
            elif direction == "forward":
                horizontal += num

        return horizontal * depth

    def dive_with_aim(self):
        horizontal = aim = depth = 0
        for move in self.moves:
            [direction, X] = move.split()
            X = int(X)

            if direction == "forward":
                horizontal += X
                depth += aim * X
            elif direction == "up":
                aim -= X
            elif direction == "down":
                aim += X

        return horizontal * depth


if __name__ == "__main__":
    sol = Day2()
    sol.part1()
    sol.part2()
