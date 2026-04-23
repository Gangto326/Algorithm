import java.io.*;
import java.util.*;

class Solution {
    static int num;
    static int[] DP;
    static int answer;
    
    public int solution(int sticker[]) {
        num = sticker.length;
        
        if (num == 1) {
            return sticker[0];
        }
        
        answer = 0;
        DP = new int[num];
        DP[0] = sticker[0];
        DP[1] = sticker[0];
        
        for (int i = 2, end = num - 1; i < end; i++) {
            DP[i] = Math.max(DP[i - 2] + sticker[i], DP[i - 1]);
        }
        
        answer = DP[num - 2];
        
        DP = new int[num];
        DP[1] = sticker[1];
        
        for (int i = 2; i < num; i++) {
            DP[i] = Math.max(DP[i - 2] + sticker[i], DP[i - 1]);
        }
        
        answer = Math.max(answer, DP[num - 1]);
        
        return answer;
    }
}