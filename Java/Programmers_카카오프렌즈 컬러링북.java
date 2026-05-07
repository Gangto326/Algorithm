import java.util.*;

class Solution {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};
    
    
    static class Pos {
        int row, col;
        
        Pos(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        boolean[][] check = new boolean[m][n];
        
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (picture[row][col] != 0 && !check[row][col]) {
                    numberOfArea += 1;
                    
                    ArrayDeque<Pos> BFS = new ArrayDeque<Pos>();
                    BFS.add(new Pos(row, col));
                    check[row][col] = true;
                    
                    int sizeArea = 1;
                    int color = picture[row][col];
                    
                    while (!BFS.isEmpty()) {
                        Pos pos = BFS.pollFirst();
                        
                        for (int way = 0; way < 4; way++) {
                            int nr = pos.row + dx[way];
                            int nc = pos.col + dy[way];
                            
                            if (nr < 0 || nc < 0 || nr >= m || nc >= n) {
                                continue;
                            }
                            
                            if (picture[nr][nc] == color && !check[nr][nc]) {
                                BFS.add(new Pos(nr, nc));
                                check[nr][nc] = true;
                                sizeArea += 1;
                            }
                        }
                    }
                    
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, sizeArea);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}