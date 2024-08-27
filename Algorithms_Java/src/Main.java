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
        test1 T = new test1();
        int[][] ip = {{1000, 1}, {0, 10}};
        System.out.print(T.solution(ip,2000));
    }
}