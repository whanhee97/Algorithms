import java.util.*;
public class inf_9_13 {
    static int n;
    static int[][] arr;
    static int[] dx = {1,-1,0,0,1,-1,1,-1};
    static int[] dy = {0,0,1,-1,1,-1,-1,1};

    public static void dfs(int i, int j){
        arr[i][j] = 0;
        for(int z=0;z<8;z++){
            int nx = i + dx[z];
            int ny = j + dy[z];
            if(nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny] == 1){
                dfs(nx,ny);
            }
        }
    }
    public static void bfs(int i, int j){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{i,j});
        arr[i][j] = 0;
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for(int z=0;z<8;z++){
                int nx = cur[0] + dx[z];
                int ny = cur[1] + dy[z];
                if(nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny] == 1){
                    arr[nx][ny] = 0;
                    q.offer(new int[]{nx,ny});
                }
            }
        }
    }
    public static void main(String[] args){
        Scanner kb=new Scanner(System.in);
        int answer = 0;
        n = kb.nextInt();
        arr = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr[i][j] = kb.nextInt();
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(arr[i][j] == 1){
                    dfs(i,j);
                    answer++;
                }
            }
        }

        System.out.println(answer);
    }
}
