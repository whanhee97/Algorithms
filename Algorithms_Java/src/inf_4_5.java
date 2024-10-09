import java.util.*;
public class inf_4_5 {
    public static int solution(int n, int k, int[] arr){
        int answer = -1;
        Set<Integer> s = new TreeSet<>(Comparator.reverseOrder());
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
                for(int y=j+1;y<n;y++){
                    s.add(arr[i]+arr[j]+arr[y]);
                }
            }
        }
        int cnt = 1;
        for(int x:s){
            if(cnt == k){
                answer = x;
                break;
            }
            cnt++;
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

        System.out.println(solution(n, k, arr));
        /*for(int x : solution(n,k,arr)){
            System.out.print(x + " ");
        }*/
    }
}
