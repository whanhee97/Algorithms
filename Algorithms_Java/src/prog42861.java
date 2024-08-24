import java.util.*;
public class prog42861 {
    static int[] parents;
    public static int findParent(int target){
        if(parents[target] == target) return target; //재귀 돌다가 같아지면 리턴
        else{
            target = findParent(parents[target]); //같아지는거 찾을때 까지 재귀돌기
            return target;
        }
    }
    public static boolean union(int a, int b){
        a = findParent(a); // 부모 찾고
        b = findParent(b); // 부모 찾고
        if(a != b){ // 부모가 다르면
            parents[b] = a; //b의 부모를 a로 (간선 이거주기)
            return true; //이어주면 true
        }
        return false; // 부모가 같으면 안 이어줘도 되므로 false
    }

    public int solution(int n, int[][] costs) {
        int answer = 0;
        int size = costs.length;
        parents = new int[n];
        Arrays.sort(costs, (a,b)->a[2]-b[2]);
        for(int i=0;i<n;i++){
            parents[i] = i; // 각각의 부모를 자기 자신으로 (아무것도 안 이어져있는 상태)
        }

        for(int[] cost:costs){
            if(union(cost[0],cost[1])) answer += cost[2]; // 안 이어져있다면 이어주고 비용 더해주기
        }

        return answer;
    }
}
