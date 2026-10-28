from board import Board


class Game:
    MOVES = {
        "a": ("left", "move_left"),
        "d": ("right", "move_right"),
        "w": ("up", "move_up"),
        "s": ("down", "move_down"),
    }

    def __init__(self):
        self.board = Board()
        self.best_score = self.board.score
        self._undo_state = None
        self.last_feedback = ""

    def display(self):
        print("\n+------+------+------+------+")
        for row in self.board.grid:
            print("|" + "|".join(f"{value:^6}" if value else f"{' ':^6}"
                                 for value in row) + "|")
            print("+------+------+------+------+")
        print(f"Score: {self.board.score}  Best: {self.best_score}")

    def move(self, key):
        """Apply one direction. Feedback is produced only at this action level."""
        if key not in self.MOVES:
            self.last_feedback = "Invalid move. Use W/A/S/D."
            return False

        direction, method_name = self.MOVES[key]
        before_grid = [row[:] for row in self.board.grid]
        before_score = self.board.score
        changed = getattr(self.board, method_name)()
        if not changed:
            self.last_feedback = "No tiles moved."
            return False

        self._undo_state = (before_grid, before_score)
        merges = list(self.board.last_merges)
        self.board.add_random_tile()
        self.best_score = max(self.best_score, self.board.score)
        self.last_feedback = f"Moved {direction}."
        if merges:
            self.last_feedback += " Merged " + ", ".join(map(str, merges)) + "."
        return True

    def undo(self):
        if self._undo_state is None:
            self.last_feedback = "There is no successful move to undo."
            return False
        grid, score = self._undo_state
        self.board.grid = [row[:] for row in grid]
        self.board.score = score
        self.board.last_merges = []
        self._undo_state = None
        self.last_feedback = "Undid the last move."
        return True

    def run(self):
        print("2048 - W/A/S/D to move, U to undo, Q to quit.")
        while True:
            self.display()
            if self.board.has_won():
                print("You reached 2048!")
                return
            if not self.board.can_move():
                print("No legal moves remain.")
                return
            key = input("> ").strip().lower()
            if key == "q":
                print("Thanks for playing.")
                return
            if key == "u":
                self.undo()
                print(self.last_feedback)
                continue
            self.move(key)
            print(self.last_feedback)
