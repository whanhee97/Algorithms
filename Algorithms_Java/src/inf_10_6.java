public class inf_10_6 {

    public int solution(int n, int m, int[][] arr){
        int[] dp = new int[m+1];
        for(int i=0;i<n;i++){
            int score = arr[i][0];
            int time = arr[i][1];
            for(int j=m;j>=time;j--){
                dp[j] = Math.max(dp[j], dp[j-time]+score);
            }
        }

        return dp[m];
    }
}
