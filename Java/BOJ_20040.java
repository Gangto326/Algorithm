import java.io.*;
import java.util.*;

public class BOJ_20040 {
    static int num;
    static int queryNum;
    static int[] parents;
    static int answer;


    static int find(int index) {
        if (index == parents[index]) {
            return index;
        }

        return parents[index] = find(parents[index]);
    }


    static boolean union(int first, int sec) {
        int firstParents = find(first);
        int secParents = find(sec);

        if (firstParents == secParents) {
            return false;
        }

        parents[firstParents] = secParents;
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        num = Integer.parseInt(st.nextToken());
        queryNum = Integer.parseInt(st.nextToken());
        parents = new int[num + 1];

        for (int index = 1; index <= num; index++) {
            parents[index] = index;
        }

        answer = 0;
        for (int query = 1; query <= queryNum; query++) {
            st = new StringTokenizer(br.readLine().trim());

            if (!union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()))) {
                answer = query;
                break;
            }
        }

        System.out.println(answer);
    }
}
