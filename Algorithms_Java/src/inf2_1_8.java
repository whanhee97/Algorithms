import java.util.*;
public class inf2_1_8 {
    public int[] solution(int[] enter, int[] exit){
        int[] answer = new int[enter.length];
        List<Integer> room = new ArrayList<>(); // 방을 만들어서

        int outIdx = 0; //나가는 사람 인덱스
        for(int e: enter){
            room.add(e); //방에 집어넣고
            answer[e-1] = room.size()-1; //집어 넣은 사람의 카운트를 방에있는 사람수(자기 제외)로 초기화
            for(int x : room){ // 방에 있는 사람들 자기 제외하고 count 1씩 늘려줌
                if(x!=e){
                    answer[x-1] += 1;
                }
            }
            //exit 맨 앞에 있는사람이 방안에 있으면 방에서 없애줌 반복
            while(outIdx < exit.length && room.contains(exit[outIdx])){
                room.remove(Integer.valueOf(exit[outIdx]));
                outIdx++;
            }

        }
        return answer;
    }

    public static void main(String[] args){
        inf2_1_8 T = new inf2_1_8();
        System.out.println(Arrays.toString(T.solution(new int[]{1, 2, 3, 4}, new int[]{2, 4, 1, 3})));
        System.out.println(Arrays.toString(T.solution(new int[]{1, 2, 5, 3, 4}, new int[]{2, 3, 1, 4, 5})));
        System.out.println(Arrays.toString(T.solution(new int[]{1, 3, 2, 4, 5, 7, 6, 8}, new int[]{2, 3, 5, 6, 1, 4, 8, 7})));
        System.out.println(Arrays.toString(T.solution(new int[]{1, 4, 7, 2, 3, 5, 6}, new int[]{5, 2, 6, 1, 7, 3, 4})));
        System.out.println(Arrays.toString(T.solution(new int[]{1, 4, 2, 3}, new int[]{2, 1, 4, 3})));

    }
}
