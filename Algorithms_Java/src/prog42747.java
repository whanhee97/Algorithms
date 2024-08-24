// testcase
// [0] 0
// [3, 4] 2
// [1, 2, 3, 5, 6, 7, 10, 11] 5
// [3, 5, 11, 6, 1, 5, 3, 3, 1, 41] 5
// [1, 11, 111, 1111] 3
// [3, 3, 3, 4]
import java.util.*;

public class prog42747 {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int size = citations.length;
        for(int i=1;i<=size;i++){
            int h = 0;
            for(int j=0;j<size;j++){
                if(citations[j] >= i){
                    h = size-j;
                    break;
                }
            }
            if(h >= i){
                answer = Math.max(answer,i);
            }
        }
        return answer;
    }
}
