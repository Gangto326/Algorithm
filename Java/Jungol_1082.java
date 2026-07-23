import java.io.*;
import java.util.*;

public class Jungol_1082 {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int rowNum;
    static int colNum;
    static char[][] board;

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
        board = new char[rowNum][colNum];

        ArrayDeque<Node> fireList = new ArrayDeque<>();
        ArrayDeque<Node> BFS = new ArrayDeque<>();
        boolean[][] check = new boolean[rowNum][colNum];

        for (int row=0; row < rowNum; row++) {
            String line = br.readLine().trim();

            for (int col=0; col < colNum; col++) {
                board[row][col] = line.charAt(col);

                if (board[row][col] == '*') {
                    fireList.add(new Node(row, col, 0));
                }
                else if (board[row][col] == 'S') {
                    BFS.add(new Node(row, col, 0));
                    check[row][col] = true;
                    board[row][col] = '.';
                }
            }
        }

        boolean flag = false;
        int answer = 0;
        while (!BFS.isEmpty()) {
            ArrayDeque<Node> nextFireList = new ArrayDeque<>();
            ArrayDeque<Node> nextBFS = new ArrayDeque<>();

            for (Node fire: fireList) {
                for (int way=0; way < 4; way++) {
                    int nr = fire.row + dx[way];
                    int nc = fire.col + dy[way];

                    if (0 <= nr && nr < rowNum && 0 <= nc && nc < colNum) {
                        if (board[nr][nc] == '.') {
                            nextFireList.add(new Node(nr, nc, 0));
                            board[nr][nc] = '*';
                        }
                    }
                }
            }

            while (!BFS.isEmpty()) {
                Node node = BFS.poll();

                for (int way=0; way < 4; way++) {
                    int nr = node.row + dx[way];
                    int nc = node.col + dy[way];

                    if (0 <= nr && nr < rowNum && 0 <= nc && nc < colNum) {
                        if (board[nr][nc] == '.' && !check[nr][nc]) {
                            check[nr][nc] = true;
                            nextBFS.add(new Node(nr, nc, node.count + 1));
                        }
                        else if (board[nr][nc] == 'D') {
                            flag = true;
                            answer = node.count + 1;
                        }
                    }
                }

                if (flag) {
                    break;
                }
            }
            
            if (!flag) {
                BFS = nextBFS;
            }
            
            fireList = nextFireList;
        }

        System.out.print(answer != 0? answer: "impossible");
    }
}
