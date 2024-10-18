import java.util.*;
public class inf_10_5_1 {
    public static int solution(int n, int m, int[] arr){
        int[] dp = new int[m+1];

        for(int i=1;i<=m;i++){
            dp[i] = Integer.MAX_VALUE;
            for(int j : arr){
                if(i-j == 0){
                    dp[i] = 1;
                    break;
                }
                if(i-j > 0){
                    dp[i] = Math.min(dp[i-j]+1,dp[i]);
                }

            }
        }
        return dp[m];
    }
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = kb.nextInt();
        }
        int m = kb.nextInt();

        System.out.println(solution(n,m,arr));
    }
}
