import java.io.*;
import java.util.*;

public class BOJ_17836 {
    static int rowNum;
    static int colNum;
    static int time;
    static int[][] board;

    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static boolean[][][] check;


    static class Node {
        int row, col, count, gram;

        Node(int row, int col, int count, int gram) {
            this.row = row;
            this.col = col;
            this.count = count;
            this.gram = gram;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        rowNum = Integer.parseInt(st.nextToken());
        colNum = Integer.parseInt(st.nextToken());
        time = Integer.parseInt(st.nextToken());

        board = new int[rowNum + 2][colNum + 2];
        for (int index = 0; index < rowNum + 2; index++){
            Arrays.fill(board[index], -1);
        }

        for (int row = 1; row <= rowNum; row++) {
            st = new StringTokenizer(br.readLine());

            for (int col = 1; col <= colNum; col++) {
                board[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        check = new boolean[rowNum + 2][colNum + 2][2];
        check[1][1][0] = true;

        ArrayDeque<Node> BFS = new ArrayDeque<>();
        BFS.add(new Node(1, 1, 0, 0));

        int answer = -1;
        while (!BFS.isEmpty()) {
            Node node = BFS.pollFirst();

            if (node.count > time) {
                continue;
            }

            if (node.row == rowNum && node.col == colNum) {
                answer = node.count;
                break;
            }

            for (int way = 0; way < 4; way++) {
                int nr = node.row + dx[way];
                int nc = node.col + dy[way];

                if (board[nr][nc] == -1) {
                    continue;
                }

                if (board[nr][nc] == 1 && node.gram == 0) {
                    continue;
                }
                
                int nextGram = node.gram;
                if (board[nr][nc] == 2) {
                    nextGram = 1;
                }

                if (check[nr][nc][nextGram]) {
                    continue;
                }

                check[nr][nc][nextGram] = true;
                BFS.add(new Node(nr, nc, node.count + 1, nextGram));
            }
        }

        if (answer != -1) {
            System.out.println(answer);
        }
        else {
            System.out.println("Fail");
        }
    }
}
