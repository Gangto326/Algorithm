import java.io.*;
import java.util.*;

public class Jungol_1603 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] x = new int[n + 1];
        int[] y = new int[n + 1];

        x[0] = 0;
        y[0] = 0;

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dist = new int[n + 1][n + 1];
        int[] distToT = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            distToT[i] = getFuel(x[i], y[i], 10000, 10000);
            for (int j = 0; j <= n; j++) {
                if (i != j) {
                    dist[i][j] = getFuel(x[i], y[i], x[j], y[j]);
                }
            }
        }

        int left = 1;
        int right = 1415;
        int ans = 1415;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canReach(n, k, mid, dist, distToT)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(ans);
    }

    private static int getFuel(int x1, int y1, int x2, int y2) {
        int dx = x1 - x2;
        int dy = y1 - y2;
        double len = Math.sqrt(dx * dx + dy * dy);
        
        return (int) Math.ceil(len / 10.0);
    }

    private static boolean canReach(int n, int k, int mid, int[][] dist, int[] distToT) {
        boolean[] check = new boolean[n + 1];
        int[] count = new int[n + 1];
        
        int[] q = new int[n + 1]; 
        int head = 0, tail = 0;

        q[tail++] = 0;
        check[0] = true;
        count[0] = 0;

        while (head < tail) {
            int curr = q[head++];

            if (distToT[curr] <= mid) {
                return true;
            }

            if (count[curr] == k) {
                continue;
            }

            for (int nxt = 1; nxt <= n; nxt++) {
                if (!check[nxt] && dist[curr][nxt] <= mid) {
                    check[nxt] = true;
                    count[nxt] = count[curr] + 1;
                    q[tail++] = nxt;
                }
            }
        }

        return false;
    }
}