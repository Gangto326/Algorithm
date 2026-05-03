class Solution {
    public int solution(int n, int[][] results) {
        int[][] DP = new int[n + 1][n + 1];
        
        for (int[] result: results) {
            DP[result[1]][result[0]] = 1;
            DP[result[0]][result[1]] = -1;
        }
        
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (i == j) {
                        continue;
                    }
                    
                    if (DP[i][j] == 0 && DP[i][k] == DP[k][j]) {
                        DP[i][j] = DP[i][k];
                    }
                }
            }
        }
        
        int answer = 0;
        
        for (int index = 1; index <= n; index++) {
            boolean flag = true;
            
            for (int fight = 1; fight <= n; fight++) {
                if (index == fight) {
                    continue;
                }
                
                if (DP[index][fight] == 0) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                answer += 1;
            }
        }
        
        return answer;
    }
}