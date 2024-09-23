public class inf_3_3 {
    public static int solution(int n, int k ,int[] arr){
        int tmp = 0;

        int start = 0;
        int end = start+k;

        for(int i=start;i<end;i++){
            tmp += arr[i];
        }

        int answer = tmp;

        while(end<n){
            tmp = tmp - arr[start] + arr[end];
            if(answer<tmp) answer = tmp;
            start++;
            end++;
        }
        return answer;
    }
}
