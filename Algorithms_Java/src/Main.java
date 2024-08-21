//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.*;

public class Main {
    /*public static void main(String[] args) {
        String input = "[[0, 3], [1, 9], [2, 6]]";
        input = input.replace("[","{");
        input = input.replace("]","}");
        System.out.print(input);
    }*/


    public static void main(String[] args) {
        prog42627 T = new prog42627();
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        System.out.print(T.solution(jobs));
    }
}