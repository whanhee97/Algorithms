import java.util.*;
public class inf2_1_3 {
    public int solution(int[][] board){
        int answer = 0;
        int[] dx = {-1,0,1,0};
        int[] dy = {0,1,0,-1};

        int dirH = 0;
        int dirD = 0;
        int[] h = new int[2];
        int[] d = new int[2];
        for(int x=0;x<10;x++){
            for(int y=0;y<10;y++){
                if(board[x][y] == 2){
                    h = new int[]{x,y};
                }
                if(board[x][y] == 3){
                    d = new int[]{x,y};
                }
            }
        }

        int nxH;
        int nyH;
        int nxD;
        int nyD;
        while(true){
            if(answer > 10000){
                return 0;
            }
            if(h[0] == d[0] && h[1] == d[1]){
                break;
            }
            nxH = h[0] + dx[dirH];
            nyH = h[1] + dy[dirH];
            nxD = d[0] + dx[dirD];
            nyD = d[1] + dy[dirD];
            if(nxH >= 0 && nxH < 10 && nyH >= 0 && nyH < 10 && board[nxH][nyH] != 1){
                h[0] = nxH;
                h[1] = nyH;
            }else{
                dirH = (dirH+1)%4;
            }
            if(nxD >= 0 && nxD < 10 && nyD >= 0 && nyD < 10 && board[nxD][nyD] != 1){
                d[0] = nxD;
                d[1] = nyD;
            }else{
                dirD = (dirD+1)%4;
            }

            answer++;
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_1_3 T = new inf2_1_3();
        int[][] arr1 = {
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 2, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 3, 0, 0, 0, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 0}};
        System.out.println(T.solution(arr1));
        int[][] arr2 = {
                {1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 1, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0, 0, 0, 0, 2, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 3}};
        System.out.println(T.solution(arr2));
    }
}
