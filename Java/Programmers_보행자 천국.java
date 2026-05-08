class Solution {
    static final int[] dx = {0, -1};
    static final int[] dy = {-1, 0};
    int MOD = 20170805;
    
    public int solution(int m, int n, int[][] cityMap) {
        int[][][] DP = new int[2][m][n];
        DP[0][0][0] = 1;
        
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                for (int way = 0; way < 2; way++) {
                    int nr = row + dx[way];
                    int nc = col + dy[way];
                    
                    if (nr < 0 || nc < 0) {
                        continue;
                    }
                    
                    if (cityMap[nr][nc] == 0) {
                        DP[way][row][col] += DP[0][nr][nc] + DP[1][nr][nc];
                        DP[way][row][col] %= MOD;
                    }
                    
                    if (cityMap[nr][nc] == 2) {
                        DP[way][row][col] += DP[way][nr][nc];
                        DP[way][row][col] %= MOD;
                    }
                }
            }
        }
        
        int answer = (DP[0][m-1][n-1] + DP[1][m-1][n-1]) % MOD;
        return answer;
    }
}