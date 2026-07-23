import java.io.*;
import java.util.*;

public class Jungol_1696 {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int num;
    static int[][] board;

    static class Node {
        int row, col, count;

        Node(int row, int col, int count) {
            this.row = row;
            this.col = col;
            this.count = count;
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        num = Integer.parseInt(br.readLine());
        board = new int[num][num];

        for (int row=0; row < num; row++) {
            String rowString = br.readLine().trim();

            for (int col=0; col < num; col++) {
                board[row][col] = rowString.charAt(col) - '0';
            }
        }

        ArrayDeque<Node> BFS = new ArrayDeque<>();
        BFS.add(new Node(0, 0, 0));

        boolean[][] check = new boolean[num][num];
        check[0][0] = true;
        
        int answer = 0;
        while (!BFS.isEmpty()) {
            Node node = BFS.poll();

            if (node.row == num - 1 && node.col == num -1) {
                answer = node.count;
                break;
            }

            for (int way=0; way < 4; way++) {
                int nr = node.row + dx[way];
                int nc = node.col + dy[way];

                if (0 <= nr && nr < num && 0 <= nc && nc < num) {
                    if (!check[nr][nc]) {
                        check[nr][nc] = true;

                        if (board[nr][nc] == 1) {
                            BFS.addFirst(new Node(nr, nc, node.count));
                        }
                        else {
                            BFS.add(new Node(nr, nc, node.count + 1));
                        }
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
