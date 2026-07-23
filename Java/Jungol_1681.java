import java.io.*;
import java.util.*;

public class Jungol_1681 {
    static final int INF = 987654321;
    static int num;
    static int[][] board;
    static int[][] DP;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        num = Integer.parseInt(st.nextToken());
        board = new int[num][num];

        for (int row=0; row < num; row++) {
            st = new StringTokenizer(br.readLine().trim());

            for (int col=0; col < num; col++) {
                board[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        int total = 1 << num;
        DP = new int[total][num];
        for (int index=0; index < total; index++) {
            Arrays.fill(DP[index], INF);
        }
        DP[1][0] = 0;

        for (int visited=1; visited < total; visited++) {
            for (int curr=0; curr < num; curr++) {
                if ((visited & (1 << curr)) == 0 || DP[visited][curr] == INF) {
                    continue;
                }

                for (int next=0; next < num; next++) {
                    if ((visited & (1 << next)) != 0 || board[curr][next] == 0) {
                        continue;
                    }

                    int nextVisited = visited ^ (1 << next);
                    DP[nextVisited][next] = Math.min(DP[nextVisited][next], DP[visited][curr] + board[curr][next]);
                }
            }
        }

        int answer = Integer.MAX_VALUE;
        for (int index=1; index < num; index++) {
            if (board[index][0] == 0) {
                continue;
            }
            
            answer = Math.min(answer, DP[total-1][index] + board[index][0]);
        }

        System.out.println(answer);
    }
}
