import java.io.*;
import java.util.*;

public class Jungol_2000 {
    static int num;
    static int[] coinArray;
    static int total;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        coinArray = new int[num];

        st = new StringTokenizer(br.readLine());
        for (int index=0; index < num; index++) {
            coinArray[index] = Integer.parseInt(st.nextToken());
        }
        
        total = Integer.parseInt(br.readLine().trim());
        int[] DP = new int[total + 1];
        Arrays.fill(DP, -1);
        DP[0] = 0;

        for (int coin: coinArray) {
            for (int cost=coin; cost <= total; cost++) {
                if (DP[cost - coin] == -1) {
                    continue;
                }

                if (DP[cost] == -1) {
                    DP[cost] = DP[cost - coin] + 1;
                }
                else {
                    DP[cost] = Math.min(DP[cost], DP[cost - coin] + 1);
                }
            }
        }

        System.out.println(DP[total] != -1? DP[total]: "impossible");
    }
}
