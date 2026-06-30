import unittest

from sudoku import (
    create_grid,
    find_empty_positions,
    find_possible_values,
    get_block,
    get_col,
    get_row,
    group,
    read_sudoku,
    solve,
    check_solution,
)


class SudokuTestCase(unittest.TestCase):
    def test_group(self) -> None:
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(
            group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        )

    def test_get_row(self) -> None:
        grid = [["1", "2", "."], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(get_row(grid, (0, 0)), ["1", "2", "."])
        grid = [["1", "2", "3"], ["4", ".", "6"], ["7", "8", "9"]]
        self.assertEqual(get_row(grid, (1, 0)), ["4", ".", "6"])
        grid = [["1", "2", "3"], ["4", "5", "6"], [".", "8", "9"]]
        self.assertEqual(get_row(grid, (2, 0)), [".", "8", "9"])

    def test_get_col(self) -> None:
        grid = [["1", "2", "."], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(get_col(grid, (0, 0)), ["1", "4", "7"])
        grid = [["1", "2", "3"], ["4", ".", "6"], ["7", "8", "9"]]
        self.assertEqual(get_col(grid, (0, 1)), ["2", ".", "8"])
        grid = [["1", "2", "3"], ["4", "5", "6"], [".", "8", "9"]]
        self.assertEqual(get_col(grid, (0, 2)), ["3", "6", "9"])

    def test_get_block(self) -> None:
        grid = read_sudoku("puzzle1.txt")
        self.assertEqual(
            get_block(grid, (0, 1)),
            ["5", "3", ".", "6", ".", ".", ".", "9", "8"],
        )
        self.assertEqual(
            get_block(grid, (4, 7)),
            [".", ".", "3", ".", ".", "1", ".", ".", "6"],
        )
        self.assertEqual(
            get_block(grid, (8, 8)),
            ["2", "8", ".", ".", ".", "5", ".", "7", "9"],
        )

    def test_find_empty_positions(self) -> None:
        grid = [["1", "2", "."], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(find_empty_positions(grid), (0, 2))
        grid = [["1", "2", "3"], ["4", ".", "6"], ["7", "8", "9"]]
        self.assertEqual(find_empty_positions(grid), (1, 1))
        grid = [["1", "2", "3"], ["4", "5", "6"], [".", "8", "9"]]
        self.assertEqual(find_empty_positions(grid), (2, 0))

    def test_find_empty_positions_full(self) -> None:
        grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertIsNone(find_empty_positions(grid))

    def test_find_possible_values(self) -> None:
        grid = read_sudoku("puzzle1.txt")
        values = find_possible_values(grid, (0, 2))
        self.assertEqual(set(values), {"1", "2", "4"})
        values = find_possible_values(grid, (4, 7))
        self.assertEqual(set(values), {"2", "5", "9"})

    def test_solve(self) -> None:
        grid = read_sudoku("puzzle1.txt")
        solution = solve(grid)
        self.assertIsNotNone(solution)
        self.assertTrue(check_solution(solution))

    def test_check_solution_correct(self) -> None:
        grid = read_sudoku("puzzle1.txt")
        solution = solve(grid)
        self.assertTrue(check_solution(solution))

    def test_check_solution_incorrect_row(self) -> None:
        grid = read_sudoku("puzzle1.txt")
        solution = solve(grid)
        assert solution is not None
        solution[0][1] = solution[0][0]
        self.assertFalse(check_solution(solution))

    def test_check_solution_none(self) -> None:
        self.assertFalse(check_solution(None))


if __name__ == "__main__":
    unittest.main()
