import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from board import Board
from game import Game


class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.grid = [[0] * 4 for _ in range(4)]
        self.board.score = 0

    def test_four_equal_tiles_make_two_merges(self):
        self.assertEqual(Board.slide_line([2, 2, 2, 2]), [4, 4, 0, 0])

    def test_separated_pairs_merge_once_each(self):
        self.assertEqual(Board.slide_line([2, 0, 2, 2]), [4, 2, 0, 0])

    def test_move_scores_merges(self):
        self.board.grid[0] = [2, 2, 2, 2]
        self.assertTrue(self.board.move_left())
        self.assertEqual(self.board.grid[0], [4, 4, 0, 0])
        self.assertEqual(self.board.score, 8)
        self.assertEqual(self.board.last_merges, [4, 4])

    def test_unchanged_move_reports_false(self):
        self.board.grid[0] = [2, 0, 0, 0]
        self.assertFalse(self.board.move_left())
        self.assertEqual(self.board.score, 0)

    def test_vertical_moves(self):
        self.board.grid[0][0] = 2
        self.board.grid[1][0] = 2
        self.assertTrue(self.board.move_up())
        self.assertEqual([row[0] for row in self.board.grid], [4, 0, 0, 0])


class GameTests(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.board.grid = [[0] * 4 for _ in range(4)]
        self.game.board.score = 0

    def test_successful_move_adds_one_tile_and_feedback(self):
        self.game.board.grid[0] = [2, 2, 0, 0]
        with patch.object(self.game.board, "add_random_tile") as add_tile:
            self.assertTrue(self.game.move("a"))
        add_tile.assert_called_once()
        self.assertIn("Moved left", self.game.last_feedback)
        self.assertIn("Merged 4", self.game.last_feedback)

    def test_unchanged_and_invalid_moves_add_no_tile(self):
        self.game.board.grid[0] = [2, 0, 0, 0]
        with patch.object(self.game.board, "add_random_tile") as add_tile:
            self.assertFalse(self.game.move("a"))
            self.assertFalse(self.game.move("x"))
        add_tile.assert_not_called()
        self.assertIn("Invalid", self.game.last_feedback)

    def test_undo_restores_board_score_and_consumes_undo(self):
        self.game.board.grid[0] = [2, 2, 0, 0]
        before = [row[:] for row in self.game.board.grid]
        with patch.object(self.game.board, "add_random_tile"):
            self.assertTrue(self.game.move("a"))
        self.assertEqual(self.game.board.score, 4)
        self.assertTrue(self.game.undo())
        self.assertEqual(self.game.board.grid, before)
        self.assertEqual(self.game.board.score, 0)
        self.assertFalse(self.game.undo())

    def test_best_score_is_kept_for_the_run(self):
        self.game.board.grid[0] = [2, 2, 0, 0]
        with patch.object(self.game.board, "add_random_tile"):
            self.game.move("a")
        self.assertEqual(self.game.best_score, 4)
        self.game.undo()
        self.assertEqual(self.game.best_score, 4)

    def test_win_and_no_move_detection(self):
        self.game.board.grid[0][0] = 2048
        self.assertTrue(self.game.board.has_won())
        self.game.board.grid = [
            [2, 4, 2, 4], [4, 2, 4, 2],
            [2, 4, 2, 4], [4, 2, 4, 2],
        ]
        self.assertFalse(self.game.board.can_move())

    def test_quit_command_exits(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="q"), redirect_stdout(output):
            self.game.run()
        self.assertIn("Thanks for playing", output.getvalue())


if __name__ == "__main__":
    unittest.main()
