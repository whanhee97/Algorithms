import java.util.*;
public class inf_4_3 {
    public static ArrayList<Integer> solution(int n, int k, int[] arr){
        Map<Integer,Integer> map = new HashMap<>();
        ArrayList<Integer> answer = new ArrayList<>();
        int st = 0;
        int ed = st+k-1;

        for(int i=0;i<=ed;i++){
            map.put(arr[i],map.getOrDefault(arr[i],0)+1);
        }
        while(ed<n){
            int cnt = 0;
            Collection<Integer> vals = map.values();
            cnt = vals.size();
            answer.add(cnt);
            ed++;
            if(ed<n){
                if(map.get(arr[st])<=1){
                    map.remove(arr[st]);
                }else{
                    map.put(arr[st],map.get(arr[st])-1);
                }
                map.put(arr[ed],map.getOrDefault(arr[ed],0)+1);
            }
            st++;

        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        int n = kb.nextInt();
        int k = kb.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = kb.nextInt();
        }
        //System.out.println(solution(s1,s2));
        for(int x : solution(n,k,arr)){
            System.out.print(x + " ");
        }
    }
}
