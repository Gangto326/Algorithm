import java.io.*;
import java.util.*;

public class BOJ_14677 {
    static int num;
    static char[] pillArray;
    static int[][] DP;

    static final char[] sequence = {'B', 'L', 'D'};


    static int DFS(int left, int right, int index) {
        if (left > right) {
            return 0;
        }

        if (DP[left][right] > -1) {
            return DP[left][right];
        }

        char pill = sequence[index % 3];
        int maxCount = 0;

        if (pillArray[left] == pill) {
            maxCount = Math.max(maxCount, DFS(left + 1, right, index + 1) + 1);
        }

        if (pillArray[right] == pill) {
            maxCount = Math.max(maxCount, DFS(left, right - 1, index + 1) + 1);
        }

        DP[left][right] = maxCount;
        return DP[left][right];
    }


    public static void main(String[] arg) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        num = Integer.parseInt(st.nextToken());
        pillArray = new char[num * 3];
        DP = new int[num * 3][num * 3];

        st = new StringTokenizer(br.readLine().trim());
        String pills = st.nextToken();
        for (int index = 0, end = num * 3; index < end; index ++) {
            pillArray[index] = pills.charAt(index);
            Arrays.fill(DP[index], -1);
        }

        DFS(0, num * 3 - 1, 0);

        System.out.println(DP[0][num * 3 -1]);
    }
}
