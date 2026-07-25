import java.util.*;

class Solution {
    static ArrayList<int[]> combList;
    
    public static void comb(int weakNum, int index, int[] combArray, int count, int target) {
        if (target == count) {
            int[] result = new int[target];
            
            for (int numIndex=0; numIndex < target; numIndex++) {
                result[numIndex] = combArray[numIndex];
            }
            combList.add(result);
            return;
        }
        
        if (index >= weakNum) {
            return;
        }
        
        for (int numIndex=index, end=weakNum; numIndex < end; numIndex++) {
            combArray[count] = numIndex;
            comb(weakNum, numIndex+1, combArray, count+1, target);
        }
    }
    
    public int solution(int n, int[] weak, int[] dist) {
        int weakNum = weak.length;
        int distNum = dist.length;
        
        Arrays.sort(dist);
        
        combList = new ArrayList<>();
        for (int count=1; count <= distNum; count++) {
            combList.clear();
            comb(weakNum, 0, new int[count], 0, count);
            
            for (int[] combArray: combList) {
                PriorityQueue<Integer> lengthQueue = new PriorityQueue<>();
                
                for (int index=0; index < count-1; index++) {
                    lengthQueue.add(-(weak[combArray[index + 1] - 1] - weak[combArray[index]]));
                }
                
                int lastCheck = combArray[0] != 0? combArray[0]-1: weakNum-1;
                
                if (lastCheck != combArray[count-1]) {
                    if (lastCheck < combArray[count-1]) {
                        lengthQueue.add(-((n - weak[combArray[count-1]]) + weak[lastCheck]));
                    }
                    else {
                        lengthQueue.add(-(weak[lastCheck] - weak[combArray[count-1]]));
                    }
                }
                
                int distIndex = distNum - 1;
                while (!lengthQueue.isEmpty()) {
                    int num = -lengthQueue.poll();
                    
                    if (dist[distIndex] >= num) {
                        distIndex -= 1;
                    }
                    else {
                        lengthQueue.add(num);
                        break;
                    }
                }
                
                if (lengthQueue.isEmpty()) {
                    return count;
                }
            }
        }
        
        return -1;
    }
}