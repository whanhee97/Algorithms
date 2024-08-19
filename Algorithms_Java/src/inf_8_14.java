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

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        n = kb.nextInt();
        m = kb.nextInt();

        pizzas = new ArrayList<>();
        houses = new ArrayList<>();
        answer = 1000;

        board = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j] = kb.nextInt();
                if(board[i][j] == 1){
                    houses.add(new Integer[] {i,j});
                }else if(board[i][j] == 2){
                    pizzas.add(new Integer[] {i,j});
                }
            }
        }
        combi = new int[pizzas.size()];
        dfs(0,0);
        System.out.print(answer);
    }
}
