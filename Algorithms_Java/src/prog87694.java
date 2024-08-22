import java.util.*;
public class prog87694 {
    public static int[][] board;

    public void makeRoad(int[][] rects){
        for(int[] r:rects) {
            for(int i=r[0]*2;i<=r[2]*2;i++){
                for(int j=r[1]*2;j<=r[3]*2;j++){
                    if(board[i][j] == 2) continue;
                    board[i][j] = 2;
                    if(i==r[0]*2 || i==r[2]*2 || j==r[1]*2 || j==r[3]*2){
                        board[i][j] = 1;
                    }
                }
            }
        }
    }
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        board = new int[101][101];

        makeRoad(rectangle);

        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        Queue<int[]> q = new LinkedList<>();

        q.offer(new int[] {characterX*2,characterY*2});
        board[characterX*2][characterY*2] = 0;

        while(!q.isEmpty()){
            int len = q.size();
            for(int i=0;i<len;i++){
                int[] now = q.poll();
                if(now[0] == itemX*2 && now[1] == itemY*2){
                    return answer/2;
                }
                for(int j=0;j<4;j++){
                    int nx = now[0] + dx[j];
                    int ny = now[1] + dy[j];
                    if(nx >= 0 && nx < 101 && ny >=0 && ny < 101 && board[nx][ny] == 1){
                        board[nx][ny] = 0;
                        q.offer(new int[] {nx,ny});
                    }
                }
            }
            answer++;
        }

        return answer/2;
    }
}
