import java.util.*;
class Job implements Comparable<Job>{
    public int rt, wt;
    public Job(int rt,int wt){
        this.rt = rt;
        this.wt = wt;
    }

    @Override
    public int compareTo(Job o){
        return this.wt != o.wt ? this.wt-o.wt : this.rt-o.rt;
    }

}


public class prog42627 {

    public int solution(int[][] jobs) {
        int answer = 0;
        int start = -1;
        int now = 0;
        int size = jobs.length;
        int cnt = 0; // 수행한 잡 개수

        List<Job> jobList = new ArrayList<>();
        for(int[] x:jobs){
            jobList.add(new Job(x[0],x[1]));
        }

        PriorityQueue<Job> running = new PriorityQueue<>();

        while(size>cnt){ // 사이즈만큼 수행
            for(Job job : jobList){
                if(start < job.rt && job.rt <= now){ //요청시간이 지금보다 작거나 같으면
                    running.offer(job); //러닝큐에 넣음
                }
            }
            if(!running.isEmpty()){ //러닝큐가 비어있지 않으면
                Job cur = running.poll(); // 하나뽑아서
                start = now; //마지막 완료시간 갱신
                answer += (now-cur.rt)+cur.wt;
                now += cur.wt;

                cnt++; //수행회수 추가
            }else{
                now += 1;
            }
        }

        answer = answer / size;

        return answer;
    }


}
