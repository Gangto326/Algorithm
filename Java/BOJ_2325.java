import java.io.*;
import java.util.*;

public class BOJ_2325 {
    static int num;
    static int edgeNum;
    static Node[] nodeArray;

    static PriorityQueue<DijkNode> dijkstra;
    static int[] check;
    static int[] parents;
    
    static ArrayList<MinEdge> MinEdgeList;
    static int answer;


    static class Node {
        ArrayList<Edge> edgeList;

        Node() {
            this.edgeList = new ArrayList<>();
        }
    }


    static class Edge {
        int end, cost;

        Edge(int end, int cost) {
            this.end = end;
            this.cost = cost;
        }
    }


    static class MinEdge {
        int start, end;

        MinEdge(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }


    static class DijkNode implements Comparable<DijkNode>{
        int start, total;

        DijkNode(int start, int total) {
            this.start = start;
            this.total = total;
        }

        @Override
        public int compareTo(DijkNode o) {
            if (this.total > o.total) {
                return 1;
            }

            else {
                return -1;
            }
        }
    }


    static int Dijkstra(int start, int end) {
        dijkstra = new PriorityQueue<>();
        check = new int[num + 1];

        Arrays.fill(check, Integer.MAX_VALUE);
        check[1] = 0;
        dijkstra.add(new DijkNode(1, 0));

        while (!dijkstra.isEmpty()) {
            DijkNode dijkNode = dijkstra.poll();

            if (check[dijkNode.start] < dijkNode.total) {
                continue;
            }

            if (dijkNode.total > check[num]) {
                break;
            }

            for (Edge edge: nodeArray[dijkNode.start].edgeList) {
                if ((dijkNode.start == start && edge.end == end) || (dijkNode.start == end && edge.end == start)) {
                    continue;
                }

                int nextTotal = dijkNode.total + edge.cost;

                if (check[edge.end] <= nextTotal) {
                    continue;
                }

                check[edge.end] = nextTotal;
                parents[edge.end] = dijkNode.start;

                if (edge.end != num) {
                    dijkstra.add(new DijkNode(edge.end, nextTotal));
                }
            }
        }

        return check[num];
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

        for (int edgeIndex=0; edgeIndex < edgeNum; edgeIndex++) {
            st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int sec = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            nodeArray[first].edgeList.add(new Edge(sec, cost));
            nodeArray[sec].edgeList.add(new Edge(first, cost));
        }

        parents = new int[num + 1];
        MinEdgeList = new ArrayList<>();
        Dijkstra(0, 0);

        int index = num;
        while (index != 1) {
            MinEdgeList.add(new MinEdge(parents[index], index));
            index = parents[index];
        }

        answer = 0;
        for (MinEdge minEdge: MinEdgeList) {
            answer = Math.max(answer, Dijkstra(minEdge.start, minEdge.end));
        }

        System.out.println(answer);
    }
}
