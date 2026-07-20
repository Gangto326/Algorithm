import java.io.*;
import java.util.*;

public class Jungol_1659 {
    static int num;
    static int edgeNum;

    static Node[] nodeArray;
    static int[] costArray;
    static int[] beforeArray;

    static class Edge {
        int end, cost;

        Edge(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }
    }

    static class Node {
        int index, indegree;
        ArrayList<Edge> edgeList;

        Node(int index) {
            this.index = index;
            this.indegree = 0;
            this.edgeList = new ArrayList<>();
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        num = Integer.parseInt(br.readLine().trim());
        edgeNum = Integer.parseInt(br.readLine().trim());
        nodeArray = new Node[num + 1];

        for (int index=0; index <= num; index++) {
            nodeArray[index] = new Node(index);
        }

        for (int index=0; index < edgeNum; index++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            nodeArray[end].indegree += 1;
            nodeArray[start].edgeList.add(new Edge(end, cost));
        }

        costArray = new int[num + 1];
        beforeArray = new int[num + 1];
        
        ArrayDeque<Node> BFS = new ArrayDeque<>();
        for (Edge edge: nodeArray[1].edgeList) {
            nodeArray[edge.end].indegree -= 1;

            if (costArray[edge.end] < edge.cost) {
                costArray[edge.end] = edge.cost;
                beforeArray[edge.end] = 1;
            }
            
            if (nodeArray[edge.end].indegree == 0) {
                BFS.add(nodeArray[edge.end]);
            }
        }
        nodeArray[1] = new Node(1);

        while (!BFS.isEmpty()) {
            Node node = BFS.poll();

            for (Edge edge: node.edgeList) {
                nodeArray[edge.end].indegree -= 1;
                int nextCost = costArray[node.index] + edge.cost;

                if (costArray[edge.end] < nextCost) {
                    costArray[edge.end] = nextCost;
                    beforeArray[edge.end] = node.index;
                }
                
                if (nodeArray[edge.end].indegree == 0) {
                    BFS.add(nodeArray[edge.end]);
                }
            }
        }

        System.out.println(costArray[1]);

        ArrayList<Integer> pathList = new ArrayList<>();
        pathList.add(1);
        int startIndex = beforeArray[1];
        while (startIndex != 1) {
            pathList.add(startIndex);
            startIndex = beforeArray[startIndex];
        }
        pathList.add(1);
        Collections.reverse(pathList);

        StringBuilder answer = new StringBuilder();
        for (int index=0; index < pathList.size(); index++) {
            if (index > 0) answer.append(' ');
            answer.append(pathList.get(index));
        }
        
        System.out.println(answer);
    }
}
