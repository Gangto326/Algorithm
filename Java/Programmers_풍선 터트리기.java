class Solution {
    public int solution(int[] a) {
        int num = a.length;
        int answer = 0;
        
        int[][] numArray = new int[num][2];
        numArray[0][0] = a[0];
        
        for (int index = 1; index < num; index++) {
            if (a[index] > numArray[index-1][0]) {
                numArray[index][0] = numArray[index-1][0];
            }
            else {
                numArray[index][0] = a[index];
            }
        }
        
        numArray[num-1][1] = a[num-1];
        
        for (int index = num-2; index >= 0; index--) {
            if (a[index] > numArray[index+1][1]) {
                numArray[index][1] = numArray[index+1][1];
            }
            else {
                numArray[index][1] = a[index];
            }
        }
        
        for (int index = 0; index < num; index++) {
            if (numArray[index][0] == a[index] || numArray[index][1] == a[index]) {
                answer += 1;
            }
        }
        
        return answer;
    }
}