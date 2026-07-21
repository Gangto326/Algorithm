import java.io.*;
import java.util.*;

public class Jungol_1676 {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int num;
    static Node[] nodeArray;

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int caculate(Point o) {
            return Math.abs(this.x - o.x) + Math.abs(this.y - o.y);
        }
    }

    static class Node {
        int index;
        ArrayList<Point> pointList;

        Node(int index) {
            this.index = index;
            this.pointList = new ArrayList<Point>();
        }
    }

    static int DFS(int index, ArrayList<Point> pointList, int total) {
        if (index > num) {
            return total;
        }

        ArrayList<Point> nextPoints = new ArrayList<Point>();
        boolean[] check = new boolean[nodeArray[index].pointList.size()];

        int minNum = Integer.MAX_VALUE;

        for (int pointIndex=0, end=nodeArray[index].pointList.size(); pointIndex < end; pointIndex++) {
            Point point = nodeArray[index].pointList.get(pointIndex);

            for (Point prev: pointList) {
                int length = point.caculate(prev);

                if (minNum > length) {
                    minNum = length;
                    Arrays.fill(check, false);
                    check[pointIndex] = true;
                }

                else if (minNum == length) {
                    check[pointIndex] = true;
                }
            }
        }

        for (int pointIndex=0, end=nodeArray[index].pointList.size(); pointIndex < end; pointIndex++) {
            if (check[pointIndex]) {
                nextPoints.add(nodeArray[index].pointList.get(pointIndex));
            }
        }

        return DFS(index + 1, nextPoints, total + minNum);
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        nodeArray = new Node[num + 1];
        for (int index=0; index <= num; index++) {
            nodeArray[index] = new Node(index);
        }

        for (int index=0; index <= num; index++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            
            nodeArray[index].pointList.add(new Point(x, y));

            if (index == 0) {
                continue;
            }

            for (int way=0; way < 4; way++) {
                int nx = x + dx[way];
                int ny = y + dy[way];

                nodeArray[index].pointList.add(new Point(nx, ny));
            }
        }

        System.out.println(DFS(0, nodeArray[0].pointList, 0));
    }
}
