import java.util.*;
public class inf_10_6_1 {
    public static int solution(int n, int m, int[][] arr){
        int[] dp = new int[m+1];
        for(int i=0;i<n;i++){
            int s = arr[i][0];
            int t = arr[i][1];
            for(int j=m;j>=t;j--){
                dp[j] = Math.max(dp[j-t]+s, dp[j]);
            }
        }
        return dp[m];
    }
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();

        int[][] arr = new int[n][2];
        for(int i=0;i<n;i++){
            int s = kb.nextInt();
            int t = kb.nextInt();
            arr[i] = new int[]{s,t};
        }
        System.out.println(solution(n,m,arr));

    }
}
