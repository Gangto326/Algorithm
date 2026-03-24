import java.io.*;
import java.util.*;

public class BOJ_1717 {
    static int num;
    static int queryNum;
    static int[] parents;


    static int find(int index) {
        if (parents[index] == index) {
            return index;
        }

        return parents[index] = find(parents[index]);
    }


    static void union(int first, int sec) {
        int firstParent = find(first);
        int secParent = find(sec);

        parents[firstParent] = secParent;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder answer = new StringBuilder();

        num = Integer.parseInt(st.nextToken());
        queryNum = Integer.parseInt(st.nextToken());
        parents = new int[num + 1];

        for (int index=0; index <= num ; index++) {
            parents[index] = index;
        }

        for (int index=0; index < queryNum; index++) {
            st = new StringTokenizer(br.readLine());

            int query = Integer.parseInt(st.nextToken());

            if (query == 0) {
                union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            else {
                int firstParent = find(Integer.parseInt(st.nextToken()));
                int secParent = find(Integer.parseInt(st.nextToken()));

                if (firstParent == secParent) {
                    answer.append("YES").append("\n");
                }
                else {
                    answer.append("NO").append("\n");
                }
            }
        }

        System.out.println(answer);
    }
}
