//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.*;

public class Main {
    /*public static void main(String[] args) {
        String input = "[[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]";
        input = input.replace("[","{");
        input = input.replace("]","}");
        System.out.print(input);
    }*/


    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int v = kb.nextInt();
        int e = kb.nextInt();

        List<Road> roadList = new ArrayList<>();
        for(int i =0;i<e;i++){
            int a = kb.nextInt();
            int b = kb.nextInt();
            int cost = kb.nextInt();

            roadList.add(new Road(a,b,cost));
        }

        inf_9_7 T = new inf_9_7();

        System.out.print(T.solution2(v,e,roadList));
    }
}