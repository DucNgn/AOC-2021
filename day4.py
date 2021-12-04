class Day4:
    boards = []
    drawn = []

    def __init__(self) -> None:
        filename = "day4_input.txt"
        input = self.read_input(filename)

        # Get the draws on the 1st line
        self.drawn = list(map(int, input[0].split(",")))

        # Read the board in
        curr_board = []
        for r in range(2, len(input)):
            curr_row = input[r]
            if curr_row != "":
                curr_board.append(list(map(int, curr_row.split())))
            else:
                self.boards.append(curr_board)
                curr_board = []

        # Append the last board
        self.boards.append(curr_board)

        # Read in max row and max col
        self.max_row = len(self.boards[0])
        self.max_col = len(self.boards[0][0])

    def read_input(self, filename):
        input_file = open(filename, "r")
        inputs = input_file.read().split("\n")
        input_file.close()
        return inputs

    def part1(self):
        res = self.bingo()
        print(f"Answer for Day 4 - Part 1: {res}")

    def part2(self):
        res = self.last_win()
        print(f"Answer for Day 4 - Part 2: {res}")

    def get_pos_on_board(self, board_idx, num):
        for r in range(self.max_row):
            for c in range(self.max_col):
                if self.boards[board_idx][r][c] == num:
                    return (r, c)
        return (None, None)

    def get_num_on_board(self, board_idx, r, c):
        return self.boards[board_idx][r][c]

    def is_marked(self, num, curr_drawn_idx):
        return num in self.drawn[: curr_drawn_idx + 1]

    def get_col(self, board, target_col):
        col = []
        for r in range(self.max_row):
            col.append(board[r][target_col])
        return col

    def get_unmarked_sum(self, board_idx, curr_drawn_idx):
        unmarked_sum = 0
        for r in range(self.max_row):
            for c in range(self.max_col):
                num_at_pos = self.get_num_on_board(board_idx, r, c)
                if not self.is_marked(num_at_pos, curr_drawn_idx):
                    unmarked_sum += num_at_pos

        return unmarked_sum

    def is_winner(self, board_idx, curr_drawn_idx):
        (sr, sc) = self.get_pos_on_board(board_idx, self.drawn[curr_drawn_idx])
        if not sr and not sc:
            return False
        cr = self.boards[board_idx][sr]
        cc = self.get_col(self.boards[board_idx], sc)

        full_row = full_col = True
        for item in cr:
            if not self.is_marked(item, curr_drawn_idx):
                full_row = False
                break

        for item in cc:
            if not self.is_marked(item, curr_drawn_idx):
                full_col = False
                break

        return full_row or full_col

    # Part 1
    def bingo(self):
        for drawn_idx in range(len(self.drawn)):
            for board_idx in range(len(self.boards)):
                win = self.is_winner(board_idx, drawn_idx)
                if win:
                    return (
                        self.get_unmarked_sum(board_idx, drawn_idx)
                        * self.drawn[drawn_idx]
                    )

    # Part 2
    def last_win(self):
        boards_indexes = set(range(len(self.boards)))
        for drawn_idx in range(len(self.drawn)):
            for board_idx in boards_indexes.copy():
                win = self.is_winner(board_idx, drawn_idx)
                if win:
                    boards_indexes.remove(board_idx)
                if len(boards_indexes) == 0:
                    return (
                        self.get_unmarked_sum(board_idx, drawn_idx)
                        * self.drawn[drawn_idx]
                    )


if __name__ == "__main__":
    sol = Day4()
    sol.part1()
    sol.part2()
