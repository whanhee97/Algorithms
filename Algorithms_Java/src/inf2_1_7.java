import java.util.*;

public class inf2_1_7 {
    public int solutionMe(int[] keypad, String password){ // 시간초과나는 비효율적인 솔루션
        int answer = 0;
        char[][] pad = new char[3][3];
        int[] start = new int[]{0,0};
        for(int i=0;i<keypad.length;i++){
            pad[i/3][i%3] = (char)(keypad[i]+'0');
            if(keypad[i] == password.charAt(0)-'0') start = new int[]{i/3,i%3};
        }
        int[] dx = {1,-1,0,0,1,1,-1,-1};
        int[] dy = {0,0,1,-1,1,-1,1,-1};
        int[] cur = start;

        boolean isFound = false;
        for(int x=1;x<password.length();x++){
            char num = password.charAt(x);
            if(num == pad[cur[0]][cur[1]]){
                continue;
            }
            isFound = false;
            for(int i=0;i<8;i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if(nx >= 0 && nx < 3 && ny >= 0 && ny < 3 && pad[nx][ny] == num){
                    isFound = true;
                    cur = new int[]{nx,ny};
                    break;
                }
            }

            if(isFound){
                answer+=1;
            }else{
                answer+=2;
                for(int i=0;i<3;i++){
                    for(int j=0;j<3;j++){
                        if(num == pad[i][j]) cur = new int[]{i,j};
                    }
                }
            }
        }

        return answer;
    }

    public int solution(int[] keypad, String password){ // 정답
        int answer = 0;
        int[][] pad = new int[3][3];

        for(int i=0;i<keypad.length;i++){
            pad[i/3][i%3] = keypad[i];
        }
        int[][] dist = new int[10][10]; // 거리표 ( 1~9 하기 위해 9X9 -> 10X10 )
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if(i==j){
                    dist[i][j] = 0; // 자기 자신은 거리 0
                }else{
                    dist[i][j] = 2; // 2로 초기화
                }
            }
        }

        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                int now = pad[i][j];
                //System.out.println("----- now : " + now + " ------- ");
                //8방향 탐색해서 인접한 숫자는 거리 1로 수정
                int[] dx = {1,-1,0,0,1,1,-1,-1};
                int[] dy = {0,0,1,-1,1,-1,1,-1};
                for(int k=0;k<8;k++){
                    int nx = i+dx[k];
                    int ny = j+dy[k];
                    if(nx >= 0 && nx < 3 && ny >= 0 && ny < 3){
                        int nextNum = pad[nx][ny];
                        //System.out.println("nextNum : " + nextNum);
                        dist[now][nextNum] = 1;
                        dist[nextNum][now] = 1;

                    }
                }

            }
        }
        /*for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                System.out.print(dist[i][j]+" ");
            }
            System.out.println();
        }*/
        int now = password.charAt(0)-'0'; // 첫 번째 비밀번호 char to int
        for(int i=1;i<password.length();i++){ // 두 번째 비밀번호부터 거리 입력
            int next = password.charAt(i)-'0';
            answer += dist[now][next]; // 정답에 거리를 더해줌
            now = next;
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_1_7 T = new inf2_1_7();
        System.out.println(T.solution(new int[]{2, 5, 3, 7, 1, 6, 4, 9, 8}, "7596218"));
        System.out.println(T.solution(new int[]{1, 5, 7, 3, 2, 8, 9, 4, 6}, "63855526592"));
        System.out.println(T.solution(new int[]{2, 9, 3, 7, 8, 6, 4, 5, 1}, "323254677"));
        System.out.println(T.solution(new int[]{1, 6, 7, 3, 8, 9, 4, 5, 2}, "3337772122"));
    }
}
