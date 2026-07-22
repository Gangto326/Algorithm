import java.io.*;
import java.util.*;

public class Jungol_1677 {
    static int num;
    static int[][] board;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        board = new int[num][num];

        for (int row=0; row < num; row++) {
            st = new StringTokenizer(br.readLine());

            for (int col=0; col < num; col++) {
                board[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] DP = new int[num][num];
        for (int row=0; row < num; row++) {
            Arrays.fill(DP[row], Integer.MIN_VALUE);
        }

        DP[0][0] = board[0][0];

        for (int row=0; row < num; row++) {
            int[] rightRow = new int[num];
            int[] leftRow = new int[num];
            
            for (int col=0; col < num; col++) {
                rightRow[col] = DP[row][col];
                leftRow[col] = DP[row][col];
            }

            for (int col=0, end=num-1; col < end; col++) {
                int nc = col + 1;

                if (rightRow[nc] < rightRow[col] + board[row][nc]) {
                    rightRow[nc] = rightRow[col] + board[row][nc];
                }
            }
            
            if (row != 0) {
                for (int col=num-1; col >= 0; col--) {
                    int nc = col + -1;

                    if (0 <= nc && nc < num) {
                        if (leftRow[nc] < leftRow[col] + board[row][nc]) {
                            leftRow[nc] = leftRow[col] + board[row][nc];
                        }
                    }
                }
            }

            if (row == num-1) {
                System.out.println(rightRow[num-1]);
                break;
            }

            for (int col=0; col < num; col++) {
                int nr = row + 1;
                DP[nr][col] = Math.max(rightRow[col], leftRow[col]) + board[nr][col];
            }
        }
    }
}
