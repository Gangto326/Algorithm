import java.io.*;
import java.util.*;

public class BOJ_11378 {
    static int num;
    static int workNum;
    static int badPoint;

    static People[] peopleArray;
    static int[] workArray;
    static boolean[] check;

    static int answer;


    static class People{
        ArrayList<Integer> workList;

        People() {
            this.workList = new ArrayList<>();
        }
    }


    static void clear() {
        for (int index = 0; index <= num; index ++) {
            check[index] = false;
        }
    }


    static boolean DFS(int index) {
        if (check[index]) {
            return false;
        }

        check[index] = true;

        for (int work: peopleArray[index].workList) {
            if (workArray[work] == 0 || DFS(workArray[work])) {
                workArray[work] = index;
                return true;
            }
        }

        return false;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        num = Integer.parseInt(st.nextToken());
        workNum = Integer.parseInt(st.nextToken());
        badPoint = Integer.parseInt(st.nextToken());

        peopleArray = new People[num + 1];
        for (int index = 0; index <= num; index++) {
            peopleArray[index] = new People();
        }

        for (int index = 1; index <= num; index++) {
            st = new StringTokenizer(br.readLine());
            int count = Integer.parseInt(st.nextToken());

            for (int workIndex = 0; workIndex < count; workIndex++) {
                peopleArray[index].workList.add(Integer.parseInt(st.nextToken()));
            }
        }

        workArray = new int[workNum + 1];
        check = new boolean[num + 1];

        answer = 0;
        for (int index = 1; index <= num; index++) {
            clear();
            if (DFS(index)) {
                answer += 1;
            }
        }

        int nextPoint = badPoint;
        while (badPoint > 0) {
            for (int index = 1; index <= num; index++) {
                clear();

                if (DFS(index)) {
                    answer += 1;
                    nextPoint -= 1;

                    if (nextPoint == 0) {
                        break;
                    }
                }
            }

            if (badPoint == nextPoint) {
                break;
            }
            
            badPoint = nextPoint;
        }

        System.out.println(answer);
    }
}
