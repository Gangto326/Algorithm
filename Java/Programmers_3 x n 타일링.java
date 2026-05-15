class Solution {
    static final int MOD = 1_000_000_007;
    static long[] DP;
    static long sum;
    
    public int solution(int n) {
        if (n % 2 == 1) {
            return 0;
        }

        DP = new long[n + 1];
        sum = 0;
        
        DP[2] = 3;
        for (int i = 4; i <= n; i += 2) {
            DP[i] = (DP[i - 2] * 3 + sum * 2 + 2) % MOD;
            sum += DP[i - 2];
        }

        return (int) DP[n];
    }
}