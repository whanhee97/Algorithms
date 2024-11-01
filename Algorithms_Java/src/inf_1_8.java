import java.util.*;
public class inf_1_8 {
    public static int[] solution(int n, int[] arr){
        int[] answer = new int[n];

        for(int i=0;i<n;i++){
            int cnt = 1;
            for(int j=0;j<n;j++){
                if(i!=j){
                    if(arr[i]<arr[j]) cnt++;
                }
            }
            answer[i] = cnt;
        }

        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=kb.nextInt();
        }
        for(int x : solution(n, arr)){
            System.out.print(x + " ");
        }
    }
}
