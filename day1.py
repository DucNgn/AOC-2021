from collections import deque


class Day1:
    def __init__(self) -> None:
        filename = "day1_input.txt"
        self.reports = self.read_input(filename)

    def read_input(self, filename):
        input_file = open(filename, "r")
        # Works for not too large file
        inputs = [int(x) for x in input_file.read().split()]
        input_file.close()
        return inputs

    def part1(self):
        res = self.calculate_increments(self.reports)
        print(f"Answer for Day 1 - Part 1: {res}")

    def part2(self):
        res = self.sliding_window_increments(self.reports)
        print(f"Answer for Day 1 - Part 2: {res}")

    # Part 1
    def calculate_increments(self, reports) -> int:
        counter = 0
        for i in range(1, len(reports)):
            if reports[i] >= reports[i - 1]:
                counter += 1

        return counter

    # Part 2
    def sliding_window_increments(self, reports):
        counter = 0

        window = deque()
        for i in range(3):
            window.append(reports[i])
        prev_sum = sum(window)

        for i in range(3, len(reports)):
            out = window.popleft()
            window.append(reports[i])
            curr_sum = prev_sum - out + reports[i]
            if curr_sum > prev_sum:
                counter += 1
            prev_sum = curr_sum

        return counter


if __name__ == "__main__":
    day1 = Day1()
    day1.part1()
    day1.part2()
