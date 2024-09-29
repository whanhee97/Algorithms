import java.util.*;
public class inf_3_6 {
    public static int solution(int n,int k, int[] arr){
        int answer = 0;
        int len = 0;
        int cnt = 0;
        int lt = 0;
        for(int rt=0;rt<n;rt++){
            len += 1;
            if(arr[rt] == 0){
                cnt++;
                while(cnt>k){
                    len -= 1;
                    if(arr[lt] == 0) cnt--;
                    lt++;
                }
            }
            if(answer < len) answer = len;
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        int n = kb.nextInt();
        int k = kb.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = kb.nextInt();
        }
        System.out.println(solution(n,k,arr));
    }
}
