import random

SIZE = 4


class Board:
    def __init__(self):
        self.grid = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.last_merges = []
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty = [(r, c) for r in range(SIZE) for c in range(SIZE)
                 if self.grid[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 4 if random.random() < 0.1 else 2

    @staticmethod
    def _merge_line(line):
        """Compress a line and merge each original tile no more than once."""
        values = [value for value in line if value]
        result = []
        merges = []
        index = 0
        while index < len(values):
            if index + 1 < len(values) and values[index] == values[index + 1]:
                merged_value = values[index] * 2
                result.append(merged_value)
                merges.append(merged_value)
                index += 2
            else:
                result.append(values[index])
                index += 1
        result.extend([0] * (SIZE - len(result)))
        return result, merges

    @staticmethod
    def slide_line(line):
        """Return the resulting line, keeping the starter API convenient."""
        return Board._merge_line(line)[0]

    def _move_lines(self, lines, write_line):
        changed = False
        merges = []
        for index, old in enumerate(lines):
            new, line_merges = self._merge_line(old)
            write_line(index, new)
            changed |= old != new
            merges.extend(line_merges)
        self.last_merges = merges if changed else []
        self.score += sum(self.last_merges)
        return changed

    def move_left(self):
        return self._move_lines(
            [row[:] for row in self.grid],
            lambda r, row: self.grid.__setitem__(r, row),
        )

    def move_right(self):
        lines = [list(reversed(row)) for row in self.grid]

        def write(r, line):
            self.grid[r] = list(reversed(line))

        return self._move_lines(lines, write)

    def move_up(self):
        lines = [[self.grid[r][c] for r in range(SIZE)] for c in range(SIZE)]

        def write(c, line):
            for r, value in enumerate(line):
                self.grid[r][c] = value

        return self._move_lines(lines, write)

    def move_down(self):
        lines = [list(reversed([self.grid[r][c] for r in range(SIZE)]))
                 for c in range(SIZE)]

        def write(c, line):
            for r, value in enumerate(reversed(line)):
                self.grid[r][c] = value

        return self._move_lines(lines, write)

    def can_move(self):
        if any(0 in row for row in self.grid):
            return True
        for r in range(SIZE):
            for c in range(SIZE):
                if c + 1 < SIZE and self.grid[r][c] == self.grid[r][c + 1]:
                    return True
                if r + 1 < SIZE and self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False

    def has_won(self):
        return any(2048 in row for row in self.grid)
