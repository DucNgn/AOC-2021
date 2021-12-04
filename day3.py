class Day3:
    def __init__(self) -> None:
        filename = "day3_input.txt"
        self.diagnostic = self.read_input(filename)
        self.max_row = len(self.diagnostic)
        self.max_col = len(self.diagnostic[0])
        self.breaker = self.max_row // 2

    def read_input(self, filename):
        input_file = open(filename, "r")
        inputs = input_file.read().split("\n")
        input_file.close()
        return inputs

    def part1(self):
        res = self.binary_diagnostic()
        print(f"Answer for Day 3 - Part 1: {res}")

    def part2(self):
        res = self.bit_criteria()
        print(f"Answer for Day 3 - Part 2: {res}")

    def binary_diagnostic(self):
        total = [0] * len(self.diagnostic[0])
        for diag in self.diagnostic:
            for i, bit in enumerate(diag):
                bit = int(bit)
                total[i] += bit

        total.reverse()
        gamma = epsilon = 0
        for i, num in enumerate(total):
            if num > self.breaker:
                gamma += 2 ** i
            else:
                epsilon += 2 ** i

        return gamma * epsilon

    def bit_criteria(self):
        def get_most_least_common(col_idx=0, rows=range(self.max_row)):
            count_ones = 0
            for r in rows:
                if int(self.diagnostic[r][col_idx]) == 1:
                    count_ones += 1
            count_zeros = len(rows) - count_ones
            most_common_bit = 1 if count_ones >= count_zeros else 0
            least_common_bit = int(not most_common_bit)
            return most_common_bit, least_common_bit

        # Initialize 1st step
        most_common_bit, least_common_bit = get_most_least_common()
        oxygen = [
            r
            for r in range(self.max_row)
            if int(self.diagnostic[r][0]) == most_common_bit
        ]
        co2 = [
            r
            for r in range(self.max_row)
            if int(self.diagnostic[r][0]) == least_common_bit
        ]

        for c in range(1, self.max_col):
            if len(oxygen) > 1:
                most_common_bit, _ = get_most_least_common(c, oxygen)
                oxygen = [
                    r for r in oxygen if int(self.diagnostic[r][c]) == most_common_bit
                ]
            if len(co2) > 1:
                _, least_common_bit = get_most_least_common(c, co2)
                co2 = [r for r in co2 if int(self.diagnostic[r][c]) == least_common_bit]
            if len(oxygen) == 1 and len(co2) == 1:
                break

        oxygen_rating = int(self.diagnostic[oxygen[0]], 2)
        co2_rating = int(self.diagnostic[co2[0]], 2)
        return oxygen_rating * co2_rating


if __name__ == "__main__":
    sol = Day3()
    sol.part1()
    sol.part2()
