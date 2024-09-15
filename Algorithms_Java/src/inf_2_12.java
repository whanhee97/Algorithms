import java.util.*;
public class inf_2_12 {
    public static int solution(int n, int m, int[][] arr){
        int answer = 0;
        int flag = 0;
        //i는 학생번호
        for(int i=1;i<n+1;i++){
            int[] visit = new int[n];

            for(int j=0;j<m;j++){
                flag = 0;
                for(int k=0;k<n;k++){
                    if(arr[j][k] == i){
                        flag = 1;
                    }
                    if(flag!=1){
                        visit[arr[j][k]-1] = 1;
                    }
                }
            }
            answer += n-(Arrays.stream(visit).sum()+1);
        }
        return answer;
    }
}
