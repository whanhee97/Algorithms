import java.util.*;

public class inf2_3_4 {
    public int solution(int[] laser, String[] enter){
        int answer = 0;
        Queue<Integer> q = new LinkedList<>(); // 대기큐

        int now = 0; // 시술 끝난 시간
        int[] visit = new int[enter.length]; //방문기록
        while(Arrays.stream(visit).sum() != enter.length){ // 방문기록이 다 안 채워지면 실행
            //System.out.println("now::::::::" + now);
            for(int i=0;i<enter.length;i++){
                if(visit[i] == 1) continue; //방문했으면 패스

                // i번째 시작시간 파싱
                int start = Integer.parseInt(enter[i].split(" ")[0].split(":")[0])*60
                        + Integer.parseInt(enter[i].split(" ")[0].split(":")[1]);
                if(now > start){ // 시작시간이 이전 사람 시술 종료시간 보다 빠르면 대기큐에 계속 넣어줌
                    q.offer(laser[Integer.parseInt(enter[i].split(" ")[1])]); // 시술시간을 대기큐에 삽입
                    //System.out.println("offer::::::::" + i);
                    visit[i] = 1; //방문표시
                }else if(q.isEmpty()){ //큐가 비었으면 시술끝시간을 파싱해서 저장하고 방문표시하고 스탑
                    now = Integer.parseInt(enter[i].split(" ")[0].split(":")[0])*60
                            + Integer.parseInt(enter[i].split(" ")[0].split(":")[1])
                            + laser[Integer.parseInt(enter[i].split(" ")[1])];
                    //System.out.println("empty::::::::" + i);
                    visit[i] = 1;
                    break;
                }else{ // 시작시간이 시술 끝시간보다 늦으면 그냥 암것도 안하고 패스
                    //System.out.println("now가 작고 안비어있음::::::::" + i);
                    break;
                }
            }
            answer = Math.max(answer, q.size()); //정답 갱신
            if(!q.isEmpty()){ // 대기큐가 안 비어있으면
                int t = q.poll(); // 시술시간 꺼네서
                now += t; // 현재시간에 더해줌 -> 시술끝시간이 됨
            }
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_3_4 T = new inf2_3_4();
        System.out.println(T.solution(new int[]{30, 20, 25, 15}, new String[]{"10:23 0", "10:40 3", "10:42 2", "10:52 3", "11:10 2"}));
        System.out.println(T.solution(new int[]{30, 20, 25, 15}, new String[]{"10:23 0", "10:40 3", "10:42 2", "10:52 3", "15:10 0", "15:20 3", "15:22 1", "15:23 0", "15:25 0"}));
        System.out.println(T.solution(new int[]{30, 20, 25, 15}, new String[]{"10:20 1", "10:40 1", "11:00 1", "11:20 1", "11:40 1"}));
    }
}
