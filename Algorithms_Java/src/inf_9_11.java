import java.util.*;
public class inf_9_11 {
    public static int bfs(int[][] arr){
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0});
        arr[0][0] = 1;
        int L = 0;
        while(!q.isEmpty()){
            int len = q.size();
            for(int i=0;i<len;i++){
                int[] cur = q.poll();
                if(cur[0] == 6 && cur[1] == 6) return L;
                for(int j=0;j<4;j++){
                    int nx = cur[0] + dx[j];
                    int ny = cur[1] + dy[j];
                    if(nx >= 0 && nx < 7 && ny >= 0 && ny < 7 && arr[nx][ny] == 0){
                        arr[nx][ny] = 1;
                        q.offer(new int[]{nx,ny});
                    }
                }

            }
            L++;
        }
        return -1;
    }
    public static void main(String[] args){
        Scanner kb=new Scanner(System.in);
        int[][] arr = new int[7][7];
        for(int i=0;i<7;i++){
            for(int j=0;j<7;j++){
                arr[i][j] = kb.nextInt();
            }
        }
        System.out.println(bfs(arr));
    }
}
