import java.util.*;
public class prog43163 {

    public boolean isSimilar(String a, String b){
        int cnt = 0;
        for(int i=0;i<a.length();i++){
            if(a.charAt(i) != b.charAt(i)){
                cnt++;
                if(cnt > 1) return false;
            }
        }
        return true;
    }

    public int solution(String begin, String target, String[] words) {
        int answer = 1;
        int[] visit = new int[words.length];

        Queue<String> q = new LinkedList<>();
        for(int i=0;i<words.length;i++){
            if(isSimilar(begin,words[i])){
                q.offer(words[i]);
                visit[i] = 1;
            }
        }
        while(!q.isEmpty()){

            int len = q.size();
            for(int j=0;j<len;j++){
                String now = q.poll();
                if(now.equals(target)){
                    return answer;
                }
                for(int i=0;i<words.length;i++){
                    if(visit[i] == 0 && isSimilar(now,words[i])){
                        q.offer(words[i]);
                        visit[i] = 1;
                    }
                }
            }

            answer++;
        }

        return 0;

    }
}
