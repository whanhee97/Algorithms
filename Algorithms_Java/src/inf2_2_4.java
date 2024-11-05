import java.util.*;
public class inf2_2_4 {
    public int solution(int[] nums, int m){
        /*
        * 0. sum - m == 0 일 경우 무조건 하나를 포함하고 있어야함 (sum == m 이기 때문에)
        * 1. sum 은 0~i까지의 합(끝이 nums[i]인 수열의 총합)
        * 2. 해시에 sum을 키값으로 빈도수를 기록함
        * 3. sum-m 값이 만약 해시에 존재한다면?? sum-m 이 끝인 수열의 합의 빈도수 -> 이것은 다른말로 m의 빈도수를 뜻함.
        * 4. 따라서, answer에 m의 빈도수 즉, sum-m의 빈도수를 더해줌
        * */

        int answer = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();
        int sum = 0;
        hm.put(0,1); //0
        for(int i=0;i<nums.length;i++){
            sum += nums[i]; //1
            if(hm.keySet().contains(sum-m)) { //3
                answer += hm.get(sum-m); //4
            }
            hm.put(sum,hm.getOrDefault(sum,0)+1); //2
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_2_4 T = new inf2_2_4();
        System.out.println(T.solution(new int[]{2, 2, 3, -1, -1, -1, 3, 1, 1}, 5));
        System.out.println(T.solution(new int[]{1, 2, 3, -3, 1, 2, 2, -3}, 5));
        System.out.println(T.solution(new int[]{1, 2, 3, -3, 1, 2}, 3));
        System.out.println(T.solution(new int[]{-1, 0, 1}, 0));
        System.out.println(T.solution(new int[]{-1, -1, -1, 1}, 0));
    }
}
