public class inf_10_5 {
    public int solution(int m, int[] arr){
        int[] dp = new int[m+1];

        for(int i=0;i<=m;i++){
            int min = Integer.MAX_VALUE;
            for(int j : arr){
                if(i == j){
                    min = 0;
                    break;
                }else if(i > j){
                    if(dp[i-j] < min){
                        min = dp[i-j];
                    }
                }
            }
            dp[i] = min+1;
        }

        return dp[m];
    }

    public int solution2(int m, int[] arr){
        int[] dp = new int[m+1];
        for(int i=1;i<=m;i++){
            dp[i] = Integer.MAX_VALUE;
        }
        for(int i : arr){
            for(int j=i;j<=m;j++){
                dp[j] = Math.min(dp[j],dp[j-i]+1);
            }
        }
        return dp[m];
    }
}