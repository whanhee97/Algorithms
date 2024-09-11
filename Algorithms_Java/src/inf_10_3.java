import java.util.*;

public class inf_10_3 {

    public int solution(int n, int[] arr){
        int answer = 0;
        int[] dp = new int[n];
        dp[0] = 1;
        for(int i=1;i<n;i++){
            int max = 0;
            for(int j=i-1;j>=0;j--){
                if(arr[i]>arr[j] && dp[j] > max) {
                    max = dp[j];
                }
            }
            dp[i] = max + 1;
            answer = Math.max(answer, dp[i]);
        }
        return answer;
    }
}
