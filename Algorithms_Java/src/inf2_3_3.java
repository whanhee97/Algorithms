import java.util.*;
public class inf2_3_3 {
    public int[] solution(int[] arrival, int[] state){
        int n = arrival.length;
        int[] answer = new int[n];

        Queue<Integer> enter = new LinkedList<>();
        Queue<Integer> exit = new LinkedList<>();
        int t = 0;
        int prev = 1; // 이전 기록한 상태값

        int start = 0; // arrival은 항상 정렬 돼서 나오므로 시작점 저장
        int cnt = 0; // 몇개 채웠는지 확인
        while(cnt < n){
            int id = -1;
            for(int i=start;i<n;i++){
                if(arrival[i] == t){ //도착시점이 현재 시간과 같으면
                    if(state[i] == 1) exit.offer(i); // 1이면 exit
                    else enter.offer(i); // 0이면 enter에 offer
                    start = i;
                }
            }
            if(prev == 1){ // 이전이 나가는거였으면
                if(!exit.isEmpty()){ // 나가는거 우선
                    id = exit.poll();
                }else{ // 나가는거 없으면
                    if(!enter.isEmpty()){ // 들어온거에서
                        id = enter.poll(); //빼고
                        prev = 0; // 상태값 변경
                    }
                }
            }else{ //이전이 들어오는거
                if(!enter.isEmpty()){ //들어오는거 우선
                    id = enter.poll();
                }else{
                    if(!exit.isEmpty()){ //들어오는거 없으면 나가는거
                        id = exit.poll();
                        prev = 1;
                    }
                }
            }
            if(id != -1){ //큐에서 pop된 id 있으면
                answer[id] = t; //해당 id에 시간 저장
                cnt++;
            }
            t++;
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_3_3 T = new inf2_3_3();
        System.out.println(Arrays.toString(T.solution(new int[]{0, 1, 1, 1, 2, 3, 8, 8}, new int[]{1, 0, 0, 1, 0, 0, 1, 0})));
        System.out.println(Arrays.toString(T.solution(new int[]{3, 3, 4, 5, 5, 5}, new int[]{1, 0, 1, 0, 1, 0})));
        System.out.println(Arrays.toString(T.solution(new int[]{2, 2, 2, 3, 4, 8, 8, 9, 10, 10}, new int[]{1, 0, 0, 0, 1, 1, 0, 1, 1, 0})));
    }
}
