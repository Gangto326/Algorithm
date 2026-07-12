import java.io.*;
import java.util.*;

public class Jungol_1494 {
    static int N;
    static int M;
    static int T;
    static int[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        board = new int[N + 1][N + 1];
        for (int index = 0; index <= N; index++) {
            Arrays.fill(board[index], Integer.MAX_VALUE);
        }

        for (int query_num = 0; query_num < M; query_num++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            board[start][end] = Math.min(board[start][end], cost);
        }

        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                if (board[i][k] == Integer.MAX_VALUE) {
                    continue;
                }

                for (int j = 1; j <= N; j++) {
                    if (i == j) {
                        continue;
                    }

                    if (board[i][j] > Math.max(board[i][k], board[k][j])) {
                        board[i][j] = Math.max(board[i][k], board[k][j]);
                    }
                }
            }
        }

        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            answer.append(board[start][end] != Integer.MAX_VALUE? board[start][end]: -1).append("\n");
        }

        System.out.print(answer);
    }
}