import java.util.*;
public class inf_7_9 {
    public static int getCnt(int[] arr, int t){
        int cnt = 0;
        int sum = 0;
        for(int n : arr){
            if(sum + n > t){
                sum = 0;
                cnt++;
            }
            sum += n;
        }
        if(sum != 0) cnt++;
        return cnt;
    }

    public static int solution(int n, int m, int[] arr){
        int answer = 0;

        int l = 0;
        int r = Arrays.stream(arr).sum();
        int mid = (l+r)/2;
        while(r>l){
            if(getCnt(arr,mid) <= m){
                r = mid;
                answer = mid;
            }else{
                l = mid+1;
            }
            mid = (l+r)/2;
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int m = kb.nextInt();
        int[] arr = new int[n];

        for(int i=0;i<n;i++){
            arr[i] = kb.nextInt();
        }
        System.out.println(solution(n,m,arr));
    }
}
