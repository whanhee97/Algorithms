import java.util.*;

public class prog32898 {
    static int[][] map;
    static int mm;
    static int nn;

    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        mm = m;
        nn = n;
        map = new int[nn][mm];
        for(int[] puddle : puddles){
            map[puddle[1]-1][puddle[0]-1] = -1;
        }
        // 1열을 -1 이 아니라면 1로 다 바꿔 주려했지만 이렇게 하면 [0,1][1,0]에 웅덩이가 있을때 결과가 0이 안 나와버림
        // 따라서 첫 -1이 나올때까지만 1로 바꿔주고 그 뒤로는 break 걸어줌
        for(int i=0;i<nn;i++){
            if(map[i][0] != -1)
                map[i][0] = 1;
            else break;
        }
        for(int i=0;i<mm;i++){
            if(map[0][i] != -1)
                map[0][i] = 1;
            else break;
        }
        for(int i=1;i<nn;i++){
            for(int j=1;j<mm;j++){
                if(map[i][j] != -1){
                    int a = map[i-1][j] == -1?0:map[i-1][j];
                    int b = map[i][j-1] == -1?0:map[i][j-1];
                    map[i][j] = (a+b) % 1000000007;
                }
            }
        }

        return map[nn-1][mm-1];
    }
}
