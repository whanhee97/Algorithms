import java.util.*;

class Time implements Comparable<Time>{
    public int s,e;
    public Time(int s, int e){
        this.s = s;
        this.e = e;
    }

    @Override
    public int compareTo(Time t){
        return this.e != t.e?this.e - t.e : this.s - t.s;
    }
}

public class inf_9_2 {


    public static int solution(int n, ArrayList<Time> times){
        Collections.sort(times);
        int eoc = 0;
        int cnt = 0;
        for(Time x : times){
            int s = x.s;
            int e = x.e;
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
        ArrayList<Time> times = new ArrayList<>();
        for(int i=0;i<n;i++){
            int s = kb.nextInt();
            int e = kb.nextInt();
            times.add(new Time(s,e));
        }

        System.out.print(solution(n,times));
    }
}
