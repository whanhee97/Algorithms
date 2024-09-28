import java.util.*;
public class inf2_1_4 {
    public int[] solution(int c, int r, int k){
        if(k>r*c){
            return new int[]{0,0};
        }
        int[][] seats = new int[r][c];
        int[] dc = {0,1,0,-1};
        int[] dr = {1,0,-1,0};
        int[] cur = new int[]{0,0};
        int dir = 0;
        int cnt = 1;
        seats[0][0] = 1;
        while(true){
            if(cnt == k){
                cur[0]++;
                cur[1]++;
                return cur;
            }
            int nc = cur[0] + dc[dir];
            int nr = cur[1] + dr[dir];
            if(nc>=0 && nc<c && nr>=0 && nr<r && seats[nr][nc]!=1){
                cur[0] = nc;
                cur[1] = nr;
                seats[cur[1]][cur[0]] = 1;
                cnt++;
            }else{
                dir = (dir+1)%4;
            }

        }

    }

    public static void main(String[] args){
        inf2_1_4 T = new inf2_1_4();
        System.out.println(Arrays.toString(T.solution(6, 5, 12)));
        System.out.println(Arrays.toString(T.solution(6, 5, 20)));
        System.out.println(Arrays.toString(T.solution(6, 5, 30)));
        System.out.println(Arrays.toString(T.solution(6, 5, 31)));
    }
}
