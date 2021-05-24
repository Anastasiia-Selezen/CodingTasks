class Solution:
    def __init__(self, grid):
        # Check that grid has appropriate type
        try:
            if type(grid) is list:
                self.grid = grid
        except TypeError:
            raise TypeError('Grid must be a list, not "%s"' % type(grid))

    def num_islands(self):
        """Function for counting number of islands

            Returns:
            int: number of islands

        """
        # Check that grid is not empty
        if not self.grid:
            return 0
        islands = 0
        for row_index in range(len(self.grid)):
            for col_index in range(len(self.grid[0])):
                # Going by rows and columns,
                # when finding "1" - update counter for islands
                # and check neighbors by vertical and horizontal to find the whole island
                if self.grid[row_index][col_index] == '1':
                    islands += 1
                    self._check_neighbors(row_index, col_index)
        return islands

    def _check_neighbors(self, row_index, col_index):
        """Function for checking all neighbors for the current item in order to determine the whole island

            Parameters:
            row_index (int): position index for rows
            col_index (int): position index for columns

        """
        # Checking that row_index and col_index are not out of boundary
        # Also checking that the value is not "0"
        if row_index < 0 or row_index >= len(self.grid) \
                or col_index < 0 or col_index >= len(self.grid[0]) \
                or self.grid[row_index][col_index] == '0':
            return 0
        # Change the value to "0" to mark as visited item to avoid counting the same island twice
        self.grid[row_index][col_index] = '0'
        # Recursively checking if the neighbors by vertical or horizontal also has the value "1"
        self._check_neighbors(row_index + 1, col_index)
        self._check_neighbors(row_index - 1, col_index)
        self._check_neighbors(row_index, col_index + 1)
        self._check_neighbors(row_index, col_index - 1)


if __name__ == '__main__':
    fairytale_map = [["1", "1", "1", "1", "0"],
                     ["1", "1", "0", "1", "0"],
                     ["1", "1", "0", "0", "0"],
                     ["0", "0", "0", "0", "0"]]
    num_of_islands = Solution(fairytale_map).num_islands()
    print("Number of Islands: " + str(num_of_islands))
