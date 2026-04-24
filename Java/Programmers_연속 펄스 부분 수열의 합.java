class Solution {
    static int num;
    static long total;
    
    public long solution(int[] sequence) {
        num = sequence.length;
        
        long answer = 0;
        total = 0;
        
        for (int i = 0; i < num; i++) {
            if (i % 2 == 0) {
                total += sequence[i];
            }
            else {
                total -= sequence[i];
            }
            
            if (total < 0) {
                total = 0;
            }
            
            answer = Math.max(answer, total);
        }
        
        total = 0;
        for (int i = 0; i < num; i++) {
            if (i % 2 != 0) {
                total += sequence[i];
            }
            else {
                total -= sequence[i];
            }
            
            if (total < 0) {
                total = 0;
            }
            
            answer = Math.max(answer, total);
        }
        
        
        return answer;
    }
}