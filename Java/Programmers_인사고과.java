import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int wanhoX = scores[0][0]; 
        int wanhoY = scores[0][1];
        int wanhoScore = scores[0][0] + scores[0][1];
        
        Arrays.sort(scores, (o1, o2) -> {
            if (o2[0] == o1[0]) {
                return o1[1] - o2[1];
            }
            
            return o2[0] - o1[0];
        });
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        boolean flag = false;
        
        PriorityQueue<Integer> serviveQueue = new PriorityQueue<Integer>(Collections.reverseOrder());
        
        for (int[] score: scores) {
            if (pq.isEmpty() || pq.peek() <= score[1]) {
                pq.add(score[1]);
                serviveQueue.add(score[0] + score[1]);
                
                if (wanhoX == score[0] && wanhoY == score[1]) {
                    flag = true;
                }
            }
        }
        
        if (!flag) {
            return -1;
        }
        
        int index = 0;
        while (true) {
            index += 1;
            int num = serviveQueue.poll();
            
            if (num == wanhoScore) {
                break;
            }
        }
        
        return index;
    }
}