import java.io.*;
import java.util.*;

public class BOJ_18405 {
    static int N;
    static int K;
    static int[][] board;
    static PriorityQueue<Node> nodeQueue;

    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int S;
    static int answerRow;
    static int answerCol;


    static class Node implements Comparable<Node>{
        int row, col, virus;

        Node(int row, int col, int virus) {
            this.row = row;
            this.col = col;
            this.virus = virus;
        }

        @Override
        public int compareTo (Node o) {
            if (this.virus < o.virus) {
                return -1;
            }

            else if (this.virus > o.virus) {
                return 1;
            }

            return 0;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        board = new int[N + 2][N + 2];
        nodeQueue = new PriorityQueue<>();

        for (int row = 0; row < N + 2; row ++) {
            Arrays.fill(board[row], -1);
        }

        for (int row = 1; row <= N; row ++) {
            st = new StringTokenizer(br.readLine().trim());

            for (int col = 1; col <= N; col ++) {
                int virus = Integer.parseInt(st.nextToken());
                board[row][col] = virus;

                if (virus != 0) {
                    nodeQueue.add(new Node(row, col, virus));
                }
            }
        }

        st = new StringTokenizer(br.readLine().trim());
        S = Integer.parseInt(st.nextToken());
        answerRow = Integer.parseInt(st.nextToken());
        answerCol = Integer.parseInt(st.nextToken());
        
        while (S-- > 0) {
            PriorityQueue<Node> nextQueue = new PriorityQueue<>();
            
            while (!nodeQueue.isEmpty()) {
                Node node = nodeQueue.poll();

                for (int way=0; way < 4; way ++) {
                    int nr = node.row + dx[way];
                    int nc = node.col + dy[way];

                    if (board[nr][nc] != 0) {
                        continue;
                    }
                    
                    board[nr][nc] = node.virus;
                    nextQueue.add(new Node(nr, nc, node.virus));
                }
            }

            nodeQueue = nextQueue;
        }
        
        System.out.println(board[answerRow][answerCol]);
    }
}