import java.util.*;
public class inf2_3_1 {
    public int solution(int[] nums){
        int answer = 0;
        Arrays.sort(nums);
        Set<Integer> ts = new TreeSet<>();
        for(int n : nums){
            ts.add(n);
        }
        int[] numList = new int[ts.size()];
        int i = 0;
        for(int n : ts){
            numList[i] = n;
            i++;
        }
        i = 0;
        int cnt = 1;
        while(i<numList.length-1){
            if(numList[i]+1 == numList[i+1]){
                cnt++;
            }else{
                answer = Math.max(cnt,answer);
                cnt = 1;
            }
            i++;
        }
        answer = Math.max(cnt,answer);

        return answer;
    }

    public int solution2(int[] nums){
        int answer = 0;
        HashSet<Integer> set = new HashSet<>(); // contains 할때 -> 해시셋을 써야 O(1) 트리셋 쓰면 O(logN)
        for(int x : nums) set.add(x);
        for(int x : set){
            if(set.contains(x - 1)) continue; // x보다 1작은 숫자가 존재하면 패스
            int cnt = 0;
            while(set.contains(x)){ //하나씩 증가시키면서 존재하면 cnt++
                cnt++;
                x++;
            }
            answer = Math.max(answer, cnt);
        }
        return answer;
    }

    public static void main(String[] args){
        inf2_3_1 T = new inf2_3_1();
        System.out.println(T.solution(new int[]{8, 1, 9, 3, 10, 2, 4, 0, 2, 3}));
        System.out.println(T.solution(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0}));
        System.out.println(T.solution(new int[]{3, 3, 3, 3, 3, 3, 3, 3}));
        System.out.println(T.solution(new int[]{-3, -1, -2, 0, 3, 3, 5, 6, 2, 2, 1, 1}));
        System.out.println(T.solution(new int[]{-5, -3, -1, -4, 3, 3, 5, 6, 2, 2, 1, 1, 7}));
    }
}
