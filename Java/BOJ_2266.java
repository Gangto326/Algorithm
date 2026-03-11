import java.io.*;
import java.util.*;

public class BOJ_2266 {
    static int num;
    static int count;
    static int[][] DP;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        count = Integer.parseInt(st.nextToken());
        DP = new int[num + 1][count + 1];

        for (int fallCount = 1; fallCount <= num; fallCount ++) {
            for (int saveCount = 1; saveCount <= count; saveCount ++) {
                DP[fallCount][saveCount] = DP[fallCount - 1][saveCount - 1] + DP[fallCount - 1][saveCount] + 1;
            }

            if (DP[fallCount][count] >= num) {
                System.out.println(fallCount);
                break;
            }
        }
    }
}
