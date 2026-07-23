import java.io.*;
import java.util.*;

public class Jungol_1863 {
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

        if (firstParent != secParent) {
            parents[secParent] = firstParent;
        }

        return;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        queryNum = Integer.parseInt(st.nextToken());
        parents = new int[num+1];
        for (int index=0; index <= num; index++) {
            parents[index] = index;
        }

        for (int query=0; query < queryNum; query++) {
            st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int sec = Integer.parseInt(st.nextToken());

            if (first < sec) {
                union(first, sec);
            }
            else {
                union(sec, first);
            }
        }

        boolean[] check = new boolean[num+1];
        int answer = 0;
        for (int index=1; index <= num; index++) {
            int root = find(index);

            if (!check[root]) {
                check[root] = true;
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}
