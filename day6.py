class Day6:
    def __init__(self) -> None:
        self.day = 6
        filename = f"day{self.day}_input.txt"
        input = self.read_input(filename)
        self.states = self.process_input(input[0])

    def process_input(self, input):
        input_lst = list(map(int, input.split(",")))
        return input_lst

    def read_input(self, filename):
        input_file = open(filename, "r")
        inputs = input_file.read().split("\n")
        input_file.close()
        return inputs

    def part1(self):
        res = self.num_of_fish_after(num_of_day=80)
        print(f"Answer for Day {self.day} - Part 1: {res}")

    def part2(self):
        res = self.num_of_fish_after(num_of_day=256)
        print(f"Answer for Day {self.day} - Part 2: {res}")

    def num_of_fish_after(self, num_of_day: int):
        # Memo
        lanternfish_dict = {}
        states = self.states.copy()
        for i in range(-1, 9):
            lanternfish_dict[i] = 0
        for state in states:
            lanternfish_dict[state] += 1

        for _ in range(num_of_day):
            for i in range(-1, 8):
                lanternfish_dict[i] = lanternfish_dict[i + 1]

            due_fish = lanternfish_dict[-1]
            lanternfish_dict[6] += due_fish
            lanternfish_dict[8] = due_fish

        del lanternfish_dict[-1]
        return sum(lanternfish_dict.values())


if __name__ == "__main__":
    sol = Day6()
    sol.part1()
    sol.part2()
