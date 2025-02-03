import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findKthLargest(self):
        sol = Solution()

        # Test case 1
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        self.assertEqual(sol.findKthLargest(nums, k), expected)

        # Test case 2
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        self.assertEqual(sol.findKthLargest(nums, k), expected)

        # Test case 3
        nums = [1]
        k = 1
        expected = 1
        self.assertEqual(sol.findKthLargest(nums, k), expected)

        # Test case 4
        nums = [2, 1]
        k = 2
        expected = 1
        self.assertEqual(sol.findKthLargest(nums, k), expected)

        # Test case 5
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 5
        expected = 6
        self.assertEqual(sol.findKthLargest(nums, k), expected)

if __name__ == "__main__":
    unittest.main()