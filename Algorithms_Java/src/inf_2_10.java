import java.util.*;
public class inf_2_10 {
    public static int solution(int n, int[][] arr){
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        int answer = n*n;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                for(int k=0;k<4;k++){
                    if((i+dx[k]>=0 && i+dx[k]<n) && (j+dy[k]>=0 && j+dy[k]<n)){
                        if(arr[i][j] <= arr[i+dx[k]][j+dy[k]]){
                            answer--;
                            break;
                        }
                    }
                }
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[][] arr = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr[i][j]=kb.nextInt();
            }
        }
        /*for(int x : solution(n, arr)){
            System.out.print(x + " ");
        }*/
        System.out.print(solution(n, arr));
    }
}
