class Solution
{
    static int num;
    static boolean[][] DP;
    static int answer;
    
    public int solution(String s)
    {
        num = s.length();
        answer = 1;
        DP = new boolean[num][num];
        
        for (int index = 0; index < num; index++) {
            DP[index][index] = true;
        }
        
        for (int index = 0, end = num - 1; index < end; index++) {
            if (s.charAt(index) == s.charAt(index + 1)) {
                DP[index][index + 1] = true;
                answer = 2;
            }
        }
        
        for (int palLenght = 3; palLenght <= num; palLenght++) {
            for (int index = 0, end = num - palLenght; index <= end; index++) {
                int beforeIndex = index + palLenght - 1;
                
                if ((s.charAt(index) == s.charAt(beforeIndex)) && DP[index + 1][beforeIndex - 1]) {
                    DP[index][beforeIndex] = true;
                    answer = palLenght;
                }
            }
        }

        return answer;
    }
}