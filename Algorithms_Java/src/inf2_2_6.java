import java.util.*;
class Report implements Comparable<Report>{
    String name;
    int time;
    public Report(String name, int time){
        this.name = name;
        this.time = time;
    }

    @Override
    public int compareTo(Report r){
        return this.time - r.time;
    }
}
public class inf2_2_6 {
    public String[] solution(String[] reports, String times){
        String[] answer = {};
        ArrayList<Report> reportList = new ArrayList<>();

        String from = times.split(" ")[0];
        int fromDigit =  Integer.parseInt(from.split(":")[0] + from.split(":")[1]);
        String to = times.split(" ")[1];
        int toDigit = Integer.parseInt(to.split(":")[0] + to.split(":")[1]);

        for(String r:reports){
            String name = r.split(" ")[0];
            int time = Integer.parseInt(r.split(" ")[1].split(":")[0] + r.split(" ")[1].split(":")[1]);

            if(time >= fromDigit && time <= toDigit){
                Report tmp = new Report(name,time);
                reportList.add(tmp);
            }
        }
        Collections.sort(reportList);

        answer = new String[reportList.size()];
        for(int i=0;i<reportList.size();i++){
            answer[i] = reportList.get(i).name;
        }

        return answer;
    }

    public static void main(String[] args){
        inf2_2_6 T = new inf2_2_6();
        System.out.println(Arrays.toString(T.solution(new String[]{"john 15:23", "daniel 09:30", "tom 07:23", "park 09:59", "luis 08:57"}, "08:33 09:45")));
        System.out.println(Arrays.toString(T.solution(new String[]{"ami 12:56", "daniel 15:00", "bob 19:59", "luis 08:57", "bill 17:35", "tom 07:23", "john 15:23", "park 09:59"}, "15:01 19:59")));
        System.out.println(Arrays.toString(T.solution(new String[]{"cody 14:20", "luis 10:12", "alice 15:40", "tom 15:20", "daniel 14:50"}, "14:20 15:20")));
    }
}
