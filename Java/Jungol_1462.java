import java.io.*;
import java.util.*;

public class Jungol_1462 {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int rowNum;
    static int colNum;
    static char[][] board;
    static ArrayDeque<Node> BFS;
    static boolean[][] check;
    static int answer;

    static void clearArray() {
        BFS.clear();

        for (int row=1; row <= rowNum; row++) {
            for (int col=1; col <= colNum; col++) {
                check[row][col] = false;
            }
        }
    }

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
        StringTokenizer st = new StringTokenizer(br.readLine());

        rowNum = Integer.parseInt(st.nextToken());
        colNum = Integer.parseInt(st.nextToken());
        board = new char[rowNum + 2][colNum + 2];
        for (int index=0, end=rowNum+2; index < end; index++) {
            Arrays.fill(board[index], 'W');
        }

        for (int row=1; row <= rowNum; row++) {
            String line = br.readLine().trim();
            
            for (int col=1; col <= colNum; col++) {
                board[row][col] = line.charAt(col-1);
            }
        }

        BFS = new ArrayDeque<>();
        check = new boolean[rowNum + 2][colNum + 2];
        answer = 0;

        for (int row=1; row <= rowNum; row++) {
            for (int col=1; col <= colNum; col++) {
                clearArray();

                if (board[row][col] == 'L') {
                    BFS.add(new Node(row, col, 0));
                    check[row][col] = true;

                    while (!BFS.isEmpty()) {
                        Node node = BFS.poll();

                        answer = Math.max(answer, node.count);
                        int nextCount = node.count + 1;

                        for (int way=0; way < 4; way++) {
                            int nr = node.row + dx[way];
                            int nc = node.col + dy[way];
                            
                            if (board[nr][nc] == 'L' && !check[nr][nc]) {
                                check[nr][nc] = true;
                                BFS.add(new Node(nr, nc, nextCount));
                            }
                        }
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
