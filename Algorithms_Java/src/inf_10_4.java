import java.util.*;

public class inf_10_4 {
    public int solution(int n, int[][] arr){
        Arrays.sort(arr,(a,b)->b[2]-a[2]); // 무게로 정렬
        int[] dp = new int[n]; //i번째 까지 쌓는 가장 큰 높이 누적치
        dp[0] = arr[0][1]; // 첫번째 높이 입력 -> 무게로 정렬 했으므로 젤 무거운게 밑이라 높이 고정
        int answer = 0;
        for(int i=1;i<n;i++){
            int max = 0;
            for(int j=i-1;j>=0;j--){
                if(arr[i][0]<arr[j][0] && max<dp[j]){ // j가 쭉 거꾸로 돌면서 밑면이 더 큰것들 중 가장 큰 누적 높이 저장
                    max = dp[j];
                }
            }
            dp[i] = arr[i][1] + max;
            answer = Math.max(answer, dp[i]);
        }

        return answer;
    }
}
