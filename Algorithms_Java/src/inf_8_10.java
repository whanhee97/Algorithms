import java.util.*;

/*https://cote.inflearn.com/contest/10/problem/08-10*/
public class inf_8_10 {
    public static int[][] board;
    public static int[] dx = {1,-1,0,0};
    public static int[] dy = {0,0,1,-1};
    public static int answer;

    public static void dfs(int cx, int cy){
        if(cx == 6 && cy == 6){
            answer++;
        }else{
            for(int i=0;i<4;i++){
                int nx = dx[i] + cx;
                int ny = dy[i] + cy;
                if(nx>=0 && nx<7 && ny>=0 && ny<7 && board[nx][ny] == 0){
                    board[nx][ny] = 1;
                    dfs(nx,ny);
                    board[nx][ny] = 0;
                }
            }
        }
    }

}
