import java.io.*;
import java.util.*;

public class BOJ_1298 {
    static int personNum;
    static int notebookCount;

    static int[] notebookArray;
    static boolean[] checkArray;
    static People[] peopleArray;

    static int answer;

    static class People {
        ArrayList<Integer> wanted;

        People() {
            wanted = new ArrayList<>();
        }
    }


    static boolean DFS(int index) {
        if (checkArray[index]) {
            return false;
        }

        checkArray[index] = true;

        for (int notebook: peopleArray[index].wanted) {
            if (notebookArray[notebook] == 0 || DFS(notebookArray[notebook])) {
                notebookArray[notebook] = index;
                return true;
            }
        }

        return false;
    }


    static void checkClear() {
        for (int index = 0; index <= personNum; index++) {
            checkArray[index] = false;
        }
    }


    public static void main(String[] arg) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        personNum = Integer.parseInt(st.nextToken());
        notebookCount = Integer.parseInt(st.nextToken());

        notebookArray = new int[personNum + 1];
        checkArray = new boolean[personNum + 1];
        peopleArray = new People[personNum + 1];

        answer = 0;

        for (int index = 0; index <= personNum; index++) {
            peopleArray[index] = new People();
        }

        for (int queryNum = 0; queryNum < notebookCount; queryNum++) {
            st = new StringTokenizer(br.readLine());
            peopleArray[Integer.parseInt(st.nextToken())].wanted.add(Integer.parseInt(st.nextToken()));
        }

        for (int index = 1; index <= personNum; index++) {
            checkClear();

            if (DFS(index)) {
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}
