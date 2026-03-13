import java.io.*;
import java.util.*;

public class BOJ_32349 {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int rowNum;
    static int colNum;

    static int[][] board;
    static int[][] nextBoard;
    static int[][] answerBoard;
    static boolean[][] checkBoard;

    static Point[] pointArray;
    static int count;
    static int answerCount;
    static int answer;


    static class Point {
        int row, col, index;

        Point(int row, int col, int index) {
            this.row = row;
            this.col = col;
            this.index = index;
        }
    }


    static void clear() {
        for (int row = 1; row <= rowNum; row++) {
            for (int col = 1; col <= colNum; col++) {
                checkBoard[row][col] = false;
            }
        }
    }


    static boolean DFS(int index) {
        Point point = pointArray[index];

        if (checkBoard[point.row][point.col]) {
            return false;
        }

        checkBoard[point.row][point.col] = true;

        for (int way = 0; way < 4; way++) {
            int nr = point.row + dx[way];
            int nc = point.col + dy[way];

            if (answerBoard[nr][nc] != 1) {
                continue;
            }

            if (nextBoard[nr][nc] == 0 || DFS(nextBoard[nr][nc])) {
                nextBoard[nr][nc] = index;
                return true;
            }
        }

        return false;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        colNum = Integer.parseInt(st.nextToken());
        rowNum = Integer.parseInt(st.nextToken());

        board = new int[rowNum + 2][colNum + 2];
        nextBoard = new int[rowNum + 2][colNum + 2];
        answerBoard = new int[rowNum + 2][colNum + 2];
        checkBoard = new boolean[rowNum + 2][colNum + 2];

        count = 0;
        answerCount = 0;
        answer = 0;

        for (int rowIndex = 0, end = rowNum + 2; rowIndex < end; rowIndex++) {
            Arrays.fill(board[rowIndex], -1);
            Arrays.fill(answerBoard[rowIndex], -1);
        }

        for (int row = 1; row <= rowNum; row++) {
            st = new StringTokenizer(br.readLine());

            for (int col = 1; col <= colNum; col++) {
                int num = Integer.parseInt(st.nextToken());
                board[row][col] = num;

                if (num == 1) {
                    count += 1;
                }
            }
        }

        for (int row = 1; row <= rowNum; row++) {
            st = new StringTokenizer(br.readLine());

            for (int col = 1; col <= colNum; col++) {
                int num = Integer.parseInt(st.nextToken());
                answerBoard[row][col] = num;

                if (num == 1) {
                    answerCount += 1;
                }
                
                if (answerBoard[row][col] == 1 && board[row][col] == answerBoard[row][col]) {
                    answerBoard[row][col] = 0;
                    board[row][col] = 0;
                    
                    count -= 1;
                    answerCount -= 1;
                }
            }
        }

        if (count != answerCount) {
            System.out.println(-1);
            return;
        }

        pointArray = new Point[count + 1];
        int pointIndex = 1;

        for (int row = 1; row <= rowNum; row++) {
            for (int col = 1; col <= colNum; col++) {
                if (board[row][col] == 1) {
                    pointArray[pointIndex++] = new Point(row, col, pointIndex);
                }
            }
        }

        for (int index = 1; index < pointIndex; index++) {
            clear();

            if (DFS(index)) {
                answer += 1;
            }
        }

        answer += ((answerCount - answer) * 2);
        System.out.println(answer);
    }
}
