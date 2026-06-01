import unittest
from humidifier import solve

class TestHumidifier(unittest.TestCase):
    def test_example_1(self):
        input_data = """4
1 3
3 1
4 4
7 1"""
        self.assertEqual(solve(input_data), "3")

    def test_example_2(self):
        input_data = """3
1 8
10 11
21 5"""
        self.assertEqual(solve(input_data), "5")

    def test_example_3(self):
        input_data = """10
2 1
22 10
26 17
29 2
45 20
47 32
72 12
75 1
81 31
97 7"""
        self.assertEqual(solve(input_data), "57")

if __name__ == "__main__":
    unittest.main()
