import java.util.*;

public class inf2_1_2 {

    public int[] solution(int[][] board, int k){
        int[] answer;

        int[] dx = {1,0,-1,0}; //열
        int[] dy = {0,1,0,-1}; //행

        answer = new int[]{0,0};
        int i = 1;
        int dir = 0;
        while(i<=k){
            int nx = answer[1] + dx[dir];
            int ny = answer[0] + dy[dir];
            if(nx >= 0 && nx < board.length && ny >= 0 && ny < board.length && board[ny][nx] != 1){
                answer[1] = nx;
                answer[0] = ny;

            }else{
                dir++;
                dir = dir%4;
            }
            i++;
        }

        return answer;
    }

    public static void main(String[] args) {
        inf2_1_2 T = new inf2_1_2();
        int[][] arr1 = {
                {0, 0, 0, 0, 0},
                {0, 1, 1, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 1, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr1, 10)));
        int[][] arr2 = {
                {0, 0, 0, 1, 0, 1},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 1},
                {1, 1, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr2, 20)));
        int[][] arr3 = {
                {0, 0, 1, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 0, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr3, 25)));

    }
}
