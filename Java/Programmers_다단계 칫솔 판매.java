import java.util.*;

class Solution {
    static int num;
    static int[] answer;
    static HashMap<String, Integer> indexMap;
    static int[] parents;
    
    
    static void DFS(int index, int cost) {
        if (index == -1) {
            return;
        }
        
        if (cost == 0) {
            return;
        }
        
        int up = (int) (cost * 0.1);
        
        answer[index] += cost - up;
        DFS(parents[index], up);
    }
    
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        num = enroll.length;
        answer = new int[num];
        indexMap = new HashMap<String, Integer>();
        parents = new int[num];
        Arrays.fill(parents, -1);
        
        for (int i = 0; i < num; i++) {
            indexMap.put(enroll[i], i);
        }
        
        for (int i = 0; i < num; i++) {
            if (referral[i].equals("-")) {
                continue;
            }
            
            parents[i] = indexMap.get(referral[i]);
        }
        
        int queryNum = seller.length;
        for (int query = 0; query < queryNum; query++) {
            DFS(indexMap.get(seller[query]), amount[query] * 100);
        }
        
        return answer;
    }
}