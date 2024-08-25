import java.util.*;
public class prog57863 {

    static int[] visit;
    static ArrayList<Integer>[] graph;

    public void dfs(int here){
        visit[here] = 1;
        for(int next : graph[here]){
            if(visit[next] == 0){
                dfs(next);
            }
        }
    }
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        int size = wires.length;
        visit = new int[n+1];
        graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();

        for(int[] wire : wires){
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }

        for(int i=0;i<size;i++){
            //단선 Integer.valueOf(1)
            graph[wires[i][0]].remove(Integer.valueOf(wires[i][1]));
            graph[wires[i][1]].remove(Integer.valueOf(wires[i][0]));

            visit = new int[n+1];
            dfs(wires[i][0]);
            int s1 = Arrays.stream(visit).sum();
            int s2 = n-s1;

            answer = Math.min(answer, Math.abs(s1-s2));

            //복구
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]);
        }


        return answer;
    }
}
//n =6, wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]], answer = 2