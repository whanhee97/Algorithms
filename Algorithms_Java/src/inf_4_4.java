import java.util.*;
public class inf_4_4 {
    public static int solution(String s1, String s2){
        int answer = 0;
        Map<Character,Integer> hm = new HashMap<>();
        Map<Character,Integer> hm2 = new HashMap<>();
        char[] carr = s1.toCharArray();
        for(int i=0;i<s2.length()-1;i++){
            hm.put(carr[i],hm.getOrDefault(carr[i],0)+1);
        }
        for(char c:s2.toCharArray()){
            hm2.put(c,hm2.getOrDefault(c,0)+1);
        }

        int lt = 0;
        for(int rt=s2.length()-1;rt<s1.length();rt++){
            hm.put(carr[rt],hm.getOrDefault(carr[rt],0)+1);
            if(hm.equals(hm2)){
                answer += 1;
            }
            if(hm.get(carr[lt])<=1){
                hm.remove(carr[lt]);
            }else{
                hm.put(carr[lt],hm.get(carr[lt])-1);
            }
            lt++;
        }


        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        String s1 = kb.next();
        String s2 = kb.next();

        System.out.println(solution(s1,s2));
        /*for(int x : solution(n,k,arr)){
            System.out.print(x + " ");
        }*/
    }
}
