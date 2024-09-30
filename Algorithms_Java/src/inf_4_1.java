import java.util.*;
public class inf_4_1 {
    public static char solution(int n,String v){

        HashMap<Character,Integer> hashMap = new HashMap<Character, Integer>();
        for(char c : v.toCharArray()){
            if(hashMap.get(c)!=null){
                hashMap.put(c,hashMap.get(c)+1);
            }else{
                hashMap.put(c,1);
            }
        }
        int mx = 0;
        char answer = ' ';
        for(char key : hashMap.keySet()){
            if(hashMap.get(key) > mx){
                mx = hashMap.get(key);
                answer = key;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        int n = kb.nextInt();
        String votes = kb.next();
        System.out.println(solution(n,votes));
    }
}
