import java.io.*;
import java.util.*;

public class Jungol_1409 {
    static int num;
    static int[][] board;
    static int queryNum;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        board = new int[num+1][num+1];
        for (int index=0; index <= num; index++) {
            Arrays.fill(board[index], Integer.MAX_VALUE);
        }

        st = new StringTokenizer(br.readLine());
        board[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 0;

        queryNum = Integer.parseInt(br.readLine());
        for (int queryIndex=0; queryIndex < queryNum; queryIndex++) {
            int query = Integer.parseInt(br.readLine());
            
            int[][] nextBoard = new int[num+1][num+1];
            for (int index=0; index <= num; index++) {
                Arrays.fill(nextBoard[index], Integer.MAX_VALUE);
            }

            for (int first=1; first <= num; first++) {
                for (int sec=1; sec <= num; sec++) {
                    if (board[first][sec] != Integer.MAX_VALUE) {
                        nextBoard[query][sec] = Math.min(nextBoard[query][sec], board[first][sec] + Math.abs(first - query));
                        nextBoard[first][query] = Math.min(nextBoard[first][query], board[first][sec] + Math.abs(sec - query));
                    }
                }
            }

            board = nextBoard;
        }

        int answer = Integer.MAX_VALUE;

        for (int first=1; first <= num; first++) {
            for (int sec=1; sec <= num; sec++) {
                answer = Math.min(answer, board[first][sec]);
            }
        }

        System.out.print(answer);
    }
}
