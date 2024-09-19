public class inf_3_4 {
    public static int solution(int n, int m ,int[] arr){
        int answer = 0;
        int start = 0;
        int sum = 0;
        for(int end=0;end<n;end++){
            sum += arr[end];
            if(sum == m) answer++;
            while(sum>=m){
                sum -= arr[start];
                start++;
                if(sum == m) answer++;
            }
        }
        return answer;
    }
}
