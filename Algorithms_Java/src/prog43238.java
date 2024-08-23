import java.util.*;
public class prog43238 {
    public long canPass(long target, int[] times){
        long cnt = 0;
        for(int t: times){
            cnt += target / t;
        }
        return cnt;
    }
    public long solution(int n, int[] times) {
        long answer = 0;
        long lt = 1;
        long rt = (long)Arrays.stream(times).max().getAsInt() * n;
        if(times.length == 1){
            return (long)times[0]*n;
        }
        long min = Long.MAX_VALUE;
        long mid;
        long personCnt;
        while(lt <= rt){
            mid = (lt + rt)/2;
            personCnt = canPass(mid,times);
            if(personCnt<n){
                lt = mid + 1;
            }else{
                min = Math.min(min,mid);
                rt = mid - 1;
            }
        }
        answer = min;
        return answer;
    }
}
