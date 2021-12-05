class Day5:
    def __init__(self) -> None:
        self.day = 5
        filename = f"day{self.day}_input.txt"
        input = self.read_input(filename)
        self.lines = self.process_input(input)

    def process_input(self, input):
        """
        Process raw inputs into an array of [(start_c, start_r), (end_c, end_r)]
        """
        lines = []
        for line in input:
            start, end = line.split("->")
            new_pair = []
            for pair in [start, end]:
                x, y = pair.split(",")
                new_pair.append((int(x), int(y)))
            lines.append(new_pair)
        return lines

    def read_input(self, filename):
        input_file = open(filename, "r")
        inputs = input_file.read().split("\n")
        input_file.close()
        return inputs

    def part1(self):
        res = self.solve(count_diagonal=False)
        print(f"Answer for Day {self.day} - Part 1: {res}")

    def part2(self):
        res = self.solve()
        print(f"Answer for Day {self.day} - Part 2: {res}")

    def is_vertical(self, pair):
        (start_c, _), (end_c, _) = pair
        return start_c == end_c

    def generate_vertical_line(self, pair):
        (_, start_r), (_, end_r) = pair
        return range(min(start_r, end_r), max(start_r, end_r) + 1)

    def is_horizontal(self, pair):
        (_, start_r), (_, end_r) = pair
        return start_r == end_r

    def generate_horizontal_line(self, pair):
        (start_c, _), (end_c, _) = pair
        return range(min(start_c, end_c), max(start_c, end_c) + 1)

    def generate_diagonal_line(self, pair):
        pair.sort()
        (start_c, start_r), (end_c, end_r) = pair
        col_range = range(start_c, end_c + 1)

        if start_r > end_r:
            row_range = range(start_r, end_r - 1, -1)
        else:
            row_range = range(start_r, end_r + 1)

        diagonal_line = [(c, r) for (c, r) in zip(col_range, row_range)]
        return diagonal_line

    def count_overlaps(self, pos_to_occurs):
        count = 0
        for occurs in pos_to_occurs.values():
            if occurs >= 2:
                count += 1
        return count

    def solve(self, count_vertical=True, count_horizontal=True, count_diagonal=True):
        pos_to_occur = {}
        for line in self.lines:
            if count_vertical and self.is_vertical(line):
                x = line[0][0]
                row_coordinates = self.generate_vertical_line(line)
                for y in row_coordinates:
                    if (x, y) in pos_to_occur:
                        pos_to_occur[(x, y)] += 1
                    else:
                        pos_to_occur[(x, y)] = 1

            elif count_horizontal and self.is_horizontal(line):
                y = line[0][1]
                col_coordinates = self.generate_horizontal_line(line)
                for x in col_coordinates:
                    if (x, y) in pos_to_occur:
                        pos_to_occur[(x, y)] += 1
                    else:
                        pos_to_occur[(x, y)] = 1

            elif count_diagonal:
                diagonal_coordinates = self.generate_diagonal_line(line)
                for pos in diagonal_coordinates:
                    if pos in pos_to_occur:
                        pos_to_occur[pos] += 1
                    else:
                        pos_to_occur[pos] = 1

        return self.count_overlaps(pos_to_occur)


if __name__ == "__main__":
    sol = Day5()
    sol.part1()
    sol.part2()
