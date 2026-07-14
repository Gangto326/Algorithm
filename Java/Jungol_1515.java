import java.io.*;
import java.util.*;

public class Jungol_1515 {
    static int N;
    static int M;
    static int half;

    static int[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        half = (N / 2) + 1;

        board = new int[N + 1][N + 1];

        for (int queryNum = 0; queryNum < M; queryNum++) {
            st = new StringTokenizer(br.readLine());
            int heavy = Integer.parseInt(st.nextToken());
            int light = Integer.parseInt(st.nextToken());

            board[light][heavy] = 1;
            board[heavy][light] = -1;
        }

        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                if (board[i][k] == 0) {
                    continue;
                }

                for (int j = 1; j <= N; j++) {
                    if (board[k][j] == 0) {
                        continue;
                    }
                    
                    if (board[i][k] == board[k][j]) {
                        board[i][j] = board[i][k];
                    }
                }
            }
        }

        int answer = 0;
        for (int[] stone: board) {
            int hCount = 0;
            int lCount = 0;

            for (int index = 1; index <= N; index++) {
                if (stone[index] == 1) {
                    hCount += 1;
                }

                if (stone[index] == -1) {
                    lCount += 1;
                }
            }

            if (hCount >= half || lCount >= half) {
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}