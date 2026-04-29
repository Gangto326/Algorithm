class Solution {
    static final long MOD = 1_000_000_007L;
    static long[] DP;
    
    public int solution(int n, int[] money) {
        DP = new long[n + 1];
        DP[0] = 1;
        
        for (int cost: money) {
            for (int index = 0, end = n - cost; index <= end; index++) {
                DP[index + cost] += DP[index];
                DP[index + cost] %= MOD;
            }
        }
        
        return (int) (DP[n] % MOD);
    }
}