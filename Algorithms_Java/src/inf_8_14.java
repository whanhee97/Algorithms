import java.util.*;

public class inf_8_14 {
    static int n;
    static int m;
    static int[][] board;
    static ArrayList<Integer[]> pizzas;
    static ArrayList<Integer[]> houses;
    static int[] combi;
    static int answer;

    public static int calDis(){
        int sum = 0;
        for(Integer[] house : houses) {
            int dis = 1000;
            for (int i : combi) {
                Integer[] pizza = pizzas.get(i);
                dis = Math.min(dis,Math.abs(house[0] - pizza[0]) + Math.abs(house[1] - pizza[1]));
            }
            sum += dis;
        }
        return sum;
    }
    public static void dfs(int L, int start){
        if(L == m){
            answer = Math.min(answer, calDis());
        }else{
            for(int i=start;i<combi.length;i++){
                if(combi[i] != 1){
                    combi[L] = i;
                    dfs(L+1,i+1);
                }
            }
        }
    }

}
