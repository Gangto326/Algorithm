import java.io.*;
import java.util.*;

public class Jungol_1519 {
    static int N;
    static int M;
    static int K;

    static ArrayList<Node> nodeList;
    static int[] tree;
    static long answer;

    static class Node implements Comparable<Node>{
        int start, end;

        Node(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Node o) {
            if (this.start > o.start) {
                return 1;
            }

            else if (this.start < o.start) {
                return -1;
            }

            else {
                return Integer.compare(this.end, o.end);
            }
        }
    }

    static void update(int index, int left, int right, int target) {
        tree[index] += 1;
        if (left == right) {
            return;
        }

        int mid = (left + right) / 2;
        if ((target >= left) && (target <= mid)) {
            update(index * 2, left, mid, target);
        }
        else if ((target <= right) && (target > mid)) {
            update(index * 2 + 1, mid + 1, right, target);
        }
    }

    static int excuteQuery(int index, int left, int right, int start, int end) {
        if (left > end || right < start) {
            return 0;
        }

        else if (start <= left && end >= right) {
            return tree[index];
        }

        int mid = (left + right) / 2;
        int leftCount = excuteQuery(index * 2, left, mid, start, end);
        int rightCount = excuteQuery(index * 2 + 1, mid + 1, right, start, end);

        return leftCount + rightCount;
    }

    public static void main (String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        nodeList = new ArrayList<Node>();
        for (int query=0; query < K; query++) {
            st = new StringTokenizer(br.readLine());
            nodeList.add(new Node(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        Collections.sort(nodeList);
        tree = new int[M * 4];
        answer = 0L;

        for (Node node: nodeList) {
            if (node.end != M) {
                answer += excuteQuery(1, 1, M, node.end + 1, M);
            }
            update(1, 1, M, node.end);
        }

        System.out.println(answer);
    }
}
