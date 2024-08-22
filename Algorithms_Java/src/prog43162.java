import java.util.*;

public class prog43162 {

    public static int[] visit;
    public static int gn;
    public static int[][] gCom;

    public void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        visit[start] = 1;
        q.offer(start);

        while(!q.isEmpty()){
            int cur = q.poll();
            for(int i=0;i<gn;i++){
                if(visit[i] == 0 && gCom[cur][i] == 1){
                    visit[i] = 1;
                    q.offer(i);
                }
            }
        }
    }

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visit = new int[n];
        gn = n;
        gCom = computers;

        for(int i=0;i<n;i++){
            if(visit[i] == 0){
                bfs(i);
                answer++;
            }
        }

        return answer;
    }
}
