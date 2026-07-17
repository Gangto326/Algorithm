import java.io.*;
import java.util.*;

public class Jungol_1544 {
    static final int MAX_NUM = 100;
    static int num;
    static int[][] floid;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        floid = new int[num + 1][num + 1];
        for (int index=0; index <= num; index++) {
            Arrays.fill(floid[index], MAX_NUM);
            floid[index][index] = 0;
        }

        while (true) {
            st = new StringTokenizer(br.readLine());
            int friendA = Integer.parseInt(st.nextToken());
            int friendB = Integer.parseInt(st.nextToken());

            if (friendA == -1) {
                break;
            }

            floid[friendA][friendB] = 1;
            floid[friendB][friendA] = 1;
        }

        for (int k=1; k <= num; k++) {
            for (int i=1; i <= num; i++) {
                if (floid[i][k] == MAX_NUM) {
                    continue;
                }

                for (int j=1; j <= num; j++) {
                    floid[i][j] = Math.min(floid[i][j], floid[i][k] + floid[k][j]);
                }
            }
        }

        ArrayList<Integer> answerList = new ArrayList<Integer>();
        int minCount = MAX_NUM;

        for (int index=1; index <= num; index++) {
            int maxCount = 0;

            for (int friendIndex=1; friendIndex <= num; friendIndex++) {
                maxCount = Math.max(maxCount, floid[index][friendIndex]);

                if (maxCount > minCount) {
                    break;
                }
            }

            if (maxCount < minCount) {
                minCount = maxCount;
                answerList = new ArrayList<Integer>();
                answerList.add(index);
            }

            else if (maxCount == minCount) {
                answerList.add(index);
            }
        }

        StringBuilder answer = new StringBuilder();
        answer.append(minCount + " " + answerList.size()).append("\n");
        for (int index: answerList) {
            answer.append(index).append(" ");
        }

        System.out.println(answer);
    }
}
