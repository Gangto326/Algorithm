import java.io.*;
import java.util.*;

public class BOJ_26146 {
    static int num;
    static int edgeNum;
    static Node[] nodeArray;

    static ArrayDeque<Integer> stack;
    static boolean[] check;

    static int[] groupArray;
    static int groupId;
    

    static class Node {
        ArrayList<Integer> nextNodes;
        ArrayList<Integer> beforeNodes;

        Node() {
            this.nextNodes = new ArrayList<>();
            this.beforeNodes = new ArrayList<>();
        }
    }


    static void DFS(int index) {
        check[index] = true;

        for (int node: nodeArray[index].nextNodes) {
            if (!check[node]) {
                DFS(node);
            }
        }

        stack.add(index);
    }


    static void reversedDFS(int index) {
        groupArray[index] = groupId;

        for (int node: nodeArray[index].beforeNodes) {
            if (groupArray[node] == 0) {
                reversedDFS(node);
            }
        }
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        edgeNum = Integer.parseInt(st.nextToken());

        nodeArray = new Node[num + 1];
        for (int index = 0; index <= num; index++) {
            nodeArray[index] = new Node();
        }

        for (int index = 0; index < edgeNum; index++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            nodeArray[start].nextNodes.add(end);
            nodeArray[end].beforeNodes.add(start);
        }

        stack = new ArrayDeque<>();
        check = new boolean[num + 1];
        for (int index = 1; index <= num; index++) {
            if (!check[index]) {
                DFS(index);
            }
        }

        groupArray = new int[num + 1];
        groupId = 0;

        while (!stack.isEmpty()) {
            int node = stack.pollLast();

            if (groupArray[node] == 0) {
                groupId += 1;
                reversedDFS(node);
            }
        }

        if (groupId == 1) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
