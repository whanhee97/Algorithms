import java.util.*;
public class inf2_1_6 {
    static int[] visit;
    public int getMinIdx(int[] f){
        int min = 10000;
        int minIdx = 0;
        for(int i=0;i<3;i++){
            if(f[i]<min){
                min = f[i];
                minIdx = i;
            }else if(f[i] == min){
                return -1;
            }
        }
        return minIdx;
    }

    public int solution(int[][] fruit){
        /*
        * 서로 이득을 보는 조건
        *
        * 1) 최솟값이 유니크해야함. -> 그렇지 않으면 바꿔도 다른 과일을 가져가야 하기 때문에 이득이 아님.
        * 2) 최솟값의 인덱스가 서로 같으면 안 됨. -> 문제 조건
        * 3) 바꾸었을때 최솟값이 유지가 되어야함. -> 1)과 마찬가지로 바꿔도 다른 과일을 가져가야함.
        *
        * */

        int n = fruit.length;
        visit = new int[n];

        for(int i=0;i<n;i++){
            if(visit[i] != 0) continue; // i방문 안 했고

            int iMin = getMinIdx(fruit[i]);
            if(iMin == -1) continue; //유니크하지 않으면 패스

            for(int j=i+1;j<n;j++){
                if(visit[j] != 0) continue; // j방문 안 했고

                int jMin = getMinIdx(fruit[j]);
                if(jMin == -1) continue; //유니크하지 않으면 패스

                if(iMin == jMin) continue; //최솟값의 인덱스가 같으면 패스

                if(fruit[i][iMin]+1 <= fruit[i][jMin]-1 && fruit[j][jMin]+1 <= fruit[j][iMin]-1){ //바꿔도 최솟값이 유지되면
                    //교환하고
                    fruit[i][iMin]++;
                    fruit[i][jMin]--;
                    fruit[j][jMin]++;
                    fruit[j][iMin]--;

                    //최솟값을 저장
                    visit[i] = fruit[i][iMin];
                    visit[j] = fruit[j][jMin];
                    break;
                }
            }
        }

        for(int i=0;i<n;i++){
            if(visit[i] == 0){
                visit[i] = Arrays.stream(fruit[i]).min().getAsInt();
            }
        }

        return Arrays.stream(visit).sum();
    }


    public static void main(String[] args){
        inf2_1_6 T = new inf2_1_6();
        System.out.println(T.solution(new int[][]{{10, 20, 30}, {12, 15, 20}, {20, 12, 15}, {15, 20, 10}, {10, 15, 10}}));
        System.out.println(T.solution(new int[][]{{10, 9, 11}, {15, 20, 25}}));
        System.out.println(T.solution(new int[][]{{0, 3, 27}, {20, 5, 5}, {19, 5, 6}, {10, 10, 10}, {15, 10, 5}, {3, 7, 20}}));
        System.out.println(T.solution(new int[][]{{3, 7, 20}, {10, 15, 5}, {19, 5, 6}, {10, 10, 10}, {15, 10, 5}, {3, 7, 20}, {12, 12, 6}, {10, 20, 0}, {5, 10, 15}}));
    }
}

