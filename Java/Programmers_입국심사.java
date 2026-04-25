class Solution {
    static final long MAX_VALUE = 1_000_000_000;
    static long num;
    static long answer;
    
    
    static void binary_search(int[] times, long target) {
        long left = 0;
        long right = num;
        
        while (left < right) {
            long mid = (left + right) / 2;
            
            long count = 0;
            
            for (int time: times) {
                count += mid / (long) time;
            }
            
            if (count < target) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        
        answer = left;
        return;
    }
    
    
    public long solution(int n, int[] times) {
        num = MAX_VALUE * (long) n;
        binary_search(times, (long) n);
        return answer;
    }
}