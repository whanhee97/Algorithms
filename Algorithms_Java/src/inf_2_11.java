import java.util.*;
public class inf_2_11 {
    public static int solution(int n, int[][] arr){

        int[] result = new int[n];
        for(int i=0;i<n;i++){
            int[] visit = new int[n];
            for(int j=0;j<5;j++){
                for(int k=0;k<n;k++){
                    if(i!=k && arr[i][j] == arr[k][j]){
                        if(visit[k] != 1) visit[k]=1;
                    }
                }
            }
            result[i] = Arrays.stream(visit).sum();
        }
        int mx = 0;
        int answer = 0;
        for(int i=0;i<n;i++){
            if(mx < result[i]){
                mx = result[i];
                answer = i;
            }
        }
        return answer+1;
    }
}
