//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String input = "\t[[\"e\", \"bs\"], [\"f\", \"cm\"], [\"f\", \"bb\"], [\"f\", \"sm\"]]";
        input = input.replace("[","{");
        input = input.replace("]","}");
        System.out.print(input);
    }
}