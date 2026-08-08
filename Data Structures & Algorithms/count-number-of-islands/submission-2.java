class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int columns = grid[0].length;
        int numOfIslands = 0;
        Set visited = new HashSet<String>();

        for (int r = 0; r < rows; r ++) {
            for (int c = 0; c < columns; c ++) {
                if (isLand(grid, r, c) && !visited.contains(r + "-" + c)) {
                    goToLand(grid, r, c, visited);
                    numOfIslands ++;
                }
            }
        }
        return numOfIslands;
    }

    public static boolean isLand(char[][] grid, int r, int c) {
        return grid[r][c] == '1';
    }

    public static void goToLand(char[][] grid, int r, int c, Set visited) {
        if ((r < 0 || r >= grid.length)  || (c < 0 || c >= grid[0].length)) {
            return;
        }

        if (!isLand(grid, r, c)) {
            return;
        }

        if (visited.contains(r + "-" + c)) {
            return;
        }

        visited.add((r + "-" + c));

        goToLand(grid, r - 1, c, visited);
        goToLand(grid, r + 1, c, visited);
        goToLand(grid, r, c - 1, visited);
        goToLand(grid, r, c + 1, visited);

        return;
    }
}