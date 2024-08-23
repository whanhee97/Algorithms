import java.util.*;
public class prog43164 {
    static int size;
    static int[] chk;
    static String[][] tickets;
    static List<String> answerList;

    public void dfs(int L, String arrive, String root){
        if(L == size-1){
            answerList.add(root);
        }else{
            for(int i=0;i<size;i++){
                if(chk[i]==0 && tickets[i][0].equals(arrive)){
                    chk[i]=1;
                    String nextRoot = root + " " + tickets[i][1];
                    dfs(L+1,tickets[i][1],nextRoot);
                    chk[i]=0;
                }
            }
        }
    }

    public String[] solution(String[][] tickets1) {
        String[] answer = {};
        size = tickets1.length;
        tickets = tickets1;
        chk = new int[size];
        answerList = new ArrayList<>();
        for(int i=0;i<size;i++){
            if(tickets[i][0].equals("ICN")){
                chk[i] = 1;
                dfs(0,tickets[i][1],"ICN "+tickets[i][1]);
                chk[i] = 0;
            }
        }

        Collections.sort(answerList);
        answer = answerList.get(0).split(" ");
        return answer;
    }
}
