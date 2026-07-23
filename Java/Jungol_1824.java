import java.io.*;
import java.util.*;

public class Jungol_1824 {
    static int[][] board;
    static boolean[][] rowCheck;
    static boolean[][] colCheck;
    static boolean[][] blockCheck;

    static ArrayList<Point> pointList;
    static int pointCount;
    static StringBuilder answer;
    
    static boolean DFS(int index) {
        if (index >= pointCount) {
            for (int row=0; row < 9; row++) {
                for (int col=0; col < 9; col++) {
                    if (col > 0) {
                        answer.append(' ');
                    }
                    answer.append(board[row][col]);
                }

                answer.append("\n");
            }
            return true;
        }

        Point point = pointList.get(index);
        for (int num=1; num <= 9; num++) {
            if (
                !rowCheck[point.row][num] && 
                !colCheck[point.col][num] && 
                !blockCheck[((point.row / 3) * 3) + (point.col / 3)][num]
            ) {
                rowCheck[point.row][num] = true;
                colCheck[point.col][num] = true;
                blockCheck[((point.row / 3) * 3) + (point.col / 3)][num] = true;
                board[point.row][point.col] = num;

                if (DFS(index + 1)) {
                    return true;
                }

                rowCheck[point.row][num] = false;
                colCheck[point.col][num] = false;
                blockCheck[((point.row / 3) * 3) + (point.col / 3)][num] = false;
                board[point.row][point.col] = 0;
                }
        }

        return false;
    }

    static class Point {
        int row, col;

        Point(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        board = new int[9][9];
        rowCheck = new boolean[9][10];
        colCheck = new boolean[9][10];
        blockCheck = new boolean[9][10];
        answer = new StringBuilder();

        pointList = new ArrayList<>();

        for (int row=0; row < 9; row++) {
            st = new StringTokenizer(br.readLine());

            for (int col=0; col < 9; col++) {
                board[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        for (int row=0; row < 9; row++) {
            for (int col=0; col < 9; col++) {
                if (board[row][col] != 0) {
                    rowCheck[row][board[row][col]] = true;
                    colCheck[col][board[row][col]] = true;
                    blockCheck[((row / 3) * 3) + (col / 3)][board[row][col]] = true;
                }
                else {
                    pointList.add(new Point(row, col));
                }
            }
        }

        pointCount = pointList.size();
        DFS(0);

        System.out.print(answer);
    }
}
