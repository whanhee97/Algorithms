import java.util.*;
public class inf2_1_5 {
    public int solution(int[] nums){
        int answer = 0;
        ArrayList<Integer> peaks = new ArrayList<>();
        for(int i=1;i<nums.length-1;i++){
            if(nums[i] > nums[i-1] && nums[i] > nums[i+1]){
                peaks.add(i);
            }
        }

        for(int peak : peaks){
            int cnt=1;
            int left = peak-1;
            int right = peak+1;
            while(left >= 0){
                if(nums[left+1] > nums[left]){
                    cnt++;
                    left--;
                }else break;
            }
            while(right < nums.length){
                if(nums[right-1]>nums[right]){
                    cnt++;
                    right++;
                }else break;
            }
            answer = Math.max(answer,cnt);
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_1_5 T = new inf2_1_5();
        System.out.println(T.solution(new int[]{1, 2, 1, 2, 3, 2, 1}));
        System.out.println(T.solution(new int[]{1, 1, 2, 3, 5, 7, 4, 3, 1, 2}));
        System.out.println(T.solution(new int[]{3, 2, 1, 3, 2, 4, 6, 7, 3, 1}));
        System.out.println(T.solution(new int[]{1, 3, 1, 2, 1, 5, 3, 2, 1, 1}));
    }
}
