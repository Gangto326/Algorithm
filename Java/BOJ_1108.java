import java.io.*;
import java.util.*;

public class BOJ_1108 {
    static int num;
    static ArrayList<Edge> edgeList;

    static ArrayList<String> nodeList;
    static HashMap<String, ArrayList<String>> nodeMap;
    static HashMap<String, ArrayList<String>> reversedNodeMap;
    static String target;
    
    static ArrayDeque<String> stack;
    static HashSet<String> check;

    static HashMap<String, Integer> groupMap;
    static int groupId;

    static HashMap<String, Long> DP;


    static class Edge {
        int start, end;

        Edge(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }


    static void DFS(String index) {
        check.add(index);

        if (!nodeMap.containsKey(index)) {
            return;
        }

        for (String nextNode: nodeMap.get(index)) {
            if (!check.contains(nextNode)) {
                DFS(nextNode);
            }
        }

        stack.add(index);
    }


    static void reversedDFS(String index) {
        groupMap.put(index, groupId);

        if (!reversedNodeMap.containsKey(index)) {
            return;
        }

        for (String nextNode: reversedNodeMap.get(index)) {
            if (!groupMap.containsKey(nextNode)) {
                reversedDFS(nextNode);
            }
        }
    }


    static long getScore(String index) {
        if (DP.containsKey(index)) {
            return DP.get(index);
        }

        long score = 1L;

        if (reversedNodeMap.containsKey(index)) {
            for (String beforeNode: reversedNodeMap.get(index)) {
                if (!groupMap.get(index).equals(groupMap.get(beforeNode))) {
                    score += getScore(beforeNode);
                }
            }
        }
        
        DP.put(index, score);
        return score;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        num = Integer.parseInt(st.nextToken());

        nodeList = new ArrayList<>();
        nodeMap = new HashMap<>();
        reversedNodeMap = new HashMap<>();

        for (int index = 0; index < num; index ++) {
            st = new StringTokenizer(br.readLine());

            String node = st.nextToken();
            nodeList.add(node);

            int beforeNum = Integer.parseInt(st.nextToken());

            if (!reversedNodeMap.containsKey(node)) {
                reversedNodeMap.put(node, new ArrayList<>());
            }

            for (int beforeIndex = 0; beforeIndex < beforeNum; beforeIndex ++) {
                String beforeNode = st.nextToken();

                if (!nodeMap.containsKey(beforeNode)) {
                    nodeMap.put(beforeNode, new ArrayList<>());
                }

                reversedNodeMap.get(node).add(beforeNode);
                nodeMap.get(beforeNode).add(node);
            }
        }

        for (String node: nodeList) {
            if (!nodeMap.containsKey(node)) {
                nodeMap.put(node, new ArrayList<>());
            }

            if (!reversedNodeMap.containsKey(node)) {
                reversedNodeMap.put(node, new ArrayList<>());
            }
        }

        st = new StringTokenizer(br.readLine());
        target = st.nextToken();   

        stack = new ArrayDeque<>();
        check = new HashSet<>();

        for (String key: nodeMap.keySet()) {
            if (!check.contains(key)) {
                DFS(key);
            }
        }

        groupMap = new HashMap<>();
        groupId = 0;

        while (!stack.isEmpty()) {
            String node = stack.pollLast();

            if (!groupMap.containsKey(node)) {
                groupId += 1;
                reversedDFS(node);
            }
        }
        
        DP = new HashMap<>();
        System.out.println(getScore(target));
    }
}
