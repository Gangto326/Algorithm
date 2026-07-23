import java.io.*;
import java.util.*;

public class Jungol_1681 {
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
            Arrays.fill(DP[index], Integer.MAX_VALUE);
        }
        
        for (int index=0; index < num; index++) {
            DP[1 << index][index] = board[0][index] > 0? board[0][index]: Integer.MAX_VALUE;
        }

        for (int comb=0; comb < total; comb++) {
            for (int index=0; index < num; index++) {
                int indexBit = 1 << index;

                if ((comb & indexBit) == 0) {
                    continue;
                }

                int prev = comb - indexBit;
                for (int beforeIndex=0; beforeIndex < num; beforeIndex++) {
                    if (DP[prev][beforeIndex] == Integer.MAX_VALUE) {
                        continue;
                    }

                    if (board[beforeIndex][index] == 0) {
                        continue;
                    }

                    DP[comb][index] = Math.min(DP[comb][index], DP[prev][beforeIndex] + board[beforeIndex][index]);
                }
            }
        }

        int answer = Integer.MAX_VALUE;
        for (int index=1; index < num; index++) {
            answer = Math.min(answer, DP[total-1][index] + board[index][0]);
        }

        System.out.println(DP[total-1][0]);
    }
}
