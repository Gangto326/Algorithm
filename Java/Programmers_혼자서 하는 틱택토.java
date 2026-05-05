import java.util.*;

class Solution {
    static int oCount;
    static int xCount;
    static ArrayList<Point> oList;
    static ArrayList<Point> xList;
    static int answer;
    static char[][] check;
    
    static class Point {
        int row, col;
        
        Point(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
    
    
    static boolean checkFinish() {
        for (int row = 0; row < 3; row++) {
            boolean flag = true;
            
            if (check[row][0] == '.') {
                continue;
            }
            
            for (int col = 0; col < 3; col++) {
                if (check[row][0] != check[row][col]) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                return true;
            }
        }
        
        for (int col = 0; col < 3; col++) {
            boolean flag = true;
            
            if (check[0][col] == '.') {
                continue;
            }
            
            for (int row = 0; row < 3; row++) {
                if (check[0][col] != check[row][col]) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                return true;
            }
        }
        
        if (check[0][0] != '.') {
            boolean flag = true;
            
            for (int index = 0; index < 3; index++) {
                if (check[index][index] != check[0][0]) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                return true;
            }
        }
        
        if (check[0][2] != '.') {
            if (check[1][1] == check[0][2] && check[2][0] == check[0][2]) {
                return true;
            }
        }
        
        return false;
    }
        
    
    static void DFS(int oCount, int xCount, boolean turn) {
        if (oCount == 0 && xCount == 0) {
            answer = 1;
            return;
        }
        
        if (checkFinish()) {
            return;
        }
        
        if (answer == 1) {
            return;
        }
        
        if (turn) {
            for (Point o: oList) {
                if (check[o.row][o.col] == '.') {
                    check[o.row][o.col] = 'O';
                    DFS(oCount - 1, xCount, false);
                    check[o.row][o.col] = '.';
                }
            }
        }
        else {
            for (Point o: xList) {
                if (check[o.row][o.col] == '.') {
                    check[o.row][o.col] = 'X';
                    DFS(oCount, xCount - 1, true);
                    check[o.row][o.col] = '.';
                }
            }
        }
    }
    
    
    public int solution(String[] board) {
        oCount = 0;
        xCount = 0;
        oList = new ArrayList<Point>();
        xList = new ArrayList<Point>();
        answer = 0;
        check = new char[3][3];
        
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                check[row][col] = '.';
                
                if (board[row].charAt(col) == 'O') {
                    oCount += 1;
                    oList.add(new Point(row, col));
                }
                
                if (board[row].charAt(col) == 'X') {
                    xCount += 1;
                    xList.add(new Point(row, col));
                }
            }
        }
        
        if (Math.abs(oCount - xCount) >= 2) {
            return 0;
        }
        
        DFS(oCount, xCount, true);
        return answer;
    }
}