import java.util.*;
// Time Limit Exceeded
public class inf_9_2 {

    public static int solution(int n, ArrayList<int[]> times){
        Collections.sort(times, (a,b)-> a[1] != b[1] ? a[1]-b[1] : a[0]-b[0]);
        int eoc = 0;
        int cnt = 0;
        for(int[] x : times){
            int s = x[0];
            int e = x[1];
            if(eoc <= s){
                eoc = e;
                cnt++;
            }
        }
        return cnt;
    }
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        ArrayList<int[]> times = new ArrayList<>();
        for(int i=0;i<n;i++){
            int s = kb.nextInt();
            int e = kb.nextInt();
            times.add(new int[]{s,e});
        }

        System.out.print(solution(n,times));
    }
}
