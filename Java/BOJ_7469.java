import java.io.*;
import java.util.*;


public class BOJ_7469 {
    static int num;
    static int queryNum;

    static int[] numArray;
    static Node[] tree;

    static int min_value;
    static int max_value;


    static class Node {
        ArrayList<Integer> nodeList;

        Node() {
            this.nodeList = new ArrayList<>();
        }
    }


    static int binarySearch(Node node, int target) {
        int left = 0;
        int right = node.nodeList.size();

        while (left < right) {
            int mid = (left + right) / 2;

            if (node.nodeList.get(mid) <= target) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }

        return left;
    }


    static Node makeTree(int index, int start, int end) {

        if (start == end) {
            tree[index].nodeList.add(numArray[start]);
            return tree[index];
        }

        int mid = (start + end) / 2;
        ArrayList<Integer> leftArray = makeTree(index * 2, start, mid).nodeList;
        ArrayList<Integer> rightArray = makeTree(index * 2 + 1, mid + 1, end).nodeList;

        int leftIndex = 0;
        int rightIndex = 0;

        int leftLen = leftArray.size();
        int rightLen = rightArray.size();

        while (leftIndex < leftLen && rightIndex < rightLen) {
            if (leftArray.get(leftIndex) > rightArray.get(rightIndex)) {
                tree[index].nodeList.add(rightArray.get(rightIndex));
                rightIndex += 1;
            }

            else {
                tree[index].nodeList.add(leftArray.get(leftIndex));
                leftIndex += 1;
            }
        }

        for (int i = leftIndex; i < leftLen; i++) {
            tree[index].nodeList.add(leftArray.get(i));
        }

        for (int i = rightIndex; i < rightLen; i++) {
            tree[index].nodeList.add(rightArray.get(i));
        }

        return tree[index];
    }


    static int exquteQuery(int index, int start, int end, int left, int right, int target) {
        if (start > right || end < left) {
            return 0;
        }

        if (start >= left && right >= end) {
            return binarySearch(tree[index], target);
        }

        int mid = (start + end) / 2;
        int targetCount = exquteQuery(index * 2, start, mid, left, right, target) + exquteQuery(index * 2 + 1, mid + 1, end, left, right, target);
        return targetCount;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder answer = new StringBuilder();

        num = Integer.parseInt(st.nextToken());
        queryNum = Integer.parseInt(st.nextToken());
        min_value = Integer.MAX_VALUE;
        max_value = Integer.MIN_VALUE;

        numArray = new int[num];
        st = new StringTokenizer(br.readLine());
        for (int index = 0; index < num; index++) {
            numArray[index] = Integer.parseInt(st.nextToken());
            min_value = Math.min(min_value, numArray[index]);
            max_value = Math.max(max_value, numArray[index]);
        }

        tree = new Node[num * 4];
        for (int index = 0, end = num * 4; index < end; index++) {
            tree[index] = new Node();
        }

        makeTree(1, 0, num - 1);

        for (int query = 0; query < queryNum; query++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()) - 1;
            int end = Integer.parseInt(st.nextToken()) - 1;
            int target = Integer.parseInt(st.nextToken());

            int left = min_value;
            int right = max_value;

            while (left < right) {
                int mid = (left + right) >> 1;
                int count = exquteQuery(1, 0, num - 1, start, end, mid);

                if (count < target) {
                    left = mid + 1;
                }
                else {
                    right = mid;
                }
            }

            answer.append(left).append("\n");
        }
        
        System.out.println(answer);
    }
}
