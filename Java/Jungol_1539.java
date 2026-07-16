import java.io.*;
import java.util.*;

public class Jungol_1539 {
    static int N;

    static int[] DP;
    static ArrayList<Block> blockList;
    static int[] beforeArray;

    static int startIndex;
    static int maxHeight;

    static class Block implements Comparable<Block>{
        int width, height, weight, index;

        Block(int width, int height, int weight, int index) {
            this.width = width;
            this.height = height;
            this.weight = weight;
            this.index = index;
        }

        @Override
        public int compareTo(Block o) {
            if (this.width > o.width) {
                return -1;
            }

            return 1;
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        DP = new int[10010];
        blockList = new ArrayList<Block>();
    
        for (int index=0; index < N; index++) {
            st = new StringTokenizer(br.readLine());
            blockList.add(new Block(Integer.parseInt(st.nextToken()), 
                                    Integer.parseInt(st.nextToken()), 
                                    Integer.parseInt(st.nextToken()),
                                    index + 1));
        }

        Collections.sort(blockList);
        beforeArray = new int[N + 1];
        startIndex = 0;
        maxHeight = 0;

        for (int index=0; index < N; index++) {
            Block block = blockList.get(index);

            if (DP[block.weight] < block.height) {
                DP[block.weight] = block.height;
                beforeArray[block.index] = block.index;

                if (maxHeight < DP[block.weight]) {
                    maxHeight = DP[block.weight];
                    startIndex = block.index;
                }
            }

            for (int prev=0; prev < index; prev++) {
                Block prevBlock = blockList.get(prev);

                if (prevBlock.weight > block.weight) {
                    if (DP[block.weight] < block.height + DP[prevBlock.weight]) {
                        DP[block.weight] = block.height + DP[prevBlock.weight];
                        beforeArray[block.index] = prevBlock.index;
                    }
                }

                if (maxHeight < DP[block.weight]) {
                    maxHeight = DP[block.weight];
                    startIndex = block.index;
                }
            }
        }

        int count = 0;
        StringBuilder answer = new StringBuilder();

        while (true) {
            count += 1;
            answer.append(startIndex).append("\n");
            
            if (startIndex == beforeArray[startIndex]) {
                break;
            }

            startIndex = beforeArray[startIndex];
        }

        System.out.println(count);
        System.out.print(answer);
    }
}
