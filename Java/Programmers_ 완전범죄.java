import java.util.*;

class Solution {
    static final int MAX_VALUE = 1_000_000;
    
    public int solution(int[][] info, int n, int m) {
        int[] DP = new int[121];
        Arrays.fill(DP, MAX_VALUE);
        DP[0] = 0;
        
        for (int[] i: info) {
            DP[0] += i[1];
        }
        
        for (int[] i: info) {
            for (int index = 120; index >= 0; index--) {
                if (DP[index] != MAX_VALUE) {
                    DP[index + i[0]] = Math.min(DP[index] - i[1], DP[index + i[0]]);
                }
            }
        }
        
        int answer = -1;
        for (int index = 0; index < n; index++) {
            if (DP[index] < m) {
                answer = index;
                break;
            }
        }
        
        return answer;
    }
}