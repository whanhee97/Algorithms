import java.util.*;
public class inf_5_3 {
    public static int solution(int n, int[][] board, int m, int[] moves){
        Stack<Integer> st = new Stack<>();
        int answer = 0;
        for(int move:moves){
            for(int i=0;i<n;i++){
                if (board[i][move-1] != 0){
                    if(!st.empty() && st.peek() == board[i][move-1]){
                        st.pop();
                        answer += 2;
                    }else{
                        st.push(board[i][move-1]);
                    }
                    board[i][move-1] = 0;
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] board = new int[n][n];
        for (int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j] = kb.nextInt();
            }
        }
        int m = kb.nextInt();
        int[] moves = new int[m];
        for(int i=0;i<m;i++){
            moves[i] = kb.nextInt();
        }

        System.out.println(solution(n,board,m,moves));
        /*for(int x : solution(n,k,arr)){
            System.out.print(x + " ");
        }*/
    }
}
