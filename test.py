import unittest
from main import count_words

class TestWordSearch(unittest.TestCase):
    def test_no_match(self):
        matrix = [
            list("AAAAA"),
            list("BBBBB"),
            list("CCCCC")
        ]
        self.assertEqual(count_words(matrix, "HELLO"), 0)
    
    def test_horizontal_match(self):
        matrix = [
            list("HELLO"),
            list("WORLD"),
            list("XXXXX")
        ]
        self.assertEqual(count_words(matrix, "HELLO"), 1)

    def test_vertical_match(self):
        matrix = [
            list("HXXXX"),
            list("EXXXX"),
            list("LXXXX"),
            list("LXXXX"),
            list("OXXXX"),
        ]
        self.assertEqual(count_words(matrix, "HELLO"), 1)

    def test_diagonal_match(self):
        matrix = [
            list("H...."),
            list(".E..."),
            list("..L.."),
            list("...L."),
            list("....O")
        ]
        self.assertEqual(count_words(matrix, "HELLO"), 1)

    def test_backwards_match(self):
        matrix = [
            list("OLLEH"),
            list("WORLD"),
            list("XXXXX")
        ]
        self.assertEqual(count_words(matrix, "HELLO"), 1)

    def test_backwards_diagonal_match(self):
        matrix = [
            list("....H"),
            list("...E."),
            list("..L.."),
            list(".L..."),
            list("O....")
        ]
        self.assertEqual(count_words(matrix, "HELLO"), 1)

    def test_multiple_matches(self):
        matrix = [
            list("..H.H"),
            list("..EE."),
            list("HELLO"),
            list(".LL.."),
            list("O.O..")
        ]
        result = count_words(matrix, "HELLO")
        self.assertEqual(result, 3)

    def test_original_input(self):
        matrix = [
            list("MMMSXXMASM"),
            list("MSAMXMSMSA"),
            list("AMXSXMAAMM"),
            list("MSAMASMSMX"),
            list("XMASAMXAMM"),
            list("XXAMMXXAMA"),
            list("SMSMSASXSS"),
            list("SAXAMASAAA"),
            list("MAMMMXMMMM"),
            list("MXMXAXMASX"),
        ]
        self.assertEqual(count_words(matrix, "XMAS"), 18)