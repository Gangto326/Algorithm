class Solution {
    public int solution(int[] money) {
        int num = money.length;
        int answer = Math.max(money[0], money[1]);
        
        int[] DP = new int[num + 1];
        DP[1] = money[0];
        
        for (int index = 1, end = num - 1; index < end; index++) {
            DP[index + 1] = Math.max(DP[index], DP[index - 1] + money[index]);
            answer = Math.max(answer, DP[index + 1]);
        }
        
        DP = new int[num];
        DP[1] = money[1];
        
        for (int index = 2; index < num; index++) {
            DP[index] = Math.max(DP[index - 1], DP[index - 2] + money[index]);
            answer = Math.max(answer, DP[index]);
        }
        
        return answer;
    }
}