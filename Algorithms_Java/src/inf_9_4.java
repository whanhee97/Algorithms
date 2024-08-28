import java.util.*;

class MD implements Comparable<MD>{
    int m;
    int d;
    public MD(int m, int d){
        this.m = m;
        this.d = d;
    }

    @Override
    public int compareTo(MD o){
        return o.m-this.m;
    }
}
public class inf_9_4 {

    public int solution(int n, int[][] MDArr){
        Arrays.sort(MDArr, (a,b)-> b[1]-a[1]);

        int maxDay = MDArr[0][1];
        int[] chk = new int[maxDay+1];

        PriorityQueue<MD> pq = new PriorityQueue<>();

        int sum = 0;
        int j = 0;
        for(int day=maxDay;day>=1;day--){
            for( ;j<n;j++){
                if(MDArr[j][1] < day){
                    break;
                }
                pq.offer(new MD(MDArr[j][0],MDArr[j][1]));
            }
            if(!pq.isEmpty()){
                sum += pq.poll().m;
            }
        }

        return sum;
    }
}
