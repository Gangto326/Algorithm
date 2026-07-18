import java.io.*;
import java.util.*;

public class Main {
    static int t;
    static int aNum;
    static int[] aArray;
    static HashMap<Integer, Integer> aMap;

    static int bNum;
    static int[] bArray;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        t = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        aNum = Integer.parseInt(st.nextToken());
        aArray = new int[aNum];
        aMap = new HashMap<Integer, Integer>();

        st = new StringTokenizer(br.readLine());
        for (int index=0; index < aNum; index++) {
            aArray[index] = Integer.parseInt(st.nextToken());
        }

        for (int first=0; first < aNum; first++) {
            int total = 0;

            for (int sec=first; sec < aNum; sec++) {
                total += aArray[sec];
                aMap.put(total, aMap.getOrDefault(total, 0) + 1);
            }
        }

        st = new StringTokenizer(br.readLine());
        bNum = Integer.parseInt(st.nextToken());
        bArray = new int[bNum];

        st = new StringTokenizer(br.readLine());
        for (int index=0; index < bNum; index++) {
            bArray[index] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for (int first=0; first < bNum; first++) {
            int total = 0;

            for (int sec=first; sec < bNum; sec++) {
                total += bArray[sec];
                
                if (total > t) {
                    break;
                }

                if (aMap.containsKey(t - total)) {
                    answer += aMap.get(t - total);
                }
            }
        }

        System.out.println(answer);
    }
}
