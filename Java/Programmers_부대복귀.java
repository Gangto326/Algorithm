import java.util.*;

class Solution {
    static final int MAX_VALUE = 1_000_000;
    static Node[] nodeArray;
    static int[] answer;
    
    
    static class Node {
        ArrayList<Integer> nextNodeList;
        
        Node() {
            nextNodeList = new ArrayList<Integer>();
        }
    }
    
    
    static class BFSNode {
        int index, count;
        
        BFSNode(int index, int count) {
            this.index = index;
            this.count = count;
        }
    }
    
    
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        nodeArray = new Node[n + 1];
        answer = new int[sources.length];
        
        for (int index = 0; index <= n; index ++) {
            nodeArray[index] = new Node();
        }
        
        for (int[] road: roads) {
            nodeArray[road[0]].nextNodeList.add(road[1]);
            nodeArray[road[1]].nextNodeList.add(road[0]);
        }
        
        ArrayDeque<BFSNode> BFS = new ArrayDeque<BFSNode>();
        BFS.add(new BFSNode(destination, 0));
        
        int[] check = new int[n + 1];
        Arrays.fill(check, MAX_VALUE);
        check[destination] = 0;
        
        while (!BFS.isEmpty()) {
            BFSNode node = BFS.pollFirst();
            
            int nextCount = node.count + 1;
            for (int nextNode: nodeArray[node.index].nextNodeList) {
                if (check[nextNode] > nextCount) {
                    check[nextNode] = nextCount;
                    BFS.add(new BFSNode(nextNode, nextCount));
                }
            }
        }
        
        for (int index = 0, end = sources.length; index < end; index++) {
            int query = sources[index];
            
            if (check[query] == MAX_VALUE) {
                answer[index] = -1;
            }
            else {
                answer[index] = check[query];
            }
        }
        
        return answer;
    }
}