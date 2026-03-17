import java.io.*;
import java.util.*;

public class BOJ_15783 {
    static int num;
    static int queryNum;
    static Node[] nodeArray;
    static ArrayList<Edge> edgeList;

    static ArrayDeque<Integer> stack;
    static boolean[] check;

    static int[] groups;
    static int groupId;

    static TopolNode[] groupNodes;
    static int answer;

    static void DFS(int index) {
        check[index] = true;

        for (int node: nodeArray[index].nextNode) {
            if (!check[node]) {
                DFS(node);
            }
        }

        stack.add(index);
    }


    static void reversed_DFS(int index) {
        groups[index] = groupId;

        for (int node: nodeArray[index].beforeNode) {
            if (groups[node] == 0) {
                reversed_DFS(node);
            }
        }
    }


    static class Node {
        ArrayList<Integer> nextNode;
        ArrayList<Integer> beforeNode;

        Node() {
            this.nextNode = new ArrayList<>();
            this.beforeNode = new ArrayList<>();
        }
    }


    static class Edge {
        int start, end;

        Edge(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }


    static class TopolNode {
        int indegree;
        ArrayList<Integer> next_groups;

        TopolNode() {
            this.indegree = 0;
            this.next_groups = new ArrayList<>();
        }
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        queryNum = Integer.parseInt(st.nextToken());
        nodeArray = new Node[num + 1];
        edgeList = new ArrayList<>();

        for (int index = 0; index <= num; index++) {
            nodeArray[index] = new Node();
        }

        for (int query = 0; query < queryNum; query++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken()) + 1;
            int end = Integer.parseInt(st.nextToken()) + 1;

            nodeArray[start].nextNode.add(end);
            nodeArray[end].beforeNode.add(start);
            edgeList.add(new Edge(start, end));
        }

        stack = new ArrayDeque<>();
        check = new boolean[num + 1];

        for (int index = 1; index <= num; index++) {
            if (!check[index]) {
                DFS(index);
            }
        }

        groups = new int[num + 1];
        groupId = 0;

        while (!stack.isEmpty()) {
            int node = stack.pollLast();

            if (groups[node] == 0) {
                groupId += 1;
                reversed_DFS(node);
            }
        }

        groupNodes = new TopolNode[groupId + 1];
        for (int index = 0; index <= groupId; index++) {
            groupNodes[index] = new TopolNode();
        }

        for (Edge edge: edgeList) {
            if (groups[edge.start] != groups[edge.end]) {
                groupNodes[groups[edge.start]].next_groups.add(groups[edge.end]);
                groupNodes[groups[edge.end]].indegree += 1;
            }
        }

        answer = 0;
        for (int index = 1; index <= groupId; index++) {
            if (groupNodes[index].indegree == 0) {
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}
