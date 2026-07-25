import java.util.*;

class Solution {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};
    
    public class Node {
        int row, col, count, key, enter, flip;
        
        Node(int row, int col, int count, int key, int enter, int flip) {
            this.row = row;
            this.col = col;
            this.count = count;
            this.key = key;
            this.enter = enter;
            this.flip = flip;
        }
    }
    
    public int solution(int[][] board, int r, int c) {
        int total = 0;
        for (int row=0; row < 4; row++) {
            for (int col=0; col < 4; col++) {
                if (board[row][col] != 0) {
                    int bit = 1 << board[row][col];
                    total |= bit;
                }
            }
        }
        
        ArrayDeque<Node> BFS = new ArrayDeque<>();
        BFS.add(new Node(r, c, 0, 0, -1, 16));
        
        boolean[][][][] check = new boolean[4][4][total + 1][17];
        
        while (!BFS.isEmpty()) {
            Node node = BFS.poll();
            
            if (node.key == total) {
                return node.count;
            }
            
            int nextCount = node.count + 1;
            
            // enter 로직 일괄 구현
            if (board[node.row][node.col] != 0) {
                if ((node.key & (1 << board[node.row][node.col])) == 0) {
                    if ((node.row * 4 + node.col) != node.flip) {
                        if (board[node.row][node.col] == node.enter) {
                            int nextKey = node.key | (1 << board[node.row][node.col]);
                            
                            if (!check[node.row][node.col][nextKey][16]) {
                                check[node.row][node.col][nextKey][16] = true;
                                BFS.add(new Node(node.row, node.col, nextCount, nextKey, -1, 16));
                            }
                        }
                        else {
                            if (node.flip == 16) {
                                if (!check[node.row][node.col][node.key][node.row * 4 + node.col]) {
                                    check[node.row][node.col][node.key][node.row * 4 + node.col] = true;
                                    BFS.add(new Node(node.row, node.col, nextCount, node.key, board[node.row][node.col], node.row * 4 + node.col));
                                }
                            }
                            else {
                                if (!check[node.row][node.col][node.key][16]) {
                                    check[node.row][node.col][node.key][16] = true;
                                    BFS.add(new Node(node.row, node.col, nextCount, node.key, board[node.row][node.col], 16));
                                }
                            }
                        }
                    }
                }
            }
            
            for (int way=0; way < 4; way++) {
                int nr = node.row + dx[way];
                int nc = node.col + dy[way];
                
                if (0 <= nr && nr < 4 && 0 <= nc && nc < 4) {
                    
                    // 한 칸 이동
                    if (!check[nr][nc][node.key][node.flip]) {
                        check[nr][nc][node.key][node.flip] = true;
                        BFS.add(new Node(nr, nc, nextCount, node.key, node.enter, node.flip));
                    }
                    
                    // Ctrl + 이동
                    int nnr = node.row;
                    int nnc = node.col;
                    while (true) {
                        nnr += dx[way];
                        nnc += dy[way];

                        if (0 <= nnr && nnr < 4 && 0 <= nnc && nnc < 4) {
                            if (board[nnr][nnc] != 0) {
                                int bit = 1 << board[nnr][nnc];
                                
                                // 새로운 카드 만났을 때
                                if ((node.key & bit) == 0) {
                                    if (!check[nnr][nnc][node.key][node.flip]) {
                                        check[nnr][nnc][node.key][node.flip] = true;
                                        BFS.add(new Node(nnr, nnc, nextCount, node.key, node.enter, node.flip));
                                    }
                                    
                                    break;
                                }
                            }
                        }
                        
                        // 카드 없이 보드 범위 밖으로 나갔을 때
                        else {
                            nnr -= dx[way];
                            nnc -= dy[way];
                            
                            if (!check[nnr][nnc][node.key][node.flip]) {
                                check[nnr][nnc][node.key][node.flip] = true;
                                BFS.add(new Node(nnr, nnc, nextCount, node.key, node.enter, node.flip));
                            }
                            
                            break;
                        }
                    }
                }
            }
        }
        
        return -1;
    }
}
