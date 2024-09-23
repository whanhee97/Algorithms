public class inf_3_5 {
    public static int solution(int n){
        int answer = 0;

        int[] arr = new int[n-1];

        for(int i=0;i<n-1;i++){
            arr[i] = i+1;
        }

        int sum = 0;
        int j = 0;
        for(int i=0;i<n-1;i++){
            sum += arr[i];
            if(sum == n) answer++;
            while(sum > n){
                sum -= arr[j];
                j++;
                if(sum == n) answer++;
            }
        }
        return answer;
    }
}
