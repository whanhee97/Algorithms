import java.util.*;
public class inf_9_6 {
    static int[] parents;

    public int find(int t){
        if(parents[t] == t){
            return t;
        }else{
            parents[t] = find(parents[t]);
            return parents[t];
        }
    }

    public void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a != b)
            parents[b] = a;
    }

    public String solution(int n, int m, int[][] arr, int a, int b){
        String answer;
        parents = new int[n+1];

        for(int i=1;i<=n;i++){
            parents[i] = i;
        }

        for(int[] coup: arr){
            union(coup[0],coup[1]);
        }
        if(find(a) == find(b)) answer = "YES";
        else answer = "NO";

        return answer;
    }
}
