import java.util.*;
class Task implements Comparable<Task>{
    public int idx; //인덱스
    public int start; //호출시간
    public int run; //실행시간

    public Task(int idx, int start, int run){
        this.idx = idx;
        this.start = start;
        this.run = run;
    }

    @Override
    public int compareTo(Task o){
        return this.run == o.run?this.idx-o.idx:this.run-o.run;
    }
}
public class inf2_3_5 {
    public int[] solution(int[][] tasks){
        int[] answer = new int[tasks.length];
        int n = 0;
        HashMap<Integer, ArrayList<Task>> hm = new HashMap<>(); // 인덱스 접근을 위해 해시사용

        for(int i=0;i<tasks.length;i++){ // 실행시간을 키값, taskList를 밸류
            hm.put(tasks[i][0],new ArrayList<Task>());
        }

        for(int i=0;i<tasks.length;i++){ // Task는 인덱스를 맨앞에 추가한 옵젝
            hm.get(tasks[i][0]).add(new Task(i,tasks[i][0],tasks[i][1])); // 해당하는 실행시간에 하나씩 추가
        }

        int time=0;
        PriorityQueue<Task> pq = new PriorityQueue<>(); // 우선순위큐 실행시간으로 정렬 같으면 idx로 정렬
        int running = 0; //실행시간
        Task runT = null; //실행중인 태스크
        while(time<=10000 && n < tasks.length){
            if(runT != null && running == runT.run){ // 실행중인 작업이 있고 실행시간 다 지나면
                runT = null; // 실행중지
            }
            if(hm.containsKey(time)){ //현재 시간대의 작업 모두 큐에 집어넣음
                ArrayList<Task> candi = hm.get(time);
                for(Task t:candi){
                    pq.offer(t);
                }
            }
            if(runT == null && !pq.isEmpty()){ //실행중인 작업이 없고 대기중인 작업이 있으면
                runT = pq.poll(); // 실행
                answer[n] = runT.idx; // 답추가
                n++; // while문 멈추기위해
                running = 0; // 실행시간 초기화
            }
            running++;
            time++;
        }
        //System.out.println(time);
        return answer;
    }

    // 정답코드에서는 큐를 하나 만들어서 {idx, start, run} 형태로 집어 넣은뒤 start로 정렬
    // 우선순위 큐 생성 -> 위와 동일하게 (선언문에 람다를 활용해 정렬규칙 정의)
    // while 문(일반큐와 pq 둘다 비어있지 않으면 실행)
    // finishTime 변수를 만들고 pq 비어있으면 일반큐 peek의 실행시간과 비교해서 큰값 넣어줌(대기중인게 없을때 시간이 붕 뜰때)
    // while문으로 일반큐가 비어있지 않고 peek가 finishTime보다 작으면 pq에 작업추가
    // pq에서 하나씩 빼서 finishTime에 실행시간 더해줌
    public static void main(String[] args){
        inf2_3_5 T = new inf2_3_5();
        System.out.println(Arrays.toString(T.solution(new int[][]{{2, 3}, {1, 2}, {8, 2}, {3, 1}, {10, 2}})));
        System.out.println(Arrays.toString(T.solution(new int[][]{{5, 2}, {7, 3}, {1, 3}, {1, 5}, {2, 2}, {1, 1}})));
        System.out.println(Arrays.toString(T.solution(new int[][]{{1, 2}, {2, 3}, {1, 3}, {3, 3}, {8, 2}, {1, 5}, {2, 2}, {1, 1}})));
        System.out.println(Arrays.toString(T.solution(new int[][]{{999, 1000}, {996, 1000}, {998, 1000}, {999, 7}})));
    }
}
